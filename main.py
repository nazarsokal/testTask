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

from dispatcher import bot

asyncio.run(bot.polling())