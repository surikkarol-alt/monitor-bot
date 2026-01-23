import sys
from app.monitor import monitor
from app.config import BOT_TOKEN, CHAT_ID, LOG_FILE


def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN or CHAT_ID not set")
        sys.exit(1)

    print("✅ AlertMonitor started")
    monitor(BOT_TOKEN, CHAT_ID, LOG_FILE)


if __name__ == "__main__":
    main()
