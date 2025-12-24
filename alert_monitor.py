#!/usr/bin/env python3
import time
import os
import urllib.parse
import urllib.request

LOG_FILE = "/app/app.log"
KEYWORDS = ["ERROR", "CRITICAL"]

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

COOLDOWN_SECONDS = 30   # анти-спам: 30 секунд
last_sent = {}          # keyword -> timestamp


def send_telegram(text: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram credentials missing")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": text
    }).encode()

    try:
        urllib.request.urlopen(url, data, timeout=10)
    except Exception as e:
        print("Telegram error:", e)


def monitor():
    print("AlertMonitor started...")

    while not os.path.exists(LOG_FILE):
        print("Log file not found, waiting...")
        time.sleep(2)

    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            line = line.strip()

            for keyword in KEYWORDS:
                if keyword in line:
                    now = time.time()
                    last_time = last_sent.get(keyword, 0)

                    if now - last_time >= COOLDOWN_SECONDS:
                        msg = f"🚨 {keyword}\n{line}"
                        print(msg)
                        send_telegram(msg)
                        last_sent[keyword] = now


if __name__ == "__main__":
    monitor()
