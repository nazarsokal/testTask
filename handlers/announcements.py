from telebot.types import Message

from dispatcher import bot, db
from keyboards.general import clear_keyboard, main_keyboard 
from states.general import NewAnnouncementState

# @bot.message_handler()
# async def process_query(message: Message):
#     # requests = get_user_requests(message.chat.id)
#     # requests.append(message.text)
#     await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")

@bot.message_handler(func=lambda m: m.text == "Відправити запит ❔")
async def handle_request(message: Message):
    await bot.send_message(message.chat.id, 'Введіть заголовок оголошенння:', reply_markup=clear_keyboard())

@bot.message_handler(state=NewAnnouncementState.title)
async def get_size(message):
    inp = message.text
    if inp not in ["small", "large"]:
        await bot.send_message(message.chat.id, 'Please enter "large" or "small".')
        return
    await bot.send_message(message.chat.id, 'How will you pay? Cash or paypal?')
    await bot.set_state(message.from_user.id, NewAnnouncementState.descition, message.chat.id)
    
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['size'] = inp