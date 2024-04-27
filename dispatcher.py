from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from telebot import asyncio_filters
from database import DatabaseServiceClass

import config

db = DatabaseServiceClass()
state_storage = StateMemoryStorage()
bot = AsyncTeleBot(config.TOKEN, state_storage=state_storage)

bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.add_custom_filter(asyncio_filters.TextMatchFilter())