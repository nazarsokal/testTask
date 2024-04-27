from telebot.asyncio_storage.base_storage import StateContext
from i18n import (NEW_ANNOUNCEMENTT_BLOCK,
                 NEW_ANNOUNCEMENTT_BLOCK_MISSING as NABM, 
                 NEW_ANNOUNCEMENTT_BLOCK_CURRENT as NABC,
                 NEW_ANNOUNCEMENTT_BLOCK_PRESENT as NABP
                )
def format_announcements_block(data: StateContext):
    text = NEW_ANNOUNCEMENTT_BLOCK.format(
        title=data.get('title', NABM),
        description=data.get('description', NABC),
        photo=data.get('photo', NABP)
    )