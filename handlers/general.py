from telebot.types import Message

from dispatcher import bot, db
from keyboards.general import clear_keyboard, main_keyboard 

from i18n import START_MESSAGE


# def get_user_requests(chat_id):
#     if chat_id not in user_requests:
#         user_requests[chat_id] = []
#     return user_requests[chat_id]
# 
# @bot.message_handler(commands=['send'])
#     bot.sendmessage(config.ASK_CHANNEL_ID, 'hfgdh')
# user_requests = {}


@bot.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await bot.reply_to(message, START_MESSAGE,
                       reply_markup=main_keyboard())
    
    # ! needed to edit!
    db.writeUser(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)


@bot.message_handler(state="*", commands=['cancel'])
async def cancel(message: Message):
    await bot.delete_state(message.from_user.id, message.chat.id)
    await bot.send_message(message.chat.id, "Дія була припинена",
                       reply_markup=main_keyboard())
            
            
@bot.message_handler(text = "Мої запити 📝")
async def my_requests(message: Message):
    requests = db.get_user_requests(message.chat.id)
    if requests:
        await bot.send_message(message.chat.id, 'Ваші запити:')
        for request in requests:
            await bot.send_message(message.chat.id, request)
    else:
        await bot.send_message(message.chat.id, 'У вас немає запитів.')
#купіть слона
