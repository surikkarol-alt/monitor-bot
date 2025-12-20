import time
import os
from telegram import Bot

# === НАСТРОЙКИ ===
TOKEN = "<8459636192:AAEcNtQw7-G1YipY3MLhbRkInuPk0zyllrI>"     # вставь сюда токен Telegram бота
CHAT_ID = "217195219"      # сюда вставим позже (я объясню)
LOG_FILE = "/home/sharif/logs/system.log"   # путь к логу (заменим на твой)

bot = Bot(TOKEN)

# Список ошибок, которые будем ловить
ERROR_KEYWORDS = [
    "ERROR",
    "CRITICAL",
    "Service crashed",
    "Database unreachable",
    "High CPU load",
    "Disk usage rising",
]

last_size = 0

def check_logs():
    global last_size

    if not os.path.exists(LOG_FILE):
        print("Файл логов не найден!")
        return

    current_size = os.path.getsize(LOG_FILE)

    # Если файл ещё не изменился — выходим
    if current_size == last_size:
        return

    with open(LOG_FILE, "r") as f:
        f.seek(last_size)
        new_data = f.read()
        last_size = current_size

    # Проверяем новые строки
    for line in new_data.split("\n"):
        for keyword in ERROR_KEYWORDS:
            if keyword in line:
                message = f"⚠️ ОБНАРУЖЕНА ПРОБЛЕМА:\n\n{line}"
                bot.send_message(chat_id=CHAT_ID, text=message)
                print("Отправлено:", line)

def main():
    print("Colorado Lock Monitor запущен...")
    while True:
        check_logs()
        time.sleep(2)

if __name__ == "__main__":
    main()
