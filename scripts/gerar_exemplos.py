"""Seleciona transações reais do conjunto de teste para servirem de exemplo na API.

Usa a mesma separação treino/teste dos experimentos (semente 42, 80/20 estratificado),
de modo que nenhum exemplo foi visto pelo modelo no treino. Grava
``src/fraude_api/exemplos.json``, lido pela API para preencher o Swagger.

    python scripts/gerar_exemplos.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from fraude.artifact import Predictor, artifact_path
from fraude.config import ExperimentConfig
from fraude.data import load_dataset
from fraude.experiments import split_train_test

OUT = Path(__file__).resolve().parents[1] / "src" / "fraude_api" / "exemplos.json"

CASOS = {
    "vp": ("Fraude detectada", "Fraude real que o modelo bloqueia (verdadeiro positivo)."),
    "vn": ("Transação legítima", "Compra legítima que o modelo aprova (verdadeiro negativo)."),
    "fp": ("Falso alarme", "Compra legítima que o modelo bloqueia (falso positivo)."),
    "fn": ("Fraude não detectada", "Fraude real que passa pelo modelo (falso negativo)."),
}


def _clean(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if isinstance(v, (np.integer,)):
            v = int(v)
        elif isinstance(v, (np.floating, float)):
            v = round(float(v), 6)
        out[k] = v
    return out


def exemplos(kind: str, dataset: str, sample_frac: float | None) -> dict:
    cfg = ExperimentConfig()
    ds = load_dataset(dataset, sample_frac=sample_frac, seed=cfg.seed)
    _, te = split_train_test(ds, cfg)
    X, y = ds.X.iloc[te].reset_index(drop=True), ds.y.iloc[te].to_numpy()
    pred = Predictor.load(artifact_path(kind))
    p = pred.predict_proba(X)
    hit = p >= pred.threshold
    grupos = {"vp": (y == 1) & hit, "vn": (y == 0) & ~hit, "fp": (y == 0) & hit, "fn": (y == 1) & ~hit}
    out = {}
    for caso, mask in grupos.items():
        idx = np.flatnonzero(mask)
        if not len(idx):
            continue
        i = idx[np.argsort(p[idx])[len(idx) // 2]]
        titulo, desc = CASOS[caso]
        out[caso] = {
            "summary": titulo,
            "description": f"{desc} Transação real do conjunto de teste; probabilidade esperada ≈ {p[i]:.4f}.",
            "value": {"transaction_id": f"{kind}-{caso}", **_clean(X.iloc[i].to_dict())},
        }
    return out


if __name__ == "__main__":
    data = {"creditcard": exemplos("creditcard", "creditcard", None),
            "paysim": exemplos("paysim", "paysim", 0.2)}
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    for k, v in data.items():
        print(k, {c: e["description"].split("≈ ")[1] for c, e in v.items()})
