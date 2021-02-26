import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import consellation
import ephem
import study_commands
import word_counter
import next_full_moon
from datetime import date
from emoji import emojize
from random import choice
import cities_game
import calculator

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
    dp.add_handler(CommandHandler('planet', consellation.tell_consellation))
    dp.add_handler(CommandHandler('wordcount', word_counter.tell_amount_of_words))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon.tell_next_full_moon_date))
    dp.add_handler(CommandHandler('guess', study_commands.guess_number))
    dp.add_handler(CommandHandler('cat', study_commands.send_cat_image))
    dp.add_handler(CommandHandler('cities', cities_game.play_cities))
    dp.add_handler(CommandHandler('calc', calculator.tell_result_of_calculation))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет, пользователь! {context.user_data["emoji"]}')

if __name__ == "__main__":
    main()