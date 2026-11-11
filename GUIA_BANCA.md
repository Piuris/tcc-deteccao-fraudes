# Guia de acesso para a banca

**TCC:** Sistema de Detecção de Fraudes em Transações Financeiras com Machine Learning
**Autor:** João Vitor Pires · TADS, IFRS Campus Canoas · Orientador: Prof. Dr. Rafael Coimbra Pinto

A aplicação é uma API REST que recebe uma transação e devolve:
- a probabilidade de fraude;
- a decisão (aprovar ou bloquear);
- os cinco atributos que mais pesaram na decisão, calculados com SHAP.

Ela traz dois modelos: o da base de cartões ULB, que é o modelo principal do trabalho, e o do simulador PaySim. Os testes são feitos pelo navegador, na página interativa da API.

---

## Opção 1: acesso online (recomendado, sem instalar nada)

1. Abra **https://tcc-deteccao-fraudes.onrender.com/docs**.
2. Se a página demorar a carregar, aguarde cerca de 1 minuto. O servidor gratuito (Render) hiberna depois de 15 minutos sem uso e acorda no primeiro acesso. Depois disso, as respostas são imediatas.

Depois siga o [roteiro de testes](#roteiro-de-testes).

## Opção 2: executar no próprio computador com Docker

Requer o [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```
git clone https://github.com/Piuris/tcc-deteccao-fraudes.git
cd tcc-deteccao-fraudes
```

Os modelos treinados já vêm no repositório, na pasta `artifacts/`. Depois rode:

```
docker build -t tcc-fraudes .
docker run -p 8000:8000 tcc-fraudes
```

Abra **http://localhost:8000/docs**.

## Opção 3: executar no Windows sem Docker

Requer o [Python 3.12](https://www.python.org/downloads/). Na instalação, marque *Add python.exe to PATH*.

1. Baixe o código (botão *Code → Download ZIP* no GitHub, ou `git clone`). Os modelos treinados já vêm na pasta `artifacts/`.
2. Na pasta do projeto, execute no PowerShell:

```
powershell -ExecutionPolicy Bypass -File .\iniciar.ps1
```

Na primeira execução, o script instala as dependências, o que leva alguns minutos. Depois o navegador abre sozinho em **http://localhost:8000/docs**. Para encerrar, use Ctrl+C.

---

## Roteiro de testes

Na página `/docs`, cada rota tem um botão **Try it out**. As rotas de predição já trazem **transações reais do conjunto de teste**. Esses exemplos não foram usados no treino do modelo. Escolha um exemplo na lista **Examples**, clique em **Execute** e veja a resposta logo abaixo.

### 1. Verificar se a API está no ar

`GET /health` → `"status": "ok"` e `"models_loaded": ["creditcard", "paysim"]`.

### 2. Modelo principal: cartões de crédito (ULB)

`POST /v1/creditcard/predict`:

| Exemplo | O que é | Probabilidade esperada | Decisão esperada |
|---|---|---|---|
| Fraude detectada | fraude real (verdadeiro positivo) | ≈ 0,99 | `bloquear` |
| Transação legítima | compra legítima (verdadeiro negativo) | ≈ 0,0001 | `aprovar` |
| Falso alarme | compra legítima bloqueada (falso positivo) | ≈ 0,33 | `bloquear` |
| Fraude não detectada | fraude que passa (falso negativo) | ≈ 0,0009 | `aprovar` |

Os dois últimos casos estão aí de propósito. Eles mostram os erros que o modelo comete e que foram discutidos no Capítulo 4.

O limiar de bloqueio é **0,0345**. Ele foi escolhido pela função de custo do cenário moderado (seção 4.8). Por isso, uma probabilidade de 0,33 já leva ao bloqueio.

Como ler a resposta:
- `fraud_probability`: probabilidade calibrada de fraude.
- `threshold` e `decision`: o limiar aplicado e a decisão resultante.
- `top_factors`: os cinco atributos que mais pesaram, com o valor SHAP de cada um. Um valor positivo aumenta o risco.
- `latency_ms`: tempo de processamento no servidor.

Na ULB, os atributos V1 a V28 são anonimizados. A explicação mostra o que o modelo usou, mas não tem significado de negócio (seção 4.9).

### 3. Modelo PaySim (atributos interpretáveis)

`POST /v1/paysim/predict`, com os exemplos *Fraude detectada*, *Transação legítima* e *Fraude não detectada*.

Os campos são intuitivos:
- tipo da operação (`TRANSFER` ou `CASH_OUT`);
- valor;
- saldos antes e depois.

Este modelo usa todos os atributos, inclusive os saldos da origem. Por isso ele explora o atalho do simulador descrito na seção 4.4: a transferência que esvazia exatamente o saldo da origem. Os principais fatores da explicação (`error_balance_orig_log`, `orig_emptied`) mostram isso diretamente. As probabilidades ficam quase sempre em 0 ou 1, e o limiar escolhido pela função de custo é 1,0.

### 4. Outras rotas

- `GET /v1/models`: metadados dos modelos (algoritmo, hiperparâmetros, limiar, métricas no teste e versões das bibliotecas).
- `POST /v1/.../predict/batch`: várias transações em uma única requisição. O exemplo *Todos os casos* envia os casos acima juntos.
- **Validação de entrada:** tente apagar um campo obrigatório ou informar um valor negativo. A API recusa com **HTTP 422** e indica o campo com problema.

---

## Código-fonte e reprodução dos experimentos

O código está em https://github.com/Piuris/tcc-deteccao-fraudes. O `README.md` explica como reproduzir os experimentos do zero. Isso exige baixar as bases e algumas horas de processamento. Os testes automatizados (89) rodam com `pytest`.

**Contato:** João Vitor Pires · <EMAIL_DO_AUTOR>
