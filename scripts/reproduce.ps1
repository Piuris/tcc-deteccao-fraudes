# Reproduz todos os experimentos do TCC (Windows PowerShell).
# Uso: powershell -ExecutionPolicy Bypass -File scripts\reproduce.ps1
# A execução completa na base ULB leva de 7 a 9 horas.

$ErrorActionPreference = "Stop"
$py = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    py -3.12 -m venv .venv
    & $py -m pip install --upgrade pip
    & $py -m pip install -r requirements.txt
    & $py -m pip install -e .
}
$env:LOKY_MAX_CPU_COUNT = [Environment]::ProcessorCount

& $py -m pip freeze | Out-File -Encoding utf8 reports\environment.txt
& $py -m pytest
& $py -m fraude download --dataset creditcard
& $py -m fraude eda --dataset creditcard

# 1) Comparação principal: 6 algoritmos x 4 balanceamentos (21 configurações), n_iter=10.
& $py -m fraude experiment --dataset creditcard --n-iter 10 --no-resume
# 2) Busca ampliada (n_iter=50) para os algoritmos de boosting.
& $py -m fraude experiment --dataset creditcard --models xgboost lightgbm --n-iter 50 `
    --out-name experiments_busca50 --no-resume
# 3) Ensembles das melhores configurações de cada algoritmo de árvore.
& $py -m fraude ensemble --dataset creditcard --no-resume
# 4) CV repetida 5x3, Friedman/Nemenyi, t corrigido e seleção por parcimônia.
& $py -m fraude compare --dataset creditcard --repeats 3
# 5) Modelo final (calibrado), explicabilidade e drift.
& $py -m fraude train-final --dataset creditcard
& $py -m fraude explain --dataset creditcard
& $py -m fraude drift --dataset creditcard --windows 6 --label-delay 0
& $py -m fraude drift --dataset creditcard --windows 6 --label-delay 1

# PaySim (requer o CSV em data\paysim.csv ou a CLI do Kaggle configurada).
# Cenário sem os saldos da origem: fluxo completo (ver README, "Atalho do simulador").
if (Test-Path data\paysim.csv) {
    $s = @("--dataset", "paysim_sem_saldo", "--sample-frac", "0.2")
    & $py -m fraude eda @s
    & $py -m fraude experiment @s --n-iter 10 --no-resume
    & $py -m fraude experiment @s --models xgboost lightgbm --n-iter 50 --out-name experiments_busca50 --no-resume
    & $py -m fraude ensemble @s --no-resume
    & $py -m fraude compare @s --repeats 3
    & $py -m fraude train-final @s
    & $py -m fraude explain @s
    & $py -m fraude drift @s --windows 6 --label-delay 0
    & $py -m fraude drift @s --windows 6 --label-delay 1
    # Cenário completo (todos os modelos chegam a AUC-PR ~1,0; modelo servido pela API).
    $s = @("--dataset", "paysim", "--sample-frac", "0.2")
    & $py -m fraude eda @s
    & $py -m fraude experiment @s --n-iter 10 --no-resume
    & $py -m fraude train-final @s
    & $py -m fraude explain @s
    & $py -m fraude drift @s --windows 6
}
