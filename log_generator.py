import time
import random
from datetime import datetime

LOG_FILE = "/home/sharif/logs/system.log"

LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]

MESSAGES = {
    "INFO": ["System check ok", "Service running", "Heartbeat ok"],
    "WARNING": ["High memory usage", "Disk usage 80%", "Slow response detected"],
    "ERROR": ["Service crash detected", "Database error", "Connection lost"],
    "CRITICAL": ["System failure", "Data corruption", "Security breach"]
}

print("Log generator started...")

while True:
    level = random.choice(LEVELS)
    message = random.choice(MESSAGES[level])

    log_line = f"{datetime.now()} | {level} | {message}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_line)

    print(log_line.strip())
    time.sleep(2)
