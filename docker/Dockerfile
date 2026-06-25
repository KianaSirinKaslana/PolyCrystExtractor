FROM python:3.11-slim

WORKDIR /app

# 系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 依赖
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# 源码
COPY src/ ./src/
COPY tests/ ./tests/

ENV PYTHONPATH=/app/src:$PYTHONPATH

CMD ["python", "-m", "pytest", "tests/", "-v"]
