from telebot.types import Message

from dispatcher import bot, db
from keyboards.general import clear_keyboard, main_keyboard 
from states.general import NewRequestState

# @bot.message_handler()
# async def process_query(message: Message):
#     # requests = get_user_requests(message.chat.id)
#     # requests.append(message.text)
#     await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")


