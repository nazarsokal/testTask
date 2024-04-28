from telebot.asyncio_handler_backends import State, StatesGroup

class NewAnnouncementState(StatesGroup):
    title = State() 
    body = State()
    photo = State()
    confirm = State()