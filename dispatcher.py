from telebot.async_telebot import AsyncTeleBot
from database import DatabaseServiceClass

import config
db = DatabaseServiceClass()
bot = AsyncTeleBot(config.TOKEN)