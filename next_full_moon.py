import ephem 
from datetime import date


def tell_next_full_moon_date(update, context): 
    user_date = context.args[0]
    next_full_moon_date = count_next_full_moon(user_date)
    update.message.reply_text(next_full_moon_date)

def change_date(date):
    date = date.replace('-', '/')
    return date

def count_next_full_moon(date):
    date = change_date(date)
    next_full_moon_date = ephem.next_full_moon(date)
    return f'Ближайшее полнолуние наступит: {next_full_moon_date}'