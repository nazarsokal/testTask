from telebot.asyncio_handler_backends import State, StatesGroup

class NewAnnouncementState(StatesGroup):
    title = State() 
    description = State()
    photo = State()
    confirm = State()