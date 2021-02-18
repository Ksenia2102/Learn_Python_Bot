import ephem 
from datetime import date

"""
Функция принимает вызов команды и название планеты от пользователя
Получает название планеты и делает вызов функции по вычислению созвездия
Выводит пользователю название созвездия
Можно разбить на более мелкие фунции, чтобы не делать много действий в одной? 
"""
def say_consellation(update, context): 
    user_text = update.message.text
    planet_name = user_text.split()
    consellation_name = calculate_consellation(planet_name[1])
    update.message.reply_text(consellation_name)

"""
Получаем текущую дату в нужном формате для вычисления созвездия
"""
def get_date():
    current_date = str(date.today()).replace('-', '/')
    return current_date

"""
Вычисляем созвездия в зависимости от прилетевшего названия планеты
"""
def calculate_consellation(planet):
    date = get_date()
    if planet == 'Mercury':
        mercury = ephem.Mercury(date)
        return ephem.constellation(mercury)
    elif planet == 'Venus':
        venus = ephem.Venus(date)
        return ephem.constellation(venus)
    elif planet == 'Mars':
        mars = ephem.Mars(date)
        return ephem.constellation(mars)
    elif planet == 'Jupiter':
        jupiter = ephem.Jupiter(date)
        return ephem.constellation(jupiter)
    elif planet == 'Saturn':
        saturn = ephem.Saturn(date)
        return ephem.constellation(saturn)
    elif planet == 'Uranus':
        uranus = ephem.Uranus(date)
        return ephem.constellation(uranus)
    elif planet == 'Neptune':
        neptune = ephem.Neptune(date)
        return ephem.constellation(neptune)
