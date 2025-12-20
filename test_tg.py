import telegram

TOKEN = "8459636192:AAEcNtQw7-G1YipY3MLhbRkInuPk0zyllrI"
CHAT_ID = 217195219  # без кавычек, число!

bot = telegram.Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ ТЕСТ: Telegram работает!")
