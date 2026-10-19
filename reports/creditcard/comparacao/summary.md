# Comparação estatística

CV repetida 5×3 no treino (15 partições, as mesmas para todas as configurações).

- Friedman: χ² = 327.52, p = 9.47e-52; Nemenyi CD = 12.50
- Melhor média: **Ensemble XGBoost + LightGBM — Melhor de cada membro [ensemble]** (0.8573)
- Regra: entre as configurações não significativamente piores que a melhor (t corrigido de Nadeau-Bengio, Holm, α=0,05) e a no máximo 0.01 de AUC-PR dela, a de maior AUC-PR entre as mais rápidas (tolerância 0.5 ms)
- Escolhida (parcimônia): **XGBoost — Sensível a custo (pesos) [busca50]** (0.8566, p Holm vs. melhor = 1.000, latência 2.05 ms)

| configuração | AUC-PR (CV rep.) | ranking médio | p Holm vs. melhor | equivalente | latência ms | AUC-PR teste |
|---|---|---|---|---|---|---|
| Ensemble XGBoost + LightGBM — Melhor de cada membro [ensemble] | 0.8573 ± 0.0326 | 5.60 | 1.000 | sim | 2.90 | 0.8466 |
| XGBoost — Sensível a custo (pesos) [busca50] | 0.8566 ± 0.0325 | 6.00 | 1.000 | sim | 2.05 | 0.8393 |
| LightGBM — SMOTE [busca50] | 0.8563 ± 0.0297 | 7.33 | 1.000 | sim | 2.30 | 0.8441 |
| LightGBM — Sem tratamento [busca50] | 0.8555 ± 0.0350 | 7.70 | 1.000 | sim | 2.28 | 0.8294 |
| LightGBM — Sem tratamento | 0.8555 ± 0.0350 | 7.70 | 1.000 | sim | 2.32 | 0.8294 |
| LightGBM — SMOTE | 0.8547 ± 0.0296 | 8.80 | 1.000 | sim | 2.18 | 0.8419 |
| XGBoost — SMOTE | 0.8547 ± 0.0309 | 8.63 | 1.000 | sim | 2.06 | 0.8403 |
| XGBoost — SMOTE [busca50] | 0.8547 ± 0.0309 | 8.63 | 1.000 | sim | 2.05 | 0.8403 |
| Ensemble XGBoost + LightGBM + RF — Melhor de cada membro [ensemble] | 0.8535 ± 0.0370 | 8.00 | 1.000 | sim | 17.69 | 0.8343 |
| XGBoost — Sensível a custo (pesos) | 0.8531 ± 0.0319 | 10.67 | 1.000 | sim | 2.07 | 0.8434 |
| XGBoost — Sem tratamento | 0.8522 ± 0.0355 | 10.40 | 1.000 | sim | 2.05 | 0.8400 |
| XGBoost — Sem tratamento [busca50] | 0.8517 ± 0.0339 | 9.93 | 1.000 | sim | 2.02 | 0.8382 |
| Random Forest — SMOTE | 0.8500 ± 0.0388 | 11.27 | 1.000 | sim | 15.28 | 0.8215 |
| LightGBM — Subamostragem aleatória [busca50] | 0.8465 ± 0.0365 | 13.47 | 1.000 | sim | 2.29 | 0.8266 |
| XGBoost — Subamostragem aleatória [busca50] | 0.8453 ± 0.0339 | 14.93 | 0.754 | sim | 2.04 | 0.8326 |
| LightGBM — Subamostragem aleatória | 0.8446 ± 0.0352 | 15.13 | 1.000 | sim | 2.16 | 0.8209 |
| XGBoost — Subamostragem aleatória | 0.8397 ± 0.0352 | 17.53 | 0.230 | sim | 2.05 | 0.8247 |
| Random Forest — Sem tratamento | 0.8385 ± 0.0395 | 17.20 | 0.754 | sim | 15.26 | 0.8190 |
| Random Forest — Sensível a custo (pesos) | 0.8360 ± 0.0414 | 18.33 | 0.618 | sim | 14.71 | 0.8186 |
| MLP (rede neural) — Sem tratamento | 0.8338 ± 0.0361 | 17.40 | 0.892 | sim | 1.55 | 0.8114 |
| MLP (rede neural) — Sensível a custo (pesos) | 0.8242 ± 0.0348 | 21.13 | 0.230 | sim | 1.56 | 0.8153 |
| MLP (rede neural) — SMOTE | 0.8238 ± 0.0309 | 19.80 | 0.383 | sim | 1.54 | 0.8140 |
| LightGBM — Sensível a custo (pesos) [busca50] | 0.8169 ± 0.0583 | 19.37 | 1.000 | sim | 2.38 | 0.8248 |
| LightGBM — Sensível a custo (pesos) | 0.8169 ± 0.0583 | 19.37 | 1.000 | sim | 2.21 | 0.8248 |
| Random Forest — Subamostragem aleatória | 0.8168 ± 0.0455 | 21.53 | 0.774 | sim | 15.21 | 0.7866 |
| Regressão Logística (referência) — Sem tratamento | 0.7502 ± 0.0544 | 27.27 | 0.002 | não | 1.56 | 0.7320 |
| Regressão Logística (referência) — Subamostragem aleatória | 0.7472 ± 0.0577 | 27.73 | 0.002 | não | 1.86 | 0.7306 |
| Regressão Logística (referência) — SMOTE | 0.7462 ± 0.0578 | 28.13 | 0.002 | não | 1.64 | 0.7329 |
| MLP (rede neural) — Subamostragem aleatória | 0.7437 ± 0.0581 | 27.27 | 0.009 | não | 1.56 | 0.6719 |
| Regressão Logística (referência) — Sensível a custo (pesos) | 0.7343 ± 0.0667 | 28.73 | 0.010 | não | 1.53 | 0.6969 |
| Isolation Forest (não supervisionado) — Sem tratamento | 0.2735 ± 0.0694 | 31.00 | 0.000 | não | 3.80 | 0.2385 |