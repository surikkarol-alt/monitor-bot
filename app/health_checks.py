import os
import requests

def check_filesystem():
    try:
        test_file = "/tmp/healthcheck_test"
        with open(test_file, "w") as f:
            f.write("ok")
        os.remove(test_file)
        return True, "filesystem ok"
    except Exception as e:
        return False, f"filesystem error: {e}"

def check_telegram(bot_token):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return True, "telegram ok"
        return False, f"telegram bad status {r.status_code}"
    except Exception as e:
        return False, f"telegram error: {e}"
