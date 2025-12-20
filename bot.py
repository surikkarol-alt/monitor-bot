from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


TOKEN = "8459636192:AAEcNtQw7-G1YipY3MLhbRkInuPk0zyllrI"

# ---------- КНОПКИ ----------
main_keyboard = ReplyKeyboardMarkup(
    [["Статус", "Старт"], ["Стоп", "Помощь"]],
    resize_keyboard=True
)

# ---------- КОМАНДА /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот Colorado Lock Monitor.\nВыбери действие:",
        reply_markup=main_keyboard
    )

# ---------- ОБРАБОТКА ТЕКСТА ----------
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Статус":
        await update.message.reply_text("Статус Colorado Lock: ❓ Проверка пока не подключена")
    elif text == "Старт":
        await update.message.reply_text("Мониторинг запущен (симуляция)")
    elif text == "Стоп":
        await update.message.reply_text("Мониторинг остановлен (симуляция)")
    elif text == "Помощь":
        await update.message.reply_text("Доступные команды:\nСтатус\nСтарт\nСтоп\nПомощь")
    else:
        await update.message.reply_text("Не понимаю. Выбери кнопку.")

# ---------- MAIN ----------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    app.run_polling()


if __name__ == "__main__":
    main()


# alerting_utils.py  (примерный файл)
import time
import logging

# cooldown seconds между сообщениями в один чат
COOLDOWN = 30  # например 30 секунд

# dict last_sent[chat_id] = timestamp
last_sent = {}

def can_send(chat_id):
    now = time.time()
    last = last_sent.get(chat_id, 0)
    return (now - last) >= COOLDOWN

def mark_sent(chat_id):
    last_sent[chat_id] = time.time()

def send_alert(bot, chat_id, text, parse_mode=None):
    """
    Безопасно отправляем — проверяем таймаут.
    bot: объект telegram.Bot или telegram.ext.Bot
    chat_id: int
    text: str
    """
    try:
        if not can_send(chat_id):
            logging.info(f"Throttle: skip sending message to {chat_id}")
            return False
        # если используешь синхронный интерфейс:
        bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
        mark_sent(chat_id)
        logging.info(f"Sent alert to {chat_id}")
        return True
    except Exception as e:
        logging.exception("Failed to send alert")
        return False
