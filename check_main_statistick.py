import telebot
from main import bot

@bot.message_handler(func = lambda message: message.text == "Просмотр общей статистики")
def check_main_statistick(message: telebot.types.Message):
    pass