from telebot.types import Message, User

from telebot import types

from keyboards.general import clear_keyboard, main_keyboard 
from states.general import NewAnnouncementState
from dispatcher import bot, db
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
    db.writeUser(message.from_user)


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
    

@bot.message_handler(text = "Підтримка 💁‍♂️")
async def help_message(message: Message):
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton("Підтримка ДопомогаUA💁‍♂️", url="https://t.me/+bM_8FTZBDGUyNzcy")
    btn2 =  types.InlineKeyboardButton("ДопомогаUA", url="https://t.me/KRKtest")
    markup.add(btn1)
    markup.add(btn2)
    await bot.send_message(message.chat.id,"КОрисні посилання:", reply_markup=markup)

    
    
