import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "/app/app/logs/app.log"


# Новые переменные для состояния
STATE_FILE = "/app/app/state.json"
ALERT_COOLDOWN = 60  # секунд
