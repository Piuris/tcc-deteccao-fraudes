# Resultados — ulb_creditcard

- Transações: 275.663 | fraudes: 473 (0.1716%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=50, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LightGBM | SMOTE | 0.8584 ± 0.0224 | 0.8441 | [0.778, 0.908] | 0.9797 | 0.7547 | 0.8421 | 0.7960 | 0.7968 | 26 | 15 | 82.84 | 2.83 | 2.30 | 2.63 |
| XGBoost | SMOTE | 0.8548 ± 0.0243 | 0.8403 | [0.773, 0.903] | 0.9810 | 0.8444 | 0.8000 | 0.8216 | 0.8216 | 14 | 19 | 79.26 | 3.06 | 2.05 | 2.13 |
| XGBoost | Sensível a custo (pesos) | 0.8601 ± 0.0235 | 0.8393 | [0.765, 0.901] | 0.9804 | 0.7670 | 0.8316 | 0.7980 | 0.7983 | 24 | 16 | 81.89 | 2.54 | 2.05 | 2.14 |
| XGBoost | Sem tratamento | 0.8576 ± 0.0241 | 0.8382 | [0.772, 0.903] | 0.9681 | 0.7835 | 0.8000 | 0.7917 | 0.7913 | 21 | 19 | 78.89 | 2.09 | 2.02 | 2.09 |
| XGBoost | Subamostragem aleatória | 0.8517 ± 0.0254 | 0.8326 | [0.762, 0.898] | 0.9782 | 0.7624 | 0.8105 | 0.7857 | 0.7857 | 24 | 18 | 79.79 | 1.36 | 2.04 | 2.18 |
| LightGBM | Sem tratamento | 0.8563 ± 0.0279 | 0.8294 | [0.754, 0.895] | 0.9738 | 0.7723 | 0.8211 | 0.7959 | 0.7959 | 23 | 17 | 80.89 | 3.97 | 2.28 | 2.48 |
| LightGBM | Subamostragem aleatória | 0.8572 ± 0.0245 | 0.8266 | [0.748, 0.895] | 0.9860 | 0.7333 | 0.8105 | 0.7700 | 0.7706 | 28 | 18 | 79.58 | 1.55 | 2.29 | 2.55 |
| LightGBM | Sensível a custo (pesos) | 0.8430 ± 0.0228 | 0.8248 | [0.750, 0.892] | 0.9305 | 0.6696 | 0.8105 | 0.7333 | 0.7362 | 38 | 18 | 79.05 | 5.15 | 2.38 | 2.67 |

## Calibração após subamostragem (Dal Pozzolo et al., 2015)

| modelo | β | Brier bruto | Brier corrigido |
|---|---|---|---|
| XGBoost | 0.1717 | 0.00063 | 0.00055 |
| LightGBM | 0.1717 | 0.00066 | 0.00065 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| XGBoost | Sensível a custo (pesos) | 0.147239 | 3,739.56 | 14,760.99 | 275,190.00 | 74.67 | 74.67 |
| LightGBM | SMOTE | 0.000622 | 3,739.56 | 14,760.99 | 275,190.00 | 74.67 | 74.67 |
| XGBoost | SMOTE | 0.224067 | 3,749.56 | 14,760.99 | 275,190.00 | 74.60 | 74.60 |
| LightGBM | Sem tratamento | 0.000216 | 3,759.46 | 14,760.99 | 275,190.00 | 74.53 | 74.53 |
| XGBoost | Sem tratamento | 0.018013 | 3,769.56 | 14,760.99 | 275,190.00 | 74.46 | 74.46 |
| LightGBM | Subamostragem aleatória | 0.293036 | 3,774.56 | 14,760.99 | 275,190.00 | 74.43 | 74.43 |
| XGBoost | Subamostragem aleatória | 0.107186 | 3,784.56 | 14,760.99 | 275,190.00 | 74.36 | 74.36 |
| LightGBM | Sensível a custo (pesos) | 0.001780 | 3,919.56 | 14,760.99 | 275,190.00 | 73.45 | 73.45 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.828% e revocação 0.
