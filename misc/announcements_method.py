# from telebot.formatting import apply_html_entities
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