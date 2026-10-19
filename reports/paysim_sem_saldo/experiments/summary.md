# Resultados — paysim_sem_saldo[20%]

- Transações: 554.082 | fraudes: 1.643 (0.2965%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Sem tratamento | 0.7681 ± 0.0115 | 0.8062 | [0.764, 0.847] | 0.9529 | 0.7108 | 0.7994 | 0.7525 | 0.7530 | 107 | 66 | 78.31 | 3.95 | 3.65 | 4.13 |
| MLP (rede neural) | Sem tratamento | 0.7629 ± 0.0111 | 0.8055 | [0.764, 0.847] | 0.9560 | 0.6100 | 0.8176 | 0.6987 | 0.7052 | 172 | 60 | 79.15 | 10.87 | 2.74 | 2.85 |
| MLP (rede neural) | Sensível a custo (pesos) | 0.7567 ± 0.0107 | 0.8050 | [0.765, 0.848] | 0.9514 | 0.6186 | 0.8085 | 0.7009 | 0.7062 | 164 | 63 | 78.36 | 8.27 | 2.77 | 3.14 |
| MLP (rede neural) | SMOTE | 0.7600 ± 0.0127 | 0.8020 | [0.760, 0.843] | 0.9503 | 0.6551 | 0.8024 | 0.7213 | 0.7241 | 139 | 65 | 78.13 | 25.34 | 2.74 | 2.81 |
| Random Forest | Sem tratamento | 0.7593 ± 0.0125 | 0.8018 | [0.760, 0.846] | 0.9351 | 0.6909 | 0.8085 | 0.7451 | 0.7466 | 119 | 63 | 79.04 | 22.29 | 16.34 | 16.88 |
| XGBoost | SMOTE | 0.7604 ± 0.0127 | 0.8017 | [0.759, 0.844] | 0.9473 | 0.6735 | 0.7964 | 0.7298 | 0.7315 | 127 | 67 | 77.71 | 4.21 | 3.64 | 4.13 |
| XGBoost | Sensível a custo (pesos) | 0.7599 ± 0.0122 | 0.8010 | [0.759, 0.842] | 0.9516 | 0.6253 | 0.7964 | 0.7005 | 0.7047 | 157 | 67 | 77.25 | 3.68 | 3.52 | 3.91 |
| XGBoost | Subamostragem aleatória | 0.7603 ± 0.0132 | 0.8005 | [0.758, 0.841] | 0.9517 | 0.6527 | 0.8055 | 0.7211 | 0.7242 | 141 | 64 | 78.40 | 1.25 | 3.52 | 3.78 |
| Random Forest | SMOTE | 0.7607 ± 0.0124 | 0.8000 | [0.757, 0.844] | 0.9473 | 0.7414 | 0.7842 | 0.7622 | 0.7618 | 90 | 71 | 77.05 | 29.82 | 16.61 | 17.31 |
| MLP (rede neural) | Subamostragem aleatória | 0.7603 ± 0.0158 | 0.7999 | [0.761, 0.841] | 0.9515 | 0.8591 | 0.7599 | 0.8065 | 0.8074 | 41 | 79 | 75.36 | 4.26 | 2.80 | 3.20 |
| Random Forest | Subamostragem aleatória | 0.7533 ± 0.0130 | 0.7971 | [0.752, 0.839] | 0.9440 | 0.7049 | 0.7842 | 0.7424 | 0.7427 | 108 | 71 | 76.78 | 6.11 | 16.54 | 17.28 |
| LightGBM | Sem tratamento | 0.7578 ± 0.0128 | 0.7922 | [0.751, 0.834] | 0.9475 | 0.6855 | 0.7751 | 0.7275 | 0.7281 | 117 | 74 | 75.73 | 2.48 | 3.58 | 3.82 |
| Random Forest | Sensível a custo (pesos) | 0.7537 ± 0.0135 | 0.7917 | [0.748, 0.834] | 0.9380 | 0.5742 | 0.7994 | 0.6684 | 0.6764 | 195 | 66 | 76.98 | 23.43 | 16.90 | 17.82 |
| LightGBM | SMOTE | 0.7533 ± 0.0117 | 0.7908 | [0.747, 0.833] | 0.9511 | 0.5959 | 0.7933 | 0.6806 | 0.6865 | 177 | 68 | 76.64 | 1.89 | 3.55 | 3.67 |
| LightGBM | Subamostragem aleatória | 0.7452 ± 0.0192 | 0.7836 | [0.739, 0.826] | 0.9472 | 0.6523 | 0.7812 | 0.7109 | 0.7129 | 137 | 72 | 76.03 | 1.23 | 3.57 | 3.70 |
| LightGBM | Sensível a custo (pesos) | 0.7338 ± 0.0147 | 0.7641 | [0.720, 0.808] | 0.9450 | 0.6596 | 0.7599 | 0.7062 | 0.7071 | 129 | 79 | 74.03 | 3.13 | 3.61 | 3.89 |
| Regressão Logística (referência) | Sem tratamento | 0.5841 ± 0.0305 | 0.6076 | [0.556, 0.658] | 0.9213 | 0.4966 | 0.6717 | 0.5711 | 0.5761 | 224 | 108 | 63.77 | 1.16 | 2.84 | 2.94 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.5756 ± 0.0338 | 0.5963 | [0.544, 0.648] | 0.9260 | 0.4629 | 0.7021 | 0.5580 | 0.5686 | 268 | 98 | 66.14 | 1.04 | 2.76 | 2.95 |
| Regressão Logística (referência) | SMOTE | 0.5319 ± 0.0399 | 0.5412 | [0.487, 0.598] | 0.9326 | 0.5213 | 0.7082 | 0.6005 | 0.6062 | 214 | 96 | 67.57 | 1.13 | 2.72 | 2.83 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.5095 ± 0.0333 | 0.5328 | [0.479, 0.589] | 0.8787 | 0.9548 | 0.5137 | 0.6680 | 0.6997 | 8 | 160 | 51.25 | 3.14 | 3.54 | 3.67 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.4565 ± 0.0432 | 0.4582 | [0.404, 0.516] | 0.9329 | 0.4828 | 0.6809 | 0.5649 | 0.5718 | 240 | 105 | 64.44 | 1.51 | 2.74 | 2.82 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| Regressão Logística (referência) | 0.2973 | 0.00179 | 0.00181 |
| Random Forest | 0.2973 | 0.00096 | 0.00102 |
| XGBoost | 0.0595 | 0.00174 | 0.00093 |
| LightGBM | 0.0595 | 0.00215 | 0.00101 |
| MLP (rede neural) | 0.2973 | 0.00088 | 0.00095 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| MLP (rede neural) | Sensível a custo (pesos) | 0.001426 | 454,090.00 | 475,453,302.21 | 552,440.00 | 99.90 | 17.80 |
| MLP (rede neural) | SMOTE | 0.000005 | 460,560.00 | 475,453,302.21 | 552,440.00 | 99.90 | 16.63 |
| Random Forest | SMOTE | 0.001261 | 463,905.00 | 475,453,302.21 | 552,440.00 | 99.90 | 16.03 |
| Random Forest | Subamostragem aleatória | 0.000217 | 479,750.00 | 475,453,302.21 | 552,440.00 | 99.90 | 13.16 |
| XGBoost | SMOTE | 0.000249 | 483,895.00 | 475,453,302.21 | 552,440.00 | 99.90 | 12.41 |
| LightGBM | Subamostragem aleatória | 0.000026 | 490,510.00 | 475,453,302.21 | 552,440.00 | 99.90 | 11.21 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.026197 | 492,470.00 | 475,453,302.21 | 552,440.00 | 99.90 | 10.86 |
| MLP (rede neural) | Subamostragem aleatória | 0.000004 | 493,120.00 | 475,453,302.21 | 552,440.00 | 99.90 | 10.74 |
| XGBoost | Sensível a custo (pesos) | 0.001740 | 495,145.00 | 475,453,302.21 | 552,440.00 | 99.90 | 10.37 |
| LightGBM | Sem tratamento | 0.000006 | 506,925.00 | 475,453,302.21 | 552,440.00 | 99.89 | 8.24 |
| Regressão Logística (referência) | SMOTE | 0.000655 | 507,011.90 | 475,453,302.21 | 552,440.00 | 99.89 | 8.22 |
| MLP (rede neural) | Sem tratamento | 0.000002 | 511,220.00 | 475,453,302.21 | 552,440.00 | 99.89 | 7.46 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.000245 | 516,397.74 | 475,453,302.21 | 552,440.00 | 99.89 | 6.52 |
| LightGBM | SMOTE | 0.002154 | 522,430.00 | 475,453,302.21 | 552,440.00 | 99.89 | 5.43 |
| Regressão Logística (referência) | Sem tratamento | 0.000039 | 535,276.90 | 475,453,302.21 | 552,440.00 | 99.89 | 3.11 |
| LightGBM | Sensível a custo (pesos) | 0.000005 | 548,340.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.74 |
| Random Forest | Sem tratamento | 0.000000 | 552,440.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| Random Forest | Sensível a custo (pesos) | 0.000000 | 552,440.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| XGBoost | Subamostragem aleatória | 0.001188 | 668,555.67 | 475,453,302.21 | 552,440.00 | 99.86 | -21.02 |
| XGBoost | Sem tratamento | 0.000092 | 675,490.67 | 475,453,302.21 | 552,440.00 | 99.86 | -22.27 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.010274 | 798,499.49 | 475,453,302.21 | 552,440.00 | 99.83 | -44.54 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.704% e revocação 0.
