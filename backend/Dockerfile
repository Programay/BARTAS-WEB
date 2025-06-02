FROM python:3.12-slim as builder

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*
# Install UV
RUN apt-get update && apt-get install -y curl \
    && curl -LsSf https://astral.sh/uv/0.6.9/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"
WORKDIR /backend

# Install dependencies
COPY pyproject.toml uv.lock ./

RUN uv pip compile --group dev --quiet --generate-hashes -o requirements.txt pyproject.toml
RUN uv pip install --no-cache --system -r requirements.txt

# Runtime
FROM python:3.12-slim
WORKDIR /backend

# Create non-root user
RUN useradd -m -d /backend -s /bin/bash appuser && \
    chown -R appuser:appuser /backend
USER appuser

# Copy dependencies
COPY --from=builder --chown=appuser:appuser /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder --chown=appuser:appuser /usr/local/bin /usr/local/bin

# Set PYTHONPATH
ENV PYTHONPATH="/backend" \
    PYTHONUNBUFFERED=1

CMD ["sh", "-c", "uvicorn src.main:app --reload --host 0.0.0.0 --port ${BE_PORT}"]