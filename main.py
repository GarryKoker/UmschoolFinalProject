import telebot
from telebot import types
from check_main_statistick import *
from check_main_statistick import *
from create_survey import *
from delete_survey import *
from make_main_keyboard import *
from start import *
from taking_survey import *
from config import TOKEN
from init_bot import bot

if __name__ == "__main__":

    print("Бот запущен")

    bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))

    bot.infinity_polling()