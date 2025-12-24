# Используем стабильный легковесный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Сначала копируем только файл зависимостей (оптимизация кэша Docker)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Гарантируем, что логи Python сразу выводятся в консоль Docker
ENV PYTHONUNBUFFERED=1

# Создаем пустой файл логов, если монитор ожидает его наличия в /app/app.log
RUN touch /app/app.log

# Запускаем скрипт
CMD ["python3", "alert_monitor.py"]
