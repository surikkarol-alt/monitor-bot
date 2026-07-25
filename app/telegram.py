import requests
import logging

logger = logging.getLogger("telegram")

def send_telegram(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        r = requests.post(url, json=payload, timeout=5)
        r.raise_for_status()
    except Exception as e:
        logger.error(f"Telegram error: {e}")
