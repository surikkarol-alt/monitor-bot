import threading
from app.health import run_health_server
from app.monitor import monitor
from app.config import BOT_TOKEN, CHAT_ID, LOG_FILE

def main():
    # Запускаем health server в отдельном потоке
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()

    # Запускаем мониторинг
    monitor(BOT_TOKEN, CHAT_ID)


if __name__ == "__main__":
    main()
