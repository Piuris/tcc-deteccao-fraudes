# Resultados — ulb_creditcard

- Transações: 275.663 | fraudes: 473 (0.1716%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Sensível a custo (pesos) | 0.8564 ± 0.0236 | 0.8434 | [0.774, 0.906] | 0.9834 | 0.8021 | 0.8105 | 0.8063 | 0.8060 | 19 | 18 | 80.05 | 3.63 | 2.07 | 2.14 |
| LightGBM | SMOTE | 0.8568 ± 0.0233 | 0.8419 | [0.770, 0.905] | 0.9683 | 0.7364 | 0.8526 | 0.7902 | 0.7920 | 29 | 14 | 83.74 | 2.75 | 2.18 | 2.27 |
| XGBoost | SMOTE | 0.8548 ± 0.0243 | 0.8403 | [0.773, 0.903] | 0.9810 | 0.8444 | 0.8000 | 0.8216 | 0.8216 | 14 | 19 | 79.26 | 3.14 | 2.06 | 2.16 |
| XGBoost | Sem tratamento | 0.8528 ± 0.0279 | 0.8400 | [0.771, 0.900] | 0.9810 | 0.8352 | 0.8000 | 0.8172 | 0.8171 | 15 | 19 | 79.21 | 2.53 | 2.05 | 2.14 |
| LightGBM | Sem tratamento | 0.8563 ± 0.0279 | 0.8294 | [0.754, 0.895] | 0.9738 | 0.7723 | 0.8211 | 0.7959 | 0.7959 | 23 | 17 | 80.89 | 3.28 | 2.32 | 2.35 |
| LightGBM | Sensível a custo (pesos) | 0.8430 ± 0.0228 | 0.8248 | [0.750, 0.892] | 0.9305 | 0.6696 | 0.8105 | 0.7333 | 0.7362 | 38 | 18 | 79.05 | 3.41 | 2.21 | 2.34 |
| XGBoost | Subamostragem aleatória | 0.8443 ± 0.0280 | 0.8247 | [0.753, 0.891] | 0.9793 | 0.6610 | 0.8211 | 0.7324 | 0.7362 | 40 | 17 | 80.00 | 1.26 | 2.05 | 2.20 |
| Random Forest | SMOTE | 0.8509 ± 0.0259 | 0.8215 | [0.749, 0.887] | 0.9805 | 0.6964 | 0.8211 | 0.7536 | 0.7557 | 34 | 17 | 80.32 | 38.15 | 15.28 | 15.77 |
| LightGBM | Subamostragem aleatória | 0.8503 ± 0.0277 | 0.8209 | [0.750, 0.888] | 0.9766 | 0.6220 | 0.8316 | 0.7117 | 0.7187 | 48 | 16 | 80.63 | 1.33 | 2.16 | 2.25 |
| Random Forest | Sem tratamento | 0.8414 ± 0.0306 | 0.8190 | [0.742, 0.886] | 0.9519 | 0.7290 | 0.8211 | 0.7723 | 0.7732 | 29 | 17 | 80.58 | 62.90 | 15.26 | 15.92 |
| Random Forest | Sensível a custo (pesos) | 0.8384 ± 0.0301 | 0.8186 | [0.745, 0.888] | 0.9634 | 0.6475 | 0.8316 | 0.7281 | 0.7333 | 43 | 16 | 80.89 | 32.28 | 14.71 | 15.31 |
| MLP (rede neural) | Sensível a custo (pesos) | 0.8207 ± 0.0313 | 0.8153 | [0.743, 0.883] | 0.9591 | 0.6320 | 0.8316 | 0.7182 | 0.7244 | 46 | 16 | 80.74 | 8.29 | 1.56 | 1.84 |
| MLP (rede neural) | SMOTE | 0.8218 ± 0.0319 | 0.8140 | [0.740, 0.885] | 0.9578 | 0.6814 | 0.8105 | 0.7404 | 0.7427 | 36 | 18 | 79.16 | 9.22 | 1.54 | 1.62 |
| MLP (rede neural) | Sem tratamento | 0.8286 ± 0.0189 | 0.8114 | [0.737, 0.883] | 0.9685 | 0.5195 | 0.8421 | 0.6426 | 0.6607 | 74 | 15 | 80.32 | 6.54 | 1.55 | 1.67 |
| Random Forest | Subamostragem aleatória | 0.8283 ± 0.0279 | 0.7866 | [0.709, 0.861] | 0.9810 | 0.7476 | 0.8105 | 0.7778 | 0.7780 | 26 | 18 | 79.68 | 12.25 | 15.21 | 15.89 |
| Regressão Logística (referência) | SMOTE | 0.7455 ± 0.0442 | 0.7329 | [0.640, 0.830] | 0.9791 | 0.6240 | 0.8211 | 0.7091 | 0.7152 | 47 | 17 | 79.63 | 1.33 | 1.64 | 1.65 |
| Regressão Logística (referência) | Sem tratamento | 0.7519 ± 0.0397 | 0.7320 | [0.642, 0.826] | 0.9687 | 0.5786 | 0.8526 | 0.6894 | 0.7018 | 59 | 14 | 82.16 | 1.19 | 1.56 | 1.71 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.7444 ± 0.0468 | 0.7306 | [0.641, 0.824] | 0.9840 | 0.5896 | 0.8316 | 0.6900 | 0.6996 | 55 | 16 | 80.26 | 0.90 | 1.86 | 2.53 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.7349 ± 0.0560 | 0.6969 | [0.601, 0.802] | 0.9820 | 0.5985 | 0.8316 | 0.6960 | 0.7049 | 53 | 16 | 80.37 | 1.23 | 1.53 | 1.60 |
| MLP (rede neural) | Subamostragem aleatória | 0.7354 ± 0.0465 | 0.6719 | [0.568, 0.770] | 0.9377 | 0.8022 | 0.7684 | 0.7849 | 0.7848 | 18 | 22 | 75.89 | 1.88 | 1.56 | 1.69 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.2664 ± 0.0584 | 0.2385 | [0.165, 0.334] | 0.9576 | 0.1686 | 0.4526 | 0.2457 | 0.2743 | 212 | 52 | 34.11 | 5.30 | 3.80 | 3.93 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| Regressão Logística (referência) | 0.1717 | 0.00074 | 0.00069 |
| Random Forest | 0.1717 | 0.00072 | 0.00060 |
| XGBoost | 0.1717 | 0.00064 | 0.00055 |
| LightGBM | 0.1717 | 0.00068 | 0.00066 |
| MLP (rede neural) | 0.1717 | 0.00068 | 0.00068 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| MLP (rede neural) | Sensível a custo (pesos) | 0.800165 | 3,253.08 | 14,760.99 | 275,190.00 | 77.96 | 77.96 |
| XGBoost | Subamostragem aleatória | 0.265877 | 3,398.29 | 14,760.99 | 275,190.00 | 76.98 | 76.98 |
| LightGBM | SMOTE | 0.066580 | 3,704.56 | 14,760.99 | 275,190.00 | 74.90 | 74.90 |
| XGBoost | Sensível a custo (pesos) | 0.522801 | 3,744.56 | 14,760.99 | 275,190.00 | 74.63 | 74.63 |
| XGBoost | SMOTE | 0.224067 | 3,749.56 | 14,760.99 | 275,190.00 | 74.60 | 74.60 |
| LightGBM | Sem tratamento | 0.000216 | 3,759.46 | 14,760.99 | 275,190.00 | 74.53 | 74.53 |
| Regressão Logística (referência) | Sem tratamento | 0.032859 | 3,764.56 | 14,760.99 | 275,190.00 | 74.50 | 74.50 |
| Random Forest | SMOTE | 0.401022 | 3,764.56 | 14,760.99 | 275,190.00 | 74.50 | 74.50 |
| XGBoost | Sem tratamento | 0.045252 | 3,774.46 | 14,760.99 | 275,190.00 | 74.43 | 74.43 |
| Random Forest | Sensível a custo (pesos) | 0.214105 | 3,774.56 | 14,760.99 | 275,190.00 | 74.43 | 74.43 |
| LightGBM | Subamostragem aleatória | 0.015989 | 3,774.56 | 14,760.99 | 275,190.00 | 74.43 | 74.43 |
| Random Forest | Sem tratamento | 0.243561 | 3,789.46 | 14,760.99 | 275,190.00 | 74.33 | 74.33 |
| MLP (rede neural) | SMOTE | 0.415660 | 3,794.56 | 14,760.99 | 275,190.00 | 74.29 | 74.29 |
| Random Forest | Subamostragem aleatória | 0.435083 | 3,799.46 | 14,760.99 | 275,190.00 | 74.26 | 74.26 |
| MLP (rede neural) | Sem tratamento | 0.147269 | 3,839.56 | 14,760.99 | 275,190.00 | 73.99 | 73.99 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.121918 | 3,844.56 | 14,760.99 | 275,190.00 | 73.95 | 73.95 |
| LightGBM | Sensível a custo (pesos) | 0.001780 | 3,919.56 | 14,760.99 | 275,190.00 | 73.45 | 73.45 |
| Regressão Logística (referência) | SMOTE | 0.595964 | 4,002.42 | 14,760.99 | 275,190.00 | 72.89 | 72.89 |
| MLP (rede neural) | Subamostragem aleatória | 0.318549 | 4,117.42 | 14,760.99 | 275,190.00 | 72.11 | 72.11 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.999876 | 4,147.41 | 14,760.99 | 275,190.00 | 71.90 | 71.90 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.356701 | 7,677.69 | 14,760.99 | 275,190.00 | 47.99 | 47.99 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.828% e revocação 0.
