#!/usr/bin/env python3
import time
import os
import urllib.parse
import urllib.request

# Путь к лог-файлу
LOG_FILE = "/app/app.log"
KEYWORDS = ["ERROR", "CRITICAL"]

# Берём токен и chat_id из переменных окружения (GitHub Secrets / Fly secrets)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Анти-спам: минимальный интервал между сообщениями для одного ключевого слова
COOLDOWN_SECONDS = 30
last_sent = {}  # словарь keyword -> timestamp последнего сообщения

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

    # Ждём, пока появится лог-файл
    while not os.path.exists(LOG_FILE):
        print("Log file not found, waiting...")
        time.sleep(2)

    with open(LOG_FILE, "r") as f:
        # Перемещаемся в конец файла, чтобы читать только новые строки
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
    import threading
    import uvicorn
    import fastapi

    app = fastapi.FastAPI()

    @app.get("/")
    def root():
        return {"status": "running"}

    # Запускаем монитор в отдельном потоке
    t = threading.Thread(target=monitor, daemon=True)
    t.start()

    # Запускаем HTTP-сервер для Fly
    uvicorn.run(app, host="0.0.0.0", port=8080)
