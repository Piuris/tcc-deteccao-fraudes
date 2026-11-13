"""Análises de robustez dos resultados principais.

Cada função responde a uma pergunta que os números do capítulo de resultados
deixam em aberto: quanto do efeito das duplicatas é vazamento quando o modelo
fica fixo, qual a incerteza das métricas do modelo final no limiar escolhido,
se o limiar obtido é coerente com probabilidades calibradas e se o desempenho
no PaySim depende do tipo de operação.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, brier_score_loss

from .config import COST_SCENARIOS, SEED, CostConfig
from .data import TIME_COLUMNS
from .evaluation import classification_metrics, cost_report

FIXED_COST_SCENARIOS = {k: c for k, c in COST_SCENARIOS.items() if not c.fn_use_amount}
EXTRA_FN_COSTS = (20.0, 50.0)


def stratified_bootstrap(y, stat, n_boot: int = 500, seed: int = SEED) -> dict[str, np.ndarray]:
    """Reamostra fraudes e legítimas separadamente e devolve, para cada
    estatística de ``stat(idx)``, os valores das ``n_boot`` reamostragens."""
    y = np.asarray(y).astype(int)
    rng = np.random.default_rng(seed)
    pos, neg = np.flatnonzero(y == 1), np.flatnonzero(y == 0)
    values: dict[str, list[float]] = {}
    for _ in range(n_boot):
        idx = np.concatenate([rng.choice(pos, len(pos)), rng.choice(neg, len(neg))])
        for k, v in stat(idx).items():
            values.setdefault(k, []).append(v)
    return {k: np.asarray(v, dtype=float) for k, v in values.items()}


def interval(values: np.ndarray, alpha: float = 0.05) -> list[float]:
    lo, hi = np.quantile(values, [alpha / 2, 1 - alpha / 2])
    return [float(lo), float(hi)]


def elkan_threshold(cost: CostConfig) -> float:
    """Limiar de custo mínimo para probabilidades calibradas (Elkan, 2001)."""
    return cost.fp / (cost.fp + cost.fn)


def brier_skill(y, proba) -> float:
    """1 − Brier do modelo / Brier do preditor constante na prevalência."""
    y = np.asarray(y).astype(int)
    prev = y.mean()
    return float(1 - brier_score_loss(y, proba) / (prev * (1 - prev)))


def _cost_summary(y, proba, threshold: float, cost: CostConfig) -> dict:
    r = cost_report(y, proba, threshold, cost)
    return {"threshold": float(threshold), "cost": r["cost"],
            "savings_vs_best_trivial_pct": r["savings_vs_best_trivial_pct"]}


def final_model_robustness(y, raw, proba, threshold: float, types=None, scenario: str = "moderado",
                           n_boot: int = 500, seed: int = SEED) -> dict:
    """Incerteza e sensibilidade do modelo final no conjunto de teste.

    ``raw`` é o escore do modelo antes da calibração e ``proba`` o escore
    servido pela API. ``types`` (tipo de operação, no PaySim) permite separar
    o desempenho por tipo.
    """
    y = np.asarray(y).astype(int)
    raw, proba = np.asarray(raw, dtype=float), np.asarray(proba, dtype=float)
    cost = COST_SCENARIOS[scenario]
    pred = proba >= threshold
    n_pos = int(y.sum())

    def stat(idx):
        yy, pp, rr, hh = y[idx], proba[idx], raw[idx], pred[idx]
        tp = int((hh & (yy == 1)).sum())
        fp = int((hh & (yy == 0)).sum())
        fn = n_pos - tp
        model_cost = fn * cost.fn + fp * cost.fp
        trivial = min(n_pos * cost.fn, int((yy == 0).sum()) * cost.fp)
        return {"precision": tp / max(tp + fp, 1), "recall": tp / n_pos, "cost": model_cost,
                "savings_vs_best_trivial_pct": 100 * (1 - model_cost / trivial),
                "brier_skill": brier_skill(yy, pp),
                "brier_delta": brier_score_loss(yy, pp) - brier_score_loss(yy, np.clip(rr, 0, 1))}

    boot = stratified_bootstrap(y, stat, n_boot=n_boot, seed=seed)
    sensitivity = []
    for name, c in FIXED_COST_SCENARIOS.items():
        sensitivity.append({"scenario": name, "fn": c.fn, "fp": c.fp,
                            "elkan": _cost_summary(y, proba, elkan_threshold(c), c),
                            "chosen_threshold": _cost_summary(y, proba, threshold, c)})
    for fn in EXTRA_FN_COSTS:
        c = CostConfig(fn=fn, fp=cost.fp)
        sensitivity.append({"scenario": f"fn_{fn:g}", "fn": c.fn, "fp": c.fp,
                            "elkan": _cost_summary(y, proba, elkan_threshold(c), c),
                            "chosen_threshold": _cost_summary(y, proba, threshold, c)})

    out = {
        "n_boot": n_boot,
        "confusion": {k: classification_metrics(y, proba, threshold)[k] for k in ("tp", "fp", "tn", "fn")},
        "prevalence": float(y.mean()),
        "brier_reference": float(y.mean() * (1 - y.mean())),
        "brier_skill_raw": brier_skill(y, np.clip(raw, 0, 1)),
        "brier_skill_calibrated": brier_skill(y, proba),
        "ci95": {k: interval(v) for k, v in boot.items() if k != "brier_delta"},
        "share_bootstrap_brier_improved": float((boot["brier_delta"] < 0).mean()),
        "cost_sensitivity": sensitivity,
        "raw_threshold_05": _cost_summary(y, raw, 0.5, cost),
        "distinct_scores": int(len(np.unique(proba))),
        "frauds_with_score_1": int(((proba >= 1.0) & (y == 1)).sum()),
        "legit_with_score_1": int(((proba >= 1.0) & (y == 0)).sum()),
    }
    if types is not None:
        types = np.asarray(types)
        out["by_type"] = []
        for t in np.unique(types):
            m = types == t
            if y[m].sum() == 0:
                continue
            out["by_type"].append({
                "type": str(t), "n": int(m.sum()), "frauds": int(y[m].sum()),
                "prevalence": float(y[m].mean()),
                "auc_pr": float(average_precision_score(y[m], proba[m])),
                "detected": int((pred[m] & (y[m] == 1)).sum()),
                "false_positives": int((pred[m] & (y[m] == 0)).sum())})
    return out


def row_keys(X: pd.DataFrame, y) -> np.ndarray:
    """Chave de cada linha pelos atributos e rótulo, ignorando o instante."""
    cols = [c for c in X.columns if c not in TIME_COLUMNS]
    return pd.util.hash_pandas_object(X[cols].assign(_y=np.asarray(y)), index=False).to_numpy()


def duplicate_effect_fixed_model(X: pd.DataFrame, y, train_idx, test_idx, pipeline) -> dict:
    """Efeito do vazamento com o modelo fixo.

    Treina ``pipeline`` na partição de treino que ainda contém duplicatas e o
    avalia no mesmo teste, com e sem as linhas que têm cópia exata no treino.
    Como o modelo e o restante do teste não mudam, a diferença isola o
    vazamento da variação causada pela troca do conjunto de teste.
    """
    y = np.asarray(y).astype(int)
    keys = row_keys(X, y)
    has_copy = np.isin(keys[test_idx], keys[train_idx])
    y_te = y[test_idx]
    pipeline.fit(X.iloc[train_idx], y[train_idx])
    p = pipeline.predict_proba(X.iloc[test_idx])[:, 1]
    fraud = y_te == 1
    copied, clean = fraud & has_copy, fraud & ~has_copy
    return {
        "test_frauds": int(fraud.sum()),
        "frauds_with_copy": int(copied.sum()),
        "legit_with_copy": int((~fraud & has_copy).sum()),
        "auc_pr_full_test": float(average_precision_score(y_te, p)),
        "auc_pr_without_copies": float(average_precision_score(y_te[~has_copy], p[~has_copy])),
        "score_frauds_with_copy_mean": float(p[copied].mean()) if copied.any() else float("nan"),
        "score_frauds_with_copy_min": float(p[copied].min()) if copied.any() else float("nan"),
        "score_frauds_without_copy_mean": float(p[clean].mean()) if clean.any() else float("nan"),
    }
