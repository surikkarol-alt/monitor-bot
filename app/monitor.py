import os
import time
from app.telegram_sender import send_telegram_message


def monitor(bot_token, chat_id, log_file):
    print(f"👀 Watching log file: {log_file}")

    while not os.path.isfile(log_file):
        time.sleep(1)

    with open(log_file, "r") as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            if "ERROR" in line or "CRITICAL" in line:
                send_telegram_message(
                    bot_token,
                    chat_id,
                    f"🚨 ALERT:\n{line.strip()}"
                )
