from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from i18n import (NEW_ANNOUNCEMENTT_BLOCK,
                 NEW_ANNOUNCEMENTT_BLOCK_MISSING as NABM, 
                 NEW_ANNOUNCEMENTT_BLOCK_CURRENT as NABC,
                 NEW_ANNOUNCEMENTT_BLOCK_PRESENT as NABP
                )
def format_announcements_block(fsm_data: dict | None, current_state: int):
    if fsm_data is None: 
        fsm_data = {}
    
    params = ['title', 'body', 'photo']
    
    data = [
        NABP if fsm_data.get(param) else NABM
        for param in params
    ]
    data[current_state] = NABC
    
    text = NEW_ANNOUNCEMENTT_BLOCK.format(
        title=data[0],
        body=data[1],
        photo=data[2]
    )
    return text

async def send_announcement(bot: AsyncTeleBot, chat_id: int, data: dict, **kwargs) -> Message:
    text = f"<b>{data['title']}</b>\n<i>{data['body']}</i>"
    if data['photo']:
        message = await bot.send_photo(chat_id, data['photo'], text, **kwargs)
    else:
        message = await bot.send_message(chat_id, text, **kwargs)
    
    return message
    
    