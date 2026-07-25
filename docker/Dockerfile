FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

COPY docker /app/docker
RUN chmod +x /app/docker/healthcheck.sh

# Устанавливаем procps (нужен для pgrep или ps aux)
RUN apt-get update && \
    apt-get install -y --no-install-recommends procps && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/app/logs

# Если хочешь, чтобы логи создавались сразу — можно добавить touch, но лучше в коде
# RUN touch /app/app/logs/app.log

# ... твой CMD или ENTRYPOINT
CMD ["python", "-m", "app.main"]
