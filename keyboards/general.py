from telebot import types
from telebot.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardRemove
                           )


def clear_keyboard():
    return ReplyKeyboardRemove()

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Відправити запит ❔', 'Мої запити 📝', row_width=2)
    keyboard.add('Підтримка 💁‍♂️')
    
    return keyboard

def announcement_confirm():
    keyboard = InlineKeyboardMarkup()
    btn1 =  InlineKeyboardButton("Опублікувати", callback_data="announcement_confirm")
    btn2 =  InlineKeyboardButton("Скасувати", callback_data="announcement_cancle")
    keyboard.row(btn1, btn2)
    return keyboard

def help_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton("Підтримка ДопомогаUA💁‍♂️", url="https://t.me/+bM_8FTZBDGUyNzcy")
    btn2 =  types.InlineKeyboardButton("ДопомогаUA", url="https://t.me/KRKtest")
    markup.add(btn1)
    markup.add(btn2)
    return markup