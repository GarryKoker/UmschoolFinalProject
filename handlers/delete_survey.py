import telebot
from init_bot import bot
from config import admins_list

@bot.message_handler(func = lambda message: message.text == "Удаление опроса")
def delete_survey(message: telebot.types.Message):
    if message.from_user.id in admins_list:
        pass