# Resultados — paysim_sem_saldo[20%]

- Transações: 554.082 | fraudes: 1.643 (0.2965%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=50, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Sem tratamento | 0.7689 ± 0.0114 | 0.8094 | [0.768, 0.851] | 0.9540 | 0.6667 | 0.8085 | 0.7308 | 0.7333 | 133 | 63 | 78.83 | 1.99 | 3.47 | 3.60 |
| XGBoost | Subamostragem aleatória | 0.7673 ± 0.0112 | 0.8086 | [0.767, 0.850] | 0.9549 | 0.7458 | 0.8024 | 0.7731 | 0.7729 | 90 | 65 | 78.88 | 1.47 | 3.44 | 3.57 |
| XGBoost | SMOTE | 0.7615 ± 0.0124 | 0.8007 | [0.757, 0.842] | 0.9509 | 0.7222 | 0.7903 | 0.7547 | 0.7547 | 100 | 69 | 77.51 | 2.41 | 3.45 | 3.57 |
| LightGBM | Sem tratamento | 0.7626 ± 0.0097 | 0.8006 | [0.761, 0.842] | 0.9507 | 0.5923 | 0.7994 | 0.6805 | 0.6871 | 181 | 66 | 77.19 | 2.70 | 3.58 | 3.70 |
| LightGBM | Subamostragem aleatória | 0.7639 ± 0.0118 | 0.8006 | [0.757, 0.842] | 0.9474 | 0.6700 | 0.8085 | 0.7328 | 0.7352 | 131 | 63 | 78.86 | 1.25 | 3.58 | 3.67 |
| XGBoost | Sensível a custo (pesos) | 0.7605 ± 0.0136 | 0.7980 | [0.756, 0.840] | 0.9519 | 0.6359 | 0.7964 | 0.7072 | 0.7107 | 150 | 67 | 77.36 | 3.06 | 3.48 | 3.72 |
| LightGBM | SMOTE | 0.7564 ± 0.0138 | 0.7945 | [0.750, 0.836] | 0.9524 | 0.6927 | 0.7812 | 0.7343 | 0.7348 | 114 | 72 | 76.38 | 2.04 | 3.64 | 3.79 |
| LightGBM | Sensível a custo (pesos) | 0.7366 ± 0.0150 | 0.7625 | [0.719, 0.806] | 0.9451 | 0.6038 | 0.7781 | 0.6799 | 0.6844 | 168 | 73 | 75.26 | 2.79 | 3.66 | 4.10 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| XGBoost | 0.2973 | 0.00090 | 0.00087 |
| LightGBM | 0.2973 | 0.00092 | 0.00092 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| LightGBM | Subamostragem aleatória | 0.000255 | 475,490.00 | 475,453,302.21 | 552,440.00 | 99.90 | 13.93 |
| LightGBM | Sem tratamento | 0.000012 | 479,885.00 | 475,453,302.21 | 552,440.00 | 99.90 | 13.13 |
| XGBoost | Sensível a custo (pesos) | 0.008383 | 480,450.00 | 475,453,302.21 | 552,440.00 | 99.90 | 13.03 |
| XGBoost | SMOTE | 0.000138 | 495,390.00 | 475,453,302.21 | 552,440.00 | 99.90 | 10.33 |
| LightGBM | SMOTE | 0.000046 | 512,630.00 | 475,453,302.21 | 552,440.00 | 99.89 | 7.21 |
| LightGBM | Sensível a custo (pesos) | 0.000047 | 524,785.00 | 475,453,302.21 | 552,440.00 | 99.89 | 5.01 |
| XGBoost | Subamostragem aleatória | 0.000331 | 672,185.67 | 475,453,302.21 | 552,440.00 | 99.86 | -21.68 |
| XGBoost | Sem tratamento | 0.000115 | 675,680.67 | 475,453,302.21 | 552,440.00 | 99.86 | -22.31 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.704% e revocação 0.
