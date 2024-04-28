from dispatcher import bot
import handlers
import asyncio

print('<<Bot started>>')
asyncio.run(bot.polling())
