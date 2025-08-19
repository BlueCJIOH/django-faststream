FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY pyproject.toml ./
RUN uv pip install --system .

COPY src ./src

WORKDIR /app/src
CMD ["uv", "run", "uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--lifespan", "on"]
