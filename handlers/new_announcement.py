from telebot.types import Message, CallbackQuery

from keyboards.general import clear_keyboard, main_keyboard, announcement_confirm_markup
from misc.announcements_method import format_announcements_block, send_announcement
from states.general import NewAnnouncementState
from dispatcher import bot, db


@bot.message_handler(text = "Відправити запит ❔")
async def handle_announcements(message: Message):
    await bot.delete_state(message.from_user.id, message.chat.id)
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

        await send_announcement(bot, message.chat.id, data)
            
        await bot.set_state(message.from_user.id, NewAnnouncementState.confirm, message.chat.id)
        await bot.send_message(message.chat.id, 'Що робити з публікацею?', reply_markup=announcement_confirm_markup())
        print(data)
        
    
@bot.callback_query_handler(state=NewAnnouncementState.confirm, func=lambda callback: callback.data == "announcement_confirm")
async def callbackMessage(callback: CallbackQuery):
    async with bot.retrieve_data(callback.from_user.id, callback.from_user.id) as data:     
        post = await send_announcement(bot, callback.message.chat.id, data)

        db.writeUserAnnouncement(callback.from_user.id,
                                 post.chat.id,
                                 data['title'],
                                 data['body'],
                                 data['photo']
                                 )
            
        await bot.send_message(callback.from_user.id, "Оголошення успішно відправлено на канал")


@bot.callback_query_handler(state=NewAnnouncementState.confirm, func=lambda callback: callback.data == "announcement_cancle")
async def cancel(callback: CallbackQuery):
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id)
    await bot.delete_state(callback.from_user.id, callback.message.chat.id)
    await bot.send_message(callback.message.chat.id, "Оголошення скасовано",
                       reply_markup=main_keyboard())
    await bot.answer_callback_query(callback.id)
