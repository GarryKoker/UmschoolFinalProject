import telebot
from init_bot import bot

@bot.message_handler(func = lambda message: message.text == "Прохождение опроса")
def taking_survey(message: telebot.types.Message):
    pass