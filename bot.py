import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import consellation
import ephem
import word_counter
import next_full_moon
from datetime import date


"""
НАЗВАНИЕ БОТА echo_learn_bot
Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""

logging.basicConfig(filename='bot.log', level=logging.INFO)
PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': 
        {'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD}}

# ставим обработчик команды /wordcount с вызовом функции из модуля word_conter
# ставим обработчик команды /next_full_moon с вызовом функции из модуля next_full_moon

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', consellation.tell_consellation))
    dp.add_handler(CommandHandler('wordcount', word_counter.tell_amount_of_words))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon.tell_next_full_moon_date))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

if __name__ == "__main__":
    main()