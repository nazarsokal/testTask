from telebot import types
from dispatcher import bot, db

CHANNEL_ID = '@KRKtest'
CHAT_ID = None
@bot.message_handler(commands=["confirm"])
async def write_to_channel(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton("Так", callback_data="YES")
    btn2 =  types.InlineKeyboardButton("Ні", callback_data="NO")
    markup.row(btn1, btn2)
    await bot.send_message(message.chat.id, "Ви впевнені що хочете запостити свій запит", reply_markup=markup)
    
    # Відправка повідомлення на канал
    
@bot.callback_query_handler(func=lambda callback: True)
async def callbackMessage(callback):
    if callback.data == "YES":
        requests = db.get_user_requests()
        await bot.send_message(CHANNEL_ID, requests)
        await bot.send_message(CHAT_ID, "Ваше повідомлення було успішно відправлене на канал.")
