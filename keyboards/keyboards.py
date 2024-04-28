from telebot.types import (ReplyKeyboardMarkup,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardRemove
                           )
import config


def clear_keyboard():
    return ReplyKeyboardRemove()

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Відправити запит ❔', 'Мої запити 📝', row_width=2)
    keyboard.add('Всі канали 📕')
    
    return keyboard

def announcement_confirm_markup():
    markup = InlineKeyboardMarkup()
    btn1 =  InlineKeyboardButton("Опублікувати", callback_data="announcement_confirm")
    btn2 =  InlineKeyboardButton("Скасувати", callback_data="announcement_cancle")
    markup.row(btn1, btn2)
    return markup
    
def all_chanels_markup():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Підтримка ДопомогаUA💁‍♂️", url=config.SUPPORT_GROUP_LINK)
    btn2 = InlineKeyboardButton("Канал ДопомогаUA 🇺🇦", url=config.ANNOUNCEMENT_CHANNEL_LINK)
    markup.add(btn2)
    markup.add(btn1)
    return markup
