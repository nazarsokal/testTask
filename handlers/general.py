from dispatcher import bot

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, "Привіт! Я бот, щоб допомагати людям шукати допомогу")
    