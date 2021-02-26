from random import choice


"""
Научите бота играть в города. Правила такие - внутри бота есть список городов, 
пользователь пишет /cities Москва и если в списке такой город есть, 
бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка.

Помните, с ботом могут играть несколько пользователей одновременно
"""

cities = ['Токио', 'Дели', 'Шанхай', 'Мехико', 'Каир', 'Мумбаи', 'Пекин', 'Осака', 'Стамбул', 
            'Москва', 'Париж', 'Сеул', 'Лондон', 'Чикаго', 'Гонконг', 'Багдад', 'Мадрид', 'Торонто', 
            'Атланта','Барселона', 'Санкт-Петербург', 'Анталия', 'Якутск']


def get_first_letter(city):
    first_letter = list(city)
    return first_letter[0].upper()

def get_last_letter(city):
    last_letter = list(city)
    return last_letter[-1].upper()

def compare_cities_by_letters(user_city):
    last_letter = get_last_letter(user_city)
    cities_start_with_letter = []

    for city in cities:
        if last_letter == get_first_letter(city):
            cities_start_with_letter.append(city)
    
    answer_city = choice(cities_start_with_letter)
    cities.remove(user_city)
    return answer_city


def play_cities(update, context):
    user_city = context.args[0]
    if user_city in cities:
        answer_city = compare_cities_by_letters(user_city)
        update.message.reply_text(f'{answer_city}, ваш ход')
        cities.remove(answer_city)

    else:
        last_letter = get_last_letter(user_city)
        update.message.reply_text(f'Больше не знаю городов на букву {last_letter}, вы победили!')