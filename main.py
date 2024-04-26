from telebot.async_telebot import AsyncTeleBot
import asyncio

import config
import database
import handlers
import i18n
import images
import keyboards
import Middleware
import misc
import tests

bot = AsyncTeleBot(config.TOKEN)

asyncio.run(bot.polling())