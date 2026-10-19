# Resultados — ulb_creditcard

- Transações: 284.807 | fraudes: 492 (0.1727%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Sensível a custo (pesos) | 0.8485 ± 0.0409 | 0.8846 | [0.823, 0.940] | 0.9793 | 0.7522 | 0.8673 | 0.8057 | 0.8074 | 28 | 13 | 85.31 | 3.12 | 2.12 | 2.28 |
| LightGBM | SMOTE | 0.8568 ± 0.0435 | 0.8824 | [0.823, 0.941] | 0.9855 | 0.7107 | 0.8776 | 0.7854 | 0.7894 | 35 | 12 | 85.97 | 3.65 | 2.26 | 2.42 |
| LightGBM | Sem tratamento | 0.8511 ± 0.0453 | 0.8784 | [0.817, 0.934] | 0.9811 | 0.7611 | 0.8776 | 0.8152 | 0.8169 | 27 | 12 | 86.38 | 3.67 | 2.26 | 2.48 |
| Random Forest | SMOTE | 0.8515 ± 0.0393 | 0.8758 | [0.809, 0.932] | 0.9771 | 0.7350 | 0.8776 | 0.8000 | 0.8028 | 31 | 12 | 86.17 | 37.06 | 15.07 | 15.58 |
| XGBoost | SMOTE | 0.8562 ± 0.0377 | 0.8753 | [0.813, 0.932] | 0.9869 | 0.7456 | 0.8673 | 0.8019 | 0.8038 | 29 | 13 | 85.26 | 3.36 | 2.13 | 2.24 |
| Random Forest | Sem tratamento | 0.8383 ± 0.0494 | 0.8746 | [0.809, 0.937] | 0.9752 | 0.7544 | 0.8776 | 0.8113 | 0.8133 | 28 | 12 | 86.33 | 96.00 | 14.97 | 15.44 |
| XGBoost | Sem tratamento | 0.8507 ± 0.0395 | 0.8725 | [0.807, 0.929] | 0.9808 | 0.8000 | 0.8571 | 0.8276 | 0.8278 | 21 | 14 | 84.64 | 2.73 | 2.15 | 2.32 |
| MLP (rede neural) | Sem tratamento | 0.8370 ± 0.0392 | 0.8679 | [0.798, 0.923] | 0.9758 | 0.6418 | 0.8776 | 0.7414 | 0.7500 | 48 | 12 | 85.31 | 10.45 | 1.55 | 1.64 |
| LightGBM | Subamostragem aleatória | 0.8294 ± 0.0392 | 0.8639 | [0.797, 0.921] | 0.9768 | 0.5811 | 0.8776 | 0.6992 | 0.7135 | 62 | 12 | 84.59 | 1.44 | 2.25 | 2.45 |
| XGBoost | Subamostragem aleatória | 0.8345 ± 0.0322 | 0.8552 | [0.784, 0.912] | 0.9812 | 0.6296 | 0.8673 | 0.7296 | 0.7385 | 50 | 13 | 84.18 | 1.43 | 2.12 | 2.36 |
| Random Forest | Sensível a custo (pesos) | 0.8377 ± 0.0383 | 0.8549 | [0.786, 0.919] | 0.9614 | 0.6187 | 0.8776 | 0.7257 | 0.7363 | 53 | 12 | 85.05 | 18.00 | 14.59 | 15.02 |
| LightGBM | Sensível a custo (pesos) | 0.8375 ± 0.0380 | 0.8444 | [0.771, 0.905] | 0.9569 | 0.6721 | 0.8367 | 0.7455 | 0.7495 | 40 | 16 | 81.63 | 3.70 | 2.28 | 2.55 |
| MLP (rede neural) | SMOTE | 0.8234 ± 0.0364 | 0.8287 | [0.752, 0.891] | 0.9741 | 0.5793 | 0.8571 | 0.6914 | 0.7041 | 61 | 14 | 82.60 | 16.98 | 1.54 | 1.60 |
| Random Forest | Subamostragem aleatória | 0.7921 ± 0.0429 | 0.8245 | [0.740, 0.901] | 0.9742 | 0.7167 | 0.8776 | 0.7890 | 0.7927 | 34 | 12 | 86.02 | 12.99 | 14.68 | 15.19 |
| MLP (rede neural) | Sensível a custo (pesos) | 0.8246 ± 0.0333 | 0.8236 | [0.748, 0.888] | 0.9752 | 0.4830 | 0.8673 | 0.6204 | 0.6465 | 91 | 13 | 82.09 | 8.84 | 1.54 | 1.62 |
| Regressão Logística (referência) | Subamostragem aleatória | 0.7642 ± 0.0378 | 0.7453 | [0.656, 0.834] | 0.9694 | 0.6148 | 0.8469 | 0.7124 | 0.7211 | 52 | 15 | 82.04 | 0.96 | 1.57 | 1.65 |
| Regressão Logística (referência) | Sem tratamento | 0.7631 ± 0.0400 | 0.7418 | [0.660, 0.824] | 0.9686 | 0.6159 | 0.8673 | 0.7203 | 0.7304 | 53 | 13 | 84.03 | 1.00 | 1.54 | 1.61 |
| Regressão Logística (referência) | SMOTE | 0.7614 ± 0.0383 | 0.7416 | [0.652, 0.828] | 0.9693 | 0.6159 | 0.8673 | 0.7203 | 0.7304 | 53 | 13 | 84.03 | 1.19 | 1.66 | 1.75 |
| Regressão Logística (referência) | Sensível a custo (pesos) | 0.7476 ± 0.0386 | 0.7086 | [0.614, 0.804] | 0.9714 | 0.5183 | 0.8673 | 0.6489 | 0.6698 | 79 | 13 | 82.70 | 1.20 | 1.54 | 1.62 |
| MLP (rede neural) | Subamostragem aleatória | 0.7861 ± 0.0703 | 0.6938 | [0.596, 0.792] | 0.9454 | 0.7843 | 0.8163 | 0.8000 | 0.7998 | 22 | 18 | 80.51 | 1.90 | 1.55 | 1.63 |
| Isolation Forest (não supervisionado) | Sem tratamento | 0.2944 ± 0.0548 | 0.3298 | [0.239, 0.444] | 0.9574 | 0.1494 | 0.7041 | 0.2464 | 0.3221 | 393 | 29 | 50.36 | 5.70 | 3.86 | 3.96 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| Regressão Logística (referência) | 0.1732 | 0.00075 | 0.00062 |
| Random Forest | 0.1732 | 0.00068 | 0.00050 |
| XGBoost | 0.1732 | 0.00056 | 0.00046 |
| LightGBM | 0.1732 | 0.00057 | 0.00053 |
| MLP (rede neural) | 0.1732 | 0.00065 | 0.00063 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.827% e revocação 0.
