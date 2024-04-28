from telebot.types import Message, CallbackQuery

import config
from dispatcher import bot, db
from keyboards.general import clear_keyboard, main_keyboard, announcement_confirm
from states.general import NewAnnouncementState
from misc.announcements_method import format_announcements_block

# @bot.message_handler()
# async def process_query(message: Message):
#     # requests = get_user_requests(message.chat.id)
#     # requests.append(message.text)
#     await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")

@bot.message_handler(text = "Відправити запит ❔")
async def handle_announcements(message: Message):
    await bot.set_state(message.from_user.id, NewAnnouncementState.title, message.chat.id)
    await bot.send_message(message.chat.id, format_announcements_block(None, 0), reply_markup=clear_keyboard())
    await bot.send_message(message.chat.id, 'Ропочнемо! Спершу введіть заголовок оголошенння:', reply_markup=clear_keyboard())

@bot.message_handler(state=NewAnnouncementState.title)
async def get_title(message: Message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['title'] = message.text
       
        await bot.set_state(message.from_user.id, NewAnnouncementState.body, message.chat.id)
        await bot.send_message(message.chat.id, format_announcements_block(data, 1), reply_markup=clear_keyboard())
        await bot.send_message(message.chat.id, 'Заголовок прийнято! Тепер введіть тіло', reply_markup=clear_keyboard())
    
@bot.message_handler(state=NewAnnouncementState.body)
async def get_body(message: Message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['body'] = message.text
       
        await bot.set_state(message.from_user.id, NewAnnouncementState.photo, message.chat.id)
        await bot.send_message(message.chat.id, format_announcements_block(data, 2), reply_markup=clear_keyboard())
        await bot.send_message(message.chat.id, 'Тіло прийнято! Тепер відправте фото, або відправте /skip', reply_markup=clear_keyboard())

@bot.message_handler(state=NewAnnouncementState.photo, content_types='photo')
@bot.message_handler(state=NewAnnouncementState.photo, commands=['skip'])
async def get_photo(message: Message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['photo'] = message.photo[-1].file_id if message.photo else None
        
        await bot.send_message(message.chat.id, 'Оголошення готове до публікування\nОсь так воно виглядатиме:', reply_markup=clear_keyboard())
        text = f"<b>{data['title']}</b>\n<i>{data['body']}</i>"
        if message.photo:
            await bot.send_photo(message.chat.id, data['photo'], text)
        else:
            await bot.send_message(message.chat.id, text)
            
        await bot.set_state(message.from_user.id, NewAnnouncementState.confirm, message.chat.id)
        await bot.send_message(message.chat.id, 'Що робити з публікацею?', reply_markup=announcement_confirm())
        print(data)
        
    
@bot.callback_query_handler(state=NewAnnouncementState.confirm, func=lambda callback: callback.data == "YES")
async def callbackMessage(callback: CallbackQuery):
    async with bot.retrieve_data(callback.from_user.id, callback.from_user.id) as data:     
        text = f"<b>{data['title']}</b>\n<i>{data['body']}</i>"
        if data['photo']:
            post = await bot.send_photo(config.ANNOUNCEMENT_CHANNEL_ID, data['photo'], text)
        else:
            post = await bot.send_message(config.ANNOUNCEMENT_CHANNEL_ID, text)
        db.writeUserAnnouncement(callback.from_user.id,
                                 post.chat.id,
                                 data['title'],
                                 data['body'],
                                 data['photo']
                                 )
            
        await bot.send_message(callback.from_user.id, "Оголошення успішно відправлено на канал")