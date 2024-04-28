# from telebot.formatting import apply_html_entities
from i18n import (NEW_ANNOUNCEMENTT_BLOCK,
                 NEW_ANNOUNCEMENTT_BLOCK_MISSING as NABM, 
                 NEW_ANNOUNCEMENTT_BLOCK_CURRENT as NABC,
                 NEW_ANNOUNCEMENTT_BLOCK_PRESENT as NABP
                )
def format_announcements_block(fsm_data: dict | None, current_state: int):
    if fsm_data is None: 
        fsm_data = {}
    
    data = [
        fsm_data.get('title', NABM),
        fsm_data.get('body', NABM),
        (NABM, NABP)[fsm_data.get('photo', False)] 
    ]
    data[current_state] = NABC
    
    text = NEW_ANNOUNCEMENTT_BLOCK.format(
        title=data[0],
        body=data[1],
        photo=data[2]
    )
    return text