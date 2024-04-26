from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

def clear_keyboard():
    return ReplyKeyboardRemove()

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # or:
    (markup.add('Відправити запит', 'Мої запити', row_width=2)
           .add('Підтримка')
    )
    # display this markup:
    # bot.send_message(chat_id, 'Text', reply_markup=markup)