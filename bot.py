import logging
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from handlers import greet_user, guess_number, send_cat_image, user_cordinates

from calculator import tell_result_of_calculation
from cities_game import play_cities
from consellation import tell_consellation
from next_full_moon import tell_next_full_moon_date
import settings
from word_counter import tell_amount_of_words 

"""
НАЗВАНИЕ БОТА echo_learn_bot
"""

logging.basicConfig(filename='bot.log', level=logging.INFO)
PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': 
        {'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', tell_consellation))
    dp.add_handler(CommandHandler('wordcount', tell_amount_of_words))
    dp.add_handler(CommandHandler('next_full_moon', tell_next_full_moon_date))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_image))
    dp.add_handler(CommandHandler('cities', play_cities))
    dp.add_handler(CommandHandler('calc', tell_result_of_calculation))
    dp.add_handler(MessageHandler(Filters.location, user_cordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_image))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
