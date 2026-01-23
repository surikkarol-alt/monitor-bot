import requests


def send_telegram_message(bot_token: str, chat_id: str, text: str):
    if not bot_token or not chat_id:
        print("❌ BOT_TOKEN or CHAT_ID not set")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        r.raise_for_status()
        print("📨 Telegram message sent")
    except Exception as e:
        print(f"❌ Telegram error: {e}")
