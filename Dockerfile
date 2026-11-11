FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 app
WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

COPY --chown=app pyproject.toml ./
COPY --chown=app src ./src
COPY --chown=app artifacts ./artifacts
RUN pip install --no-cache-dir --no-deps .

USER app
ENV FRAUDE_ARTIFACTS_DIR=/app/artifacts \
    MPLCONFIGDIR=/tmp/matplotlib \
    PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn fraude_api.main:app --host 0.0.0.0 --port ${PORT}"]
