# Builder stage
FROM python:3.13-slim AS builder
RUN pip install pdm
WORKDIR /app
COPY pyproject.toml pdm.lock
RUN pdm init
RUN --mount=type=cache,target=/root/.cache/pdm pdm install --prod --no-editable

# Runtime stage
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /app/.venv ./venv
COPY . .
RUN pip install --no-deps .
CMD ["python", "src/price_radar/__init__.py"]