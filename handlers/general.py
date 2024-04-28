from telebot.types import Message

from keyboards.general import main_keyboard, all_chanels_markup
from misc.announcements_method import send_announcement
from dispatcher import bot, db
from i18n import START_MESSAGE


@bot.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await bot.reply_to(message, START_MESSAGE,
                       reply_markup=main_keyboard())

    db.writeUser(message.from_user)


@bot.message_handler(state="*", commands=['cancel'])
async def cancel(message: Message):
    await bot.delete_state(message.from_user.id, message.chat.id)
    await bot.send_message(message.chat.id, "Дія була припинена",
                       reply_markup=main_keyboard())
            

@bot.message_handler(text = "Підтримка 💁‍♂️")
async def help_message(message: Message):
    await bot.send_message(message.chat.id,"Корисні посилання:", reply_markup=all_chanels_markup())

@bot.message_handler(text = "Мої запити 📝")
async def my_requests(message: Message):
    requests = db.get_user_requests(message.chat.id)
    if requests:
        await bot.send_message(message.chat.id, 'Ваші запити:')
        for request in requests:
            # markup = close_open_announcement_markup(request)
            await send_announcement(bot, message.chat.id, request)
    else:
        await bot.send_message(message.chat.id, 'У вас немає запитів')

#купіть слона