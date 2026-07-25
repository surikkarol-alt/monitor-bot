import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler
import os


class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        super().__init__()
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level


LOG_DIR = os.getenv("LOG_DIR", "/app/app/logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
ERROR_LOG_FILE = os.getenv("ERROR_LOG_FILE", "/app/app/logs/error.log")

os.makedirs(LOG_DIR, exist_ok=True)


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    formatter = Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 🔹 Основной лог (INFO, WARNING)
    app_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)
    app_handler.addFilter(MaxLevelFilter(logging.WARNING))

    # 🔹 ERROR лог
    error_handler = RotatingFileHandler(
        ERROR_LOG_FILE,
        maxBytes=100_000,
        backupCount=3,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # 🔹 Консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ♻️ Чистим старые хендлеры
    root.handlers.clear()

    # ➕ Подключаем новые
    root.addHandler(app_handler)
    root.addHandler(error_handler)
    root.addHandler(console_handler)
