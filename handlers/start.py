import telebot
from init_bot import bot
from make_main_keyboard import make_main_keyboard

@bot.message_handler(commands=["start","Start"])
def start(message: telebot.types.Message):
    
    keyboard = make_main_keyboard(id)
    
    bot.send_message(message.chat.id, "Привет!\n\nЯ бот опросник!", reply_markup = keyboard)