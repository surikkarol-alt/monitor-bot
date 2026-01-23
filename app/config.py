import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

LOG_FILE = os.getenv(
    "LOG_FILE",
    "/app/app/logs/app.log"
)
