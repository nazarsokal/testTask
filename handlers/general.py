from database import DatabaseService
from dispatcher import bot

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, "Привіт! Я бот, щоб допомагати людям шукати допомогу")

    db = DatabaseService.DatabaseServiceClass()
    await db.writeUser(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)


    