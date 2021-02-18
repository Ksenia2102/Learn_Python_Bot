import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import consellation
import ephem
from datetime import date


"""
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

# ставим обработчик команды /planet с вызовом функции из модуля consellation
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', consellation.say_consellation))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

if __name__ == "__main__":
    main()