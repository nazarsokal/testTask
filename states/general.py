from telebot.asyncio_handler_backends import State, StatesGroup

class NewRequestState(StatesGroup):
    title = State() 
    descition = State()
    photo = State()
    confirm = State()