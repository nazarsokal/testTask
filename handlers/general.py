from dispatcher import bot
from keyboards.general import clear_keyboard, main_keyboard 

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 
                       "Привіт! Я бот, щоб допомагати людям шукати допомогу",
                       reply_markup=main_keyboard())
    