from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from database import DatabaseServiceClass

import config

db = DatabaseServiceClass()
state_storage = StateMemoryStorage()
bot = AsyncTeleBot(config.TOKEN, state_storage=state_storage)