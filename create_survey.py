import telebot
from main import bot
import main

@bot.message_handler(func = lambda message: message.text == "Создание опроса")
def create_survey(message: telebot.types.Message):
    if message.from_user.id in admins_list:
        pass