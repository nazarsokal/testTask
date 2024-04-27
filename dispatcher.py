from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ReplyKeyboardRemove

import config

bot = AsyncTeleBot(config.TOKEN)