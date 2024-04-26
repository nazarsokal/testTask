from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

def clear_keyboard():
    return ReplyKeyboardRemove()

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # or:
    (keyboard.add('Відправити запит ❔', 'Мої запити 📝', row_width=2)
           .add('Підтримка 💁‍♂️')
    )
    return keyboard