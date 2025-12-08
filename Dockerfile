# Builder stage
FROM python:3.12-slim AS builder
RUN pip install pdm
WORKDIR /app
COPY pyproject.toml pdm.lock
RUN --mount=type=cache,target=/root/.cache/pdm pdm install --prod --no-editable

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/.venv ./venv
COPY . .
RUN venv/bin/pip install --no-deps .
CMD ["python", "main.py"]