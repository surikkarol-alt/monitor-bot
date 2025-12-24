import time
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Настройка логирования
logging.basicConfig(level=logging.INFO)

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

# ---------- ФУНКЦИИ ОПОВЕЩЕНИЯ (COOLDOWN) ----------
COOLDOWN = 30
last_sent = {}

def can_send(chat_id):
    now = time.time()
    last = last_sent.get(chat_id, 0)
    return (now - last) >= COOLDOWN

def mark_sent(chat_id):
    last_sent[chat_id] = time.time()

# ---------- MAIN ----------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
