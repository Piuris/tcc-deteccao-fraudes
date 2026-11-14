"""Gera as respostas de exemplo mostradas no Swagger.

Envia cada transação de ``src/fraude_api/exemplos.json`` à própria API, com os
modelos de ``artifacts/``, e grava as respostas em
``src/fraude_api/respostas.json``. Assim, a seção "Responses" da documentação
mostra o que a API devolve de fato para cada exemplo, inclusive um erro de
validação (HTTP 422).

    python scripts/gerar_respostas.py
"""

from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from fraude_api.main import EXEMPLOS, create_app

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "fraude_api" / "respostas.json"


def _round(obj):
    if isinstance(obj, float):
        return round(obj, 4)
    if isinstance(obj, list):
        return [_round(v) for v in obj]
    if isinstance(obj, dict):
        return {k: _round(v) for k, v in obj.items()}
    return obj


def respostas(client: TestClient, kind: str) -> dict:
    out = {"200": {}, "422": {}}
    for caso, ex in EXEMPLOS[kind].items():
        r = client.post(f"/v1/{kind}/predict", json=ex["value"])
        r.raise_for_status()
        body = r.json()
        p, t, decisao = body["fraud_probability"], body["threshold"], body["decision"]
        sinal = "maior ou igual ao" if decisao == "bloquear" else "menor que o"
        p_br, t_br = f"{p:.4f}".replace(".", ","), f"{t:.4f}".replace(".", ",")
        desc = (f"Resposta da API ao exemplo de requisição \"{ex['summary']}\". A probabilidade "
                f"({p_br}) é {sinal} limiar ({t_br}), por isso a decisão é \"{decisao}\". "
                "Em `top_factors`, `value` é o atributo depois do pré-processamento (por isso difere "
                "do valor enviado) e `contribution` é o valor SHAP: positivo aumenta o risco, "
                "negativo reduz. `latency_ms` aqui foi medido em execução local.")
        out["200"][caso] = {"summary": ex["summary"], "description": desc, "value": _round(body)}

    base = next(iter(EXEMPLOS[kind].values()))["value"]
    campo = "Amount" if kind == "creditcard" else "amount"
    erros = {
        "negativo": ("Valor negativo", f"`{campo}` enviado como -10: a API recusa antes de chegar ao modelo.",
                     {**base, campo: -10}),
        "ausente": ("Campo obrigatório ausente", f"Requisição sem o campo `{campo}`.",
                    {k: v for k, v in base.items() if k != campo}),
    }
    for caso, (titulo, desc, payload) in erros.items():
        r = client.post(f"/v1/{kind}/predict", json=payload)
        assert r.status_code == 422, r.text
        detail = [{k: v for k, v in d.items() if k in ("type", "loc", "msg")} for d in r.json()["detail"]]
        out["422"][caso] = {"summary": titulo, "description": desc, "value": {"detail": detail}}
    return out


if __name__ == "__main__":
    with TestClient(create_app(ROOT / "artifacts")) as client:
        data = {kind: respostas(client, kind) for kind in EXEMPLOS}
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    for kind, v in data.items():
        print(kind, {c: e["value"]["decision"] for c, e in v["200"].items()})
