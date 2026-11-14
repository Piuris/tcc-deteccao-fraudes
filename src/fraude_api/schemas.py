"""Contratos de entrada e saída da API.

A validação é feita pelo Pydantic a partir das anotações de tipo: campos
ausentes, tipos errados, valores negativos onde não cabem e NaN/infinito são
recusados com HTTP 422 antes de chegar ao modelo.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, create_model

STRICT = ConfigDict(allow_inf_nan=False, extra="forbid")


class _Base(BaseModel):
    model_config = STRICT
    transaction_id: str | None = Field(None, max_length=64, description="Identificador opcional, devolvido na resposta.")


_v_fields = {
    f"V{i}": (float, Field(..., description=f"Componente principal {i} (anonimizada por PCA)."))
    for i in range(1, 29)
}

CreditCardTransaction = create_model(
    "CreditCardTransaction",
    __base__=_Base,
    Time=(float, Field(..., ge=0, description="Segundos desde a primeira transação da base.")),
    Amount=(float, Field(..., ge=0, description="Valor da transação.")),
    **_v_fields,
)
CreditCardTransaction.model_config["json_schema_extra"] = {
    "example": {"transaction_id": "tx-001", "Time": 406.0, "Amount": 0.0,
                **{f"V{i}": 0.0 for i in range(1, 29)}}
}


class PaySimTransaction(_Base):
    step: int = Field(..., ge=0, description="Hora da simulação (1 passo = 1 hora).")
    type: Literal["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
    amount: float = Field(..., ge=0)
    oldbalanceOrg: float = Field(..., ge=0, description="Saldo da origem antes da operação.")
    newbalanceOrig: float = Field(..., ge=0, description="Saldo da origem depois da operação.")
    oldbalanceDest: float = Field(..., ge=0, description="Saldo do destino antes da operação.")
    newbalanceDest: float = Field(..., ge=0, description="Saldo do destino depois da operação.")
    nameDest: str = Field("C0", pattern=r"^[CM]\w*$", description="Destino; prefixo M = estabelecimento.")

    model_config = ConfigDict(**STRICT, json_schema_extra={"example": {
        "transaction_id": "tx-002", "step": 1, "type": "TRANSFER", "amount": 181.0,
        "oldbalanceOrg": 181.0, "newbalanceOrig": 0.0, "oldbalanceDest": 0.0,
        "newbalanceDest": 0.0, "nameDest": "C553264065"}})


class Factor(BaseModel):
    feature: str = Field(description="Nome do atributo.")
    value: float = Field(description="Valor do atributo depois do pré-processamento (o que o modelo "
                                     "vê); por isso pode diferir do valor enviado.")
    contribution: float = Field(description="Valor SHAP: quanto o atributo empurrou o escore. Positivo "
                                            "aumenta o risco; negativo reduz. Na escala do modelo "
                                            "(log-odds no XGBoost da ULB, probabilidade no Random "
                                            "Forest do PaySim).")
    direction: Literal["aumenta_risco", "reduz_risco"] = Field(description="Sinal da contribuição, por extenso.")


class Prediction(BaseModel):
    transaction_id: str | None = Field(description="O identificador enviado na requisição.")
    fraud_probability: float = Field(ge=0, le=1, description="Probabilidade calibrada de fraude, de 0 a 1.")
    threshold: float = Field(description="Limiar de bloqueio, escolhido pela função de custo "
                                         "(cenário moderado).")
    decision: Literal["bloquear", "aprovar"] = Field(description="\"bloquear\" se fraud_probability ≥ "
                                                                 "threshold; senão, \"aprovar\".")
    is_fraud: bool = Field(description="A mesma decisão, como verdadeiro/falso.")
    top_factors: list[Factor] | None = Field(None, description="Os cinco atributos que mais pesaram "
                                                               "(SHAP). Vazio se explain=false.")
    explanation_method: str | None = Field(None, description="Método da explicação (shap_tree = SHAP "
                                                             "exato para árvores).")
    model_version: str = Field(description="Algoritmo, balanceamento e data do treino do modelo servido.")
    latency_ms: float = Field(description="Tempo de processamento no servidor, em milissegundos, sem "
                                          "contar a rede.")


class BatchResponse(BaseModel):
    predictions: list[Prediction] = Field(description="Uma predição por transação, na ordem enviada.")
    latency_ms: float = Field(description="Tempo total do lote no servidor, em milissegundos.")


class ValidationIssue(BaseModel):
    type: str = Field(description="Tipo do problema (ex.: missing, greater_than_equal).")
    loc: list[str | int] = Field(description="Onde está o problema: parte da requisição e nome do campo.")
    msg: str = Field(description="Mensagem do validador.")


class ValidationErrorResponse(BaseModel):
    detail: list[ValidationIssue] = Field(description="Um item por campo com problema.")


class ModelInfo(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    kind: str
    loaded: bool
    metadata: dict | None = None
