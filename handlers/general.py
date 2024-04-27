from database import DatabaseService
from telebot.types import Message
from dispatcher import bot
from dispatcher import ReplyKeyboardRemove
from dispatcher import ReplyKeyboardMarkup
from telebot.types import Message

from keyboards.general import clear_keyboard, main_keyboard 

# @bot.message_handler(commands=['start'])
# async def send_welcome(message):
#     await bot.reply_to(message, "Привіт! Я бот, щоб допомагати людям шукати допомогу")
#
# list_of_request = []
#
# async def process_request(request, chat_id):
#     if request == "Відправити запит ❔":
#         await bot.register_next_step_handler(await bot.send_message(chat_id, 'Введіть ваш запит:'), handle_query)
#     elif request == "Мої запити 📝":
#         await bot.register_next_step_handler(await bot.sent_message(chat_id, 'Ваші запити:'), handle_query)
#         for i in list_of_request:
#             bot.send_message(i)
# @bot.message_handler()
# async def handle_query(message):
#     query_text = message.text
#     list_of_request.append(query_text)
#     await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")
#
#
#
# @bot.message_handler(func=lambda message: True)
# async def handle_message(message):
#     await process_request(message.text, message.chat.id)




def get_user_requests(chat_id):
    if chat_id not in user_requests:
        user_requests[chat_id] = []
    return user_requests[chat_id]

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, "Привіт! Я бот, щоб допомагати людям шукати допомогу",
                       reply_markup=main_keyboard())
    db = DatabaseService.DatabaseServiceClass()
    await db.writeUser(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)

@bot.message_handler(func=lambda message: message.text in ["Відправити запит ❔", "Мої запити 📝"])
async def handle_query(message):
    if message.text == "Відправити запит ❔":
        await bot.send_message(message.chat.id, 'Введіть ваш запит:')
    elif message.text == "Мої запити 📝":
        requests = get_user_requests(message.chat.id)
        if requests:
            await bot.send_message(message.chat.id, 'Ваші запити:')
            for request in requests:
                await bot.send_message(message.chat.id, request)
        else:
            await bot.send_message(message.chat.id, 'У вас немає запитів.')

@bot.message_handler()
async def process_query(message):
    requests = get_user_requests(message.chat.id)
    requests.append(message.text)
    await bot.send_message(message.chat.id, "Ваш запит був отриманий і буде оброблено.")

user_requests = {}

@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    await process_request(message.text, message.chat.id)

async def process_request(request, chat_id):
    if request == "Відправити запит ❔":
        await bot.send_message(chat_id, 'Введіть ваш запит:')
    elif request == "Мої запити 📝":
        requests = get_user_requests(chat_id)
        if requests:
            await bot.send_message(chat_id, 'Ваші запити:')
            for request in requests:
                await bot.send_message(chat_id, request)
        else:
            await bot.send_message(chat_id, 'У вас немає запитів.')

