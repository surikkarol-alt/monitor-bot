import json
import os
import time

from app.config import ALERT_COOLDOWN, LOG_FILE, STATE_FILE


if os.path.exists(STATE_FILE):
    with open(STATE_FILE) as f:
        state = json.load(f)
else:
    state = {"last_alert": 0}


def send_alert():
    now = time.time()

    if now - state.get("last_alert", 0) >= ALERT_COOLDOWN:
        print("🔥 ALERT! Something happened!")
        state["last_alert"] = now

        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
    else:
        print("Cooldown active, alert skipped")


def monitor_task():
    if os.path.exists(LOG_FILE):
        send_alert()


if __name__ == "__main__":
    monitor_task()
