import telebot
from init_bot import bot
from config import admins_list

@bot.message_handler(func = lambda message: message.text == "Создание опроса")
def create_survey(message: telebot.types.Message):
    if message.from_user.id in admins_list:
        pass