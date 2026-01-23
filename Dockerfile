# docker/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Копируем зависимости и исходники
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Создаём папку для логов внутри контейнера
RUN mkdir -p /app/app/logs

CMD ["python", "-m", "app.main"]
