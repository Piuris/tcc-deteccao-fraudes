# Comparação estatística

CV repetida 5×3 no treino (15 partições, as mesmas para todas as configurações).

- Friedman: χ² = 373.10, p = 7.35e-61; Nemenyi CD = 12.50
- Melhor média: **XGBoost — Sem tratamento [busca50]** (0.7688)
- Regra: entre as configurações não significativamente piores que a melhor (t corrigido de Nadeau-Bengio, Holm, α=0,05) e a no máximo 0.01 de AUC-PR dela, a de maior AUC-PR entre as mais rápidas (tolerância 0.5 ms)
- Escolhida (parcimônia): **MLP (rede neural) — Subamostragem aleatória** (0.7614, p Holm vs. melhor = 0.395, latência 2.80 ms)

| configuração | AUC-PR (CV rep.) | ranking médio | p Holm vs. melhor | equivalente | latência ms | AUC-PR teste |
|---|---|---|---|---|---|---|
| XGBoost — Sem tratamento [busca50] | 0.7688 ± 0.0247 | 2.47 | 1.000 | sim | 3.47 | 0.8094 |
| XGBoost — Sem tratamento | 0.7680 ± 0.0248 | 3.33 | 0.467 | sim | 3.65 | 0.8062 |
| Ensemble XGBoost + LightGBM + RF — Melhor de cada membro [ensemble] | 0.7675 ± 0.0248 | 4.07 | 0.663 | sim | 21.09 | 0.8082 |
| XGBoost — Subamostragem aleatória [busca50] | 0.7673 ± 0.0238 | 4.20 | 0.663 | sim | 3.44 | 0.8086 |
| Ensemble XGBoost + LightGBM — Melhor de cada membro [ensemble] | 0.7672 ± 0.0248 | 4.40 | 0.437 | sim | 3.91 | 0.8070 |
| LightGBM — Subamostragem aleatória [busca50] | 0.7626 ± 0.0245 | 10.20 | 0.021 | não | 3.58 | 0.8006 |
| LightGBM — Sem tratamento [busca50] | 0.7614 ± 0.0252 | 12.07 | 0.057 | sim | 3.58 | 0.8006 |
| MLP (rede neural) — Subamostragem aleatória | 0.7614 ± 0.0249 | 12.20 | 0.395 | sim | 2.80 | 0.7999 |
| MLP (rede neural) — SMOTE | 0.7610 ± 0.0224 | 12.00 | 0.216 | sim | 2.74 | 0.8020 |
| XGBoost — SMOTE [busca50] | 0.7609 ± 0.0234 | 12.20 | 0.086 | sim | 3.45 | 0.8007 |
| XGBoost — Subamostragem aleatória | 0.7608 ± 0.0252 | 12.00 | 0.004 | não | 3.52 | 0.8005 |
| MLP (rede neural) — Sem tratamento | 0.7606 ± 0.0213 | 11.73 | 0.400 | sim | 2.74 | 0.8055 |
| Random Forest — SMOTE | 0.7604 ± 0.0245 | 12.87 | 0.219 | sim | 16.61 | 0.8000 |
| XGBoost — SMOTE | 0.7599 ± 0.0245 | 13.33 | 0.023 | não | 3.64 | 0.8017 |
| XGBoost — Sensível a custo (pesos) [busca50] | 0.7596 ± 0.0234 | 13.20 | 0.086 | sim | 3.48 | 0.7980 |
| XGBoost — Sensível a custo (pesos) | 0.7595 ± 0.0229 | 13.80 | 0.108 | sim | 3.52 | 0.8010 |
| Random Forest — Sem tratamento | 0.7594 ± 0.0256 | 13.53 | 0.095 | sim | 16.34 | 0.8018 |
| LightGBM — Sem tratamento | 0.7579 ± 0.0260 | 15.60 | 0.003 | não | 3.58 | 0.7922 |
| LightGBM — SMOTE [busca50] | 0.7569 ± 0.0259 | 16.53 | 0.002 | não | 3.64 | 0.7945 |
| MLP (rede neural) — Sensível a custo (pesos) | 0.7561 ± 0.0257 | 16.33 | 0.231 | sim | 2.77 | 0.8050 |
| LightGBM — SMOTE | 0.7534 ± 0.0239 | 20.40 | 0.002 | não | 3.55 | 0.7908 |
| Random Forest — Subamostragem aleatória | 0.7531 ± 0.0243 | 20.53 | 0.016 | não | 16.54 | 0.7971 |
| Random Forest — Sensível a custo (pesos) | 0.7519 ± 0.0250 | 21.20 | 0.000 | não | 16.90 | 0.7917 |
| LightGBM — Subamostragem aleatória | 0.7474 ± 0.0262 | 22.40 | 0.003 | não | 3.57 | 0.7836 |
| LightGBM — Sensível a custo (pesos) | 0.7356 ± 0.0270 | 25.27 | 0.000 | não | 3.61 | 0.7641 |
| LightGBM — Sensível a custo (pesos) [busca50] | 0.7355 ± 0.0218 | 25.13 | 0.003 | não | 3.66 | 0.7625 |
| Regressão Logística (referência) — Sem tratamento | 0.5838 ± 0.0298 | 27.00 | 0.000 | não | 2.84 | 0.6076 |
| Regressão Logística (referência) — Subamostragem aleatória | 0.5758 ± 0.0307 | 28.00 | 0.000 | não | 2.76 | 0.5963 |
| Regressão Logística (referência) — SMOTE | 0.5323 ± 0.0311 | 29.13 | 0.000 | não | 2.72 | 0.5412 |
| Isolation Forest (não supervisionado) — Sem tratamento | 0.5090 ± 0.0332 | 29.87 | 0.000 | não | 3.54 | 0.5328 |
| Regressão Logística (referência) — Sensível a custo (pesos) | 0.4550 ± 0.0312 | 31.00 | 0.000 | não | 2.74 | 0.4582 |