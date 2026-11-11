# Inicia a API de detecção de fraudes no Windows, sem Docker.
# Uso (PowerShell, na pasta do projeto):  powershell -ExecutionPolicy Bypass -File .\iniciar.ps1
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    Write-Host "Python não encontrado. Instale o Python 3.12 em https://www.python.org/downloads/ e tente de novo." -ForegroundColor Red
    exit 1
}
& py -3.12 --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "É necessário o Python 3.12 (https://www.python.org/downloads/)." -ForegroundColor Red
    exit 1
}

$missing = @("creditcard", "paysim") | Where-Object { -not (Test-Path "artifacts\model_$_.joblib") }
if ($missing) {
    Write-Host "Modelos ausentes em artifacts\: $($missing -join ', '). Baixe o repositório completo novamente." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path ".venv-api\Scripts\python.exe")) {
    Write-Host "Criando ambiente e instalando dependências (só na primeira vez, alguns minutos)..."
    & py -3.12 -m venv .venv-api
    & .\.venv-api\Scripts\python.exe -m pip install --upgrade pip --quiet
    & .\.venv-api\Scripts\python.exe -m pip install -r requirements-api.txt --quiet
    & .\.venv-api\Scripts\python.exe -m pip install -e . --no-deps --quiet
}

Write-Host "API em http://localhost:8000/docs  (Ctrl+C para encerrar)" -ForegroundColor Green
Start-Job { Start-Sleep 8; Start-Process "http://localhost:8000/docs" } | Out-Null
& .\.venv-api\Scripts\python.exe -m uvicorn fraude_api.main:app --port 8000
