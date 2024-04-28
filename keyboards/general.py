from telebot.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardRemove
                           )
from telebot.types import Message


def clear_keyboard():
    return ReplyKeyboardRemove()

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Відправити запит ❔', 'Мої запити 📝', row_width=2)
    keyboard.add('Підтримка 💁‍♂️')
    
    return keyboard

def announcement_confirm_markup():
    markup = InlineKeyboardMarkup()
    btn1 =  InlineKeyboardButton("Опублікувати", callback_data="announcement_confirm")
    btn2 =  InlineKeyboardButton("Скасувати", callback_data="announcement_cancle")
    markup.row(btn1, btn2)
    return markup
    
def all_chanels_markup():
    markup = InlineKeyboardMarkup()
    btn1 =  InlineKeyboardButton("Підтримка ДопомогаUA💁‍♂️", url="https://t.me/+bM_8FTZBDGUyNzcy")
    btn2 =  InlineKeyboardButton("ДопомогаUA", url="https://t.me/KRKtest")
    markup.add(btn1)
    markup.add(btn2)
    return markup
