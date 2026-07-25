import socket
import os
import requests

def send_telegram_message(bot_token, chat_id, message):
    # Добавляем идентификатор источника
    hostname = socket.gethostname()
    container_id = os.environ.get("HOSTNAME", "unknown")
    message = f"[{hostname} | {container_id}] {message}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        requests.post(url, data={"chat_id": chat_id, "text": message})
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")
