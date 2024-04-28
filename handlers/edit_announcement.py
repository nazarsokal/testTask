from telebot.types import Message, CallbackQuery

import config
from keyboards.general import close_open_announcement_markup
from misc.announcements_method import send_announcement, make_announcement_text
from dispatcher import bot, db

@bot.message_handler(text = "Мої запити 📝")
async def my_requests(message: Message):
    requests = db.get_user_requests(message.chat.id)
    if requests:
        await bot.send_message(message.chat.id, 'Ваші запити:')
        for request in requests:
            markup = close_open_announcement_markup(request)
            m = await send_announcement(bot, message.chat.id, request, reply_markup=markup)
    else:
        await bot.send_message(message.chat.id, 'У вас немає запитів')

@bot.callback_query_handler(func=lambda callback: callback.data.startswith('close-open.'))
async def callbackMessage(callback: CallbackQuery):
    _, user_id, msg_id, op = callback.data.split('.')
    msg_id = int(msg_id)
    if callback.from_user.id != user_id:
        await bot.answer_callback_query(callback.id, 'Це не ваше повідомлення')
    
    data = db.get_Title_Body(msg_id)[0]
    text = make_announcement_text(data)
    PREFIX = '<b>Збір закрито!</b>\n\n'
    if op == 'close':
        data['isClosed'] = True
        text = PREFIX + text
    elif op == 'open':
        data['isClosed'] = False
        text = text.removeprefix(PREFIX)
    else:
        raise ValueError(f"Invalid callback type '{callback.data}'")
    
    
    if data['photoID']:
        await bot.edit_message_caption(text, config.ANNOUNCEMENT_CHANNEL_ID, msg_id)
    else:
        await bot.edit_message_text(text, config.ANNOUNCEMENT_CHANNEL_ID, msg_id)
    
    db.closeFundraisng(msg_id, data['isClosed'])
    
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=close_open_announcement_markup(data))
    await bot.answer_callback_query(callback.id, 'Операція успішно виконана')