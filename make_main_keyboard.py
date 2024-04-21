import telebot
from main import bot
from telebot import types
from main import admins_list
import main

def make_main_keyboard(id):
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    if id in admins_list:
        buttons = [[types.KeyboardButton("Прохождение опроса")],
                   [types.KeyboardButton("Удаление опроса"), types.KeyboardButton("Создание опроса")],
                   [types.KeyboardButton("Просмотр общей статистики"), types.KeyboardButton("Просмотр личной статистики")]
                   ]
        
        for row in buttons:
            keyboard.add(*row)
        
    else:
        buttons = [[types.KeyboardButton("Прохождение опроса")],
                   [types.KeyboardButton("Просмотр общей статистики"), types.KeyboardButton("Просмотр личной статистики")]
                   ]
        
        for row in buttons:
            keyboard.add(*row)

    return keyboard