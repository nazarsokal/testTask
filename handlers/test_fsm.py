import telebot # telebot

from telebot import custom_filters
from telebot.asyncio_handler_backends import State, StatesGroup #States

# States storage
from telebot.asyncio_storage import StateMemoryStorage


# Now, you can pass storage to bot.
state_storage = StateMemoryStorage() # you can init here another storage

bot = telebot.TeleBot("<YOUR TOKEN HERE>", state_storage=state_storage)


# States group.
class MyStates(StatesGroup):
    # Just name variables differently
    size = State() # creating instances of State class is enough from now
    payment = State()
    confirmation = State()


@bot.message_handler(commands=['order'])
def order(message):
    bot.set_state(message.from_user.id, MyStates.size, message.chat.id)
    bot.send_message(message.chat.id, 'What size of pizza do you want? Large or small?')
 

@bot.message_handler(state="*", commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "Your order was cancelled.")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=MyStates.size)
def get_size(message):
    inp = message.text.lower()
    if inp not in ["small", "large"]:
        bot.send_message(message.chat.id, 'Please enter "large" or "small".')
        return
    bot.send_message(message.chat.id, 'How will you pay? Cash or paypal?')
    bot.set_state(message.from_user.id, MyStates.payment, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['size'] = inp
 
 
@bot.message_handler(state=MyStates.payment)
def get_payment(message):
    inp = message.text.lower()
    if inp not in ["cash", "paypal"]:
        bot.send_message(message.chat.id, 'Please enter "cash" or "paypal".')
        return    
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Your order details\n---------\n"
               f"Size: {data['size']}\n"
               f"Payment: {inp}\n---------\n"
               f"Is that correct [yes/no]?")
    bot.send_message(message.chat.id, msg)
    bot.set_state(message.from_user.id, MyStates.confirmation, message.chat.id)

 
# result
@bot.message_handler(state=MyStates.confirmation)
def confirm_order(message):
    inp = message.text.lower()  
    if inp == "yes":
        bot.send_message(message.chat.id, "Great. The order is on its way.")
        bot.delete_state(message.from_user.id, message.chat.id)
        return
    elif inp == "no":
        bot.send_message(message.chat.id, "Okay. Let's start again.")
        order(message)
        return
    bot.send_message(message.chat.id, 'Please enter "yes" or "no".')


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling(skip_pending=True)