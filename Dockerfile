# Используем стабильный легковесный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей сначала (оптимизация кэша Docker)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Гарантируем, что логи Python сразу выводятся в консоль Docker
ENV PYTHONUNBUFFERED=1

# Создаем пустой лог-файл (если монитор его ожидает)
RUN touch /app/app.log

# Запускаем наш монитор
CMD ["python3", "alert_monitor.py"]
