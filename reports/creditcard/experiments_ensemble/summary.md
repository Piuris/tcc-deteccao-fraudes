# Resultados — ulb_creditcard

- Transações: 275.663 | fraudes: 473 (0.1716%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ensemble XGBoost + LightGBM | Melhor de cada membro | 0.8604 ± 0.0229 | 0.8466 | [0.777, 0.906] | 0.9805 | 0.7670 | 0.8316 | 0.7980 | 0.7983 | 24 | 16 | 81.89 | 5.87 | 2.90 | 3.02 |
| Ensemble XGBoost + LightGBM + RF | Melhor de cada membro | 0.8545 ± 0.0239 | 0.8343 | [0.763, 0.897] | 0.9812 | 0.7091 | 0.8211 | 0.7610 | 0.7626 | 32 | 17 | 80.42 | 46.40 | 17.69 | 18.52 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| Ensemble XGBoost + LightGBM | Melhor de cada membro | 0.077006 | 3,744.56 | 14,760.99 | 275,190.00 | 74.63 | 74.63 |
| Ensemble XGBoost + LightGBM + RF | Melhor de cada membro | 0.185011 | 3,749.56 | 14,760.99 | 275,190.00 | 74.60 | 74.60 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.828% e revocação 0.
