import telebot
from main import bot

@bot.message_handler(func = lambda message: message.text == "Просмотр моей статистики")
def check_my_statistick(message: telebot.types.Message):
    pass