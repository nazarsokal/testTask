from telebot.types import Message

from dispatcher import bot, db
from keyboards.general import clear_keyboard, main_keyboard 
from states.general import NewAnnouncementState

# @bot.message_handler()
# async def process_query(message: Message):
#     # requests = get_user_requests(message.chat.id)
#     # requests.append(message.text)
#     await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")

@bot.message_handler(text = "Відправити запит ❔")
async def handle_request(message: Message):
    await bot.set_state(message.from_user.id, NewAnnouncementState.title, message.chat.id)
    await bot.send_message(message.chat.id, 'Введіть заголовок оголошенння:', reply_markup=clear_keyboard())

@bot.message_handler(state=NewAnnouncementState.title)
async def get_size(message):
    title = message.text
    
    await bot.set_state(message.from_user.id, NewAnnouncementState.description, message.chat.id)
    await bot.send_message(message.chat.id, 'Заголовок прийнято, тепер введіть опис')
    
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['title'] = title