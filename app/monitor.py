import time
import logging
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "/app/app/logs/app.log"

logging.basicConfig(level=logging.INFO, filename=LOG_FILE, format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger("monitor")

MONITORED_SERVICES = {
    "test-service": "http://test-service:9090/health"
}

STATE_FILE = "/app/state.json"

def send_telegram(msg: str):
    if not BOT_TOKEN or not CHAT_ID:
        logger.warning("BOT_TOKEN or CHAT_ID not set, cannot send message")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.get(url, params={"chat_id": CHAT_ID, "text": msg}, timeout=5)
        logger.info(f"Sent Telegram message: {msg}")
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")

def monitor():
    logger.info("Monitor started")
    previous_status = {name: True for name in MONITORED_SERVICES}
    while True:
        for name, url in MONITORED_SERVICES.items():
            try:
                r = requests.get(url, timeout=2)
                healthy = r.status_code == 200
            except:
                healthy = False

            if healthy != previous_status[name]:
                if healthy:
                    logger.info(f"{name} RECOVERED")
                    send_telegram(f"{name} RECOVERED")
                else:
                    logger.error(f"{name} is DOWN")
                    send_telegram(f"{name} is DOWN")
                previous_status[name] = healthy
        time.sleep(10)

if __name__ == "__main__":
    monitor()
