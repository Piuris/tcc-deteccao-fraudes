# Resultados — paysim[20%]

- Transações: 554.082 | fraudes: 1.643 (0.2965%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Random Forest | SMOTE | 0.9956 ± 0.0022 | 0.9930 | [0.983, 1.000] | 0.9975 | 0.9878 | 0.9848 | 0.9863 | 0.9863 | 4 | 5 | 98.42 | 37.63 | 16.62 | 17.05 |
| Random Forest | Sensível a custo (pesos) | 0.9957 ± 0.0023 | 0.9925 | [0.983, 0.999] | 0.9972 | 1.0000 | 0.9878 | 0.9939 | 0.9939 | 0 | 4 | 98.78 | 38.08 | 16.71 | 17.10 |
| MLP (rede neural) | SMOTE | 0.9938 ± 0.0030 | 0.9922 | [0.982, 0.999] | 0.9981 | 0.9446 | 0.9848 | 0.9643 | 0.9644 | 19 | 5 | 98.19 | 6.84 | 3.39 | 3.62 |
| Random Forest | Subamostragem aleatória | 0.9954 ± 0.0020 | 0.9921 | [0.982, 1.000] | 0.9967 | 0.9939 | 0.9848 | 0.9893 | 0.9893 | 2 | 5 | 98.45 | 1.80 | 16.72 | 17.13 |
| LightGBM | Subamostragem aleatória | 0.9950 ± 0.0023 | 0.9920 | [0.982, 0.999] | 0.9952 | 1.0000 | 0.9878 | 0.9939 | 0.9939 | 0 | 4 | 98.78 | 1.65 | 4.52 | 4.54 |
| MLP (rede neural) | Sensível a custo (pesos) | 0.9937 ± 0.0022 | 0.9910 | [0.980, 0.999] | 0.9980 | 0.9643 | 0.9848 | 0.9744 | 0.9744 | 12 | 5 | 98.30 | 6.54 | 3.38 | 3.51 |
| XGBoost | SMOTE | 0.9949 ± 0.0023 | 0.9910 | [0.980, 1.000] | 0.9968 | 0.9615 | 0.9878 | 0.9745 | 0.9745 | 13 | 4 | 98.59 | 5.84 | 4.35 | 4.37 |
| LightGBM | SMOTE | 0.9949 ± 0.0019 | 0.9909 | [0.979, 1.000] | 0.9950 | 1.0000 | 0.9878 | 0.9939 | 0.9939 | 0 | 4 | 98.78 | 3.33 | 4.41 | 4.65 |
| XGBoost | Subamostragem aleatória | 0.9953 ± 0.0020 | 0.9904 | [0.979, 0.999] | 0.9956 | 0.9503 | 0.9878 | 0.9687 | 0.9688 | 17 | 4 | 98.53 | 1.54 | 4.24 | 4.39 |
| MLP (rede neural) | Sem tratamento | 0.9921 ± 0.0047 | 0.9904 | [0.980, 0.998] | 0.9990 | 0.9969 | 0.9787 | 0.9877 | 0.9877 | 1 | 7 | 97.86 | 11.54 | 3.39 | 3.56 |
| LightGBM | Sem tratamento | 0.9954 ± 0.0020 | 0.9896 | [0.978, 0.998] | 0.9949 | 0.9969 | 0.9848 | 0.9908 | 0.9908 | 1 | 5 | 98.47 | 1.85 | 4.37 | 4.51 |
| XGBoost | Sem tratamento | 0.9951 ± 0.0018 | 0.9893 | [0.978, 0.998] | 0.9953 | 0.9819 | 0.9878 | 0.9848 | 0.9848 | 6 | 4 | 98.69 | 3.65 | 4.22 | 4.38 |
| XGBoost | Sensível a custo (pesos) | 0.9953 ± 0.0020 | 0.9891 | [0.977, 0.998] | 0.9951 | 0.9969 | 0.9878 | 0.9924 | 0.9924 | 1 | 4 | 98.77 | 4.07 | 4.25 | 4.44 |
| Random Forest | Sem tratamento | 0.9942 ± 0.0016 | 0.9889 | [0.977, 0.997] | 0.9955 | 0.9878 | 0.9878 | 0.9878 | 0.9878 | 4 | 4 | 98.72 | 17.60 | 16.71 | 17.12 |
| LightGBM | Sensível a custo (pesos) | 0.9943 ± 0.0018 | 0.9888 | [0.976, 0.997] | 0.9952 | 1.0000 | 0.9878 | 0.9939 | 0.9939 | 0 | 4 | 98.78 | 4.20 | 4.40 | 4.57 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.9897 ± 0.0020 | 0.9857 | [0.972, 0.996] | 0.9968 | 0.9729 | 0.9818 | 0.9773 | 0.9772 | 9 | 6 | 98.04 | 1.28 | 3.36 | 3.46 |
| MLP (rede neural) | Subamostragem aleatória | 0.9902 ± 0.0033 | 0.9849 | [0.971, 0.996] | 0.9983 | 0.9847 | 0.9787 | 0.9817 | 0.9817 | 5 | 7 | 97.80 | 5.12 | 3.39 | 3.56 |
| Regressão Logística (referência) | SMOTE | 0.9897 ± 0.0020 | 0.9843 | [0.971, 0.994] | 0.9978 | 0.9390 | 0.9818 | 0.9599 | 0.9600 | 21 | 6 | 97.86 | 1.80 | 3.36 | 3.50 |
| Regressão Logística (referência) | Sem tratamento | 0.9880 ± 0.0028 | 0.9818 | [0.966, 0.994] | 0.9908 | 0.9877 | 0.9757 | 0.9817 | 0.9816 | 4 | 8 | 97.51 | 1.64 | 3.45 | 3.47 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.8996 ± 0.0444 | 0.8769 | [0.847, 0.903] | 0.9969 | 0.8075 | 0.9818 | 0.8861 | 0.8900 | 77 | 6 | 97.01 | 1.85 | 3.37 | 3.55 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.5527 ± 0.0232 | 0.5706 | [0.518, 0.625] | 0.9809 | 0.8995 | 0.5167 | 0.6564 | 0.6811 | 19 | 159 | 51.38 | 3.54 | 4.10 | 4.23 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| Regressão Logística (referência) | 0.0595 | 0.00024 | 0.00013 |
| Random Forest | 0.0297 | 0.00018 | 0.00007 |
| XGBoost | 0.0595 | 0.00009 | 0.00005 |
| LightGBM | 0.0595 | 0.00012 | 0.00006 |
| MLP (rede neural) | 0.2973 | 0.00008 | 0.00008 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| MLP (rede neural) | Subamostragem aleatória | 0.000042 | 167,235.00 | 475,453,302.21 | 552,440.00 | 99.96 | 69.73 |
| MLP (rede neural) | SMOTE | 0.000036 | 285,147.30 | 475,453,302.21 | 552,440.00 | 99.94 | 48.38 |
| LightGBM | Subamostragem aleatória | 0.000008 | 357,551.84 | 475,453,302.21 | 552,440.00 | 99.92 | 35.28 |
| Random Forest | Sensível a custo (pesos) | 0.009292 | 357,711.84 | 475,453,302.21 | 552,440.00 | 99.92 | 35.25 |
| Random Forest | Subamostragem aleatória | 0.060587 | 358,011.84 | 475,453,302.21 | 552,440.00 | 99.92 | 35.19 |
| Random Forest | Sem tratamento | 0.000065 | 450,916.84 | 475,453,302.21 | 552,440.00 | 99.91 | 18.38 |
| MLP (rede neural) | Sem tratamento | 0.000000 | 499,990.00 | 475,453,302.21 | 552,440.00 | 99.89 | 9.49 |
| XGBoost | Subamostragem aleatória | 0.009661 | 506,530.50 | 475,453,302.21 | 552,440.00 | 99.89 | 8.31 |
| MLP (rede neural) | Sensível a custo (pesos) | 0.119886 | 507,740.50 | 475,453,302.21 | 552,440.00 | 99.89 | 8.09 |
| Regressão Logística (referência) | Sem tratamento | 0.000000 | 552,430.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| Regressão Logística (referência) | SMOTE | 0.000000 | 552,440.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.000000 | 552,440.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.000027 | 552,440.00 | 475,453,302.21 | 552,440.00 | 99.88 | 0.00 |
| LightGBM | Sensível a custo (pesos) | 0.000000 | 570,761.84 | 475,453,302.21 | 552,440.00 | 99.88 | -3.32 |
| Random Forest | SMOTE | 0.061663 | 586,331.41 | 475,453,302.21 | 552,440.00 | 99.88 | -6.13 |
| XGBoost | SMOTE | 0.004382 | 588,516.41 | 475,453,302.21 | 552,440.00 | 99.88 | -6.53 |
| LightGBM | SMOTE | 0.000000 | 591,256.41 | 475,453,302.21 | 552,440.00 | 99.88 | -7.03 |
| LightGBM | Sem tratamento | 0.000031 | 736,285.07 | 475,453,302.21 | 552,440.00 | 99.85 | -33.28 |
| XGBoost | Sem tratamento | 0.000296 | 737,065.07 | 475,453,302.21 | 552,440.00 | 99.84 | -33.42 |
| XGBoost | Sensível a custo (pesos) | 0.002171 | 737,315.07 | 475,453,302.21 | 552,440.00 | 99.84 | -33.47 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.113316 | 766,103.20 | 475,453,302.21 | 552,440.00 | 99.84 | -38.68 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.704% e revocação 0.
