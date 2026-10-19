# Resultados — paysim_sem_saldo[20%]

- Transações: 554.082 | fraudes: 1.643 (0.2965%)
- Protocolo: CV estratificada k=5, busca aleatória n_iter=10, seleção por AUC-PR, semente=42
- Limiares escolhidos com predições *out-of-fold* do treino; teste usado uma única vez.

## Tabela comparativa (limiar de custo, cenário moderado FN:FP = 20:1)

| model | balancing | cv_auc_pr | auc_pr | auc_pr_ci95 | auc_roc | precision | recall | f1 | mcc | fp | fn | savings_pct | train_seconds | latency_mean_ms | latency_p95_ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ensemble XGBoost + LightGBM + RF | Melhor de cada membro | 0.7676 ± 0.0126 | 0.8082 | [0.766, 0.849] | 0.9482 | 0.7186 | 0.7994 | 0.7568 | 0.7572 | 103 | 66 | 78.37 | 28.41 | 21.09 | 28.44 |
| Ensemble XGBoost + LightGBM | Melhor de cada membro | 0.7681 ± 0.0118 | 0.8070 | [0.765, 0.848] | 0.9495 | 0.7070 | 0.7994 | 0.7504 | 0.7510 | 109 | 66 | 78.28 | 2.39 | 3.91 | 3.92 |

## Custo dependente do valor (FN = valor da fraude, piso 25; FP = 5)

Economia contra a melhor política trivial (a mais barata entre aprovar e bloquear tudo): quando o FN é muito mais caro que o FP, o limiar ótimo cai para perto de zero e "economia vs. aprovar tudo" engana.

| modelo | balanceamento | limiar | prejuízo | aprovar tudo | bloquear tudo | economia vs. aprovar tudo % | economia vs. melhor trivial % |
|---|---|---|---|---|---|---|---|
| Ensemble XGBoost + LightGBM + RF | Melhor de cada membro | 0.000731 | 462,020.00 | 475,453,302.21 | 552,440.00 | 99.90 | 16.37 |
| Ensemble XGBoost + LightGBM | Melhor de cada membro | 0.000212 | 468,530.00 | 475,453,302.21 | 552,440.00 | 99.90 | 15.19 |

## Acurácia é enganosa

Um classificador que aprova tudo teria acurácia de 99.704% e revocação 0.
