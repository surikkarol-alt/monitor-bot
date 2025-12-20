import asyncio
from telegram import Bot

TOKEN = "8459636192:AAEcNtQw7-G1YipY3MLhbRkInuPk0zyllrI"
CHAT_ID = 217195219

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ ТЕСТ УСПЕШЕН: сообщение отправлено!"
    )

asyncio.run(main())
