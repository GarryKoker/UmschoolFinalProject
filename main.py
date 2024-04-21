from init_bot import bot
import telebot
from handlers import register_handlers

if __name__ == "__main__":

    register_handlers()
    
    print("Бот запущен")

    bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))

    bot.infinity_polling()