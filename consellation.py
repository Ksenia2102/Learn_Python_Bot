import ephem 
from datetime import date

"""
Функция принимает вызов команды и название планеты от пользователя
Получает название планеты и делает вызов функции по вычислению созвездия
Выводит пользователю название созвездия
Можно разбить на более мелкие фунции, чтобы не делать много действий в одной? 
"""
def tell_consellation(update, context): 
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
# Способ 1 (перебор через if)
# def calculate_consellation(planet):
#     date = get_date()
#     if planet == 'Mercury':
#         mercury = ephem.Mercury(date)
#         return ephem.constellation(mercury)
#     elif planet == 'Venus':
#         venus = ephem.Venus(date)
#         return ephem.constellation(venus)
#     elif planet == 'Mars':
#         mars = ephem.Mars(date)
#         return ephem.constellation(mars)
#     elif planet == 'Jupiter':
#         jupiter = ephem.Jupiter(date)
#         return ephem.constellation(jupiter)
#     elif planet == 'Saturn':
#         saturn = ephem.Saturn(date)
#         return ephem.constellation(saturn)
#     elif planet == 'Uranus':
#         uranus = ephem.Uranus(date)
#         return ephem.constellation(uranus)
#     elif planet == 'Neptune':
#         neptune = ephem.Neptune(date)
#         return ephem.constellation(neptune)

# Способ 2 (через словарь)

date = get_date()
planets = {
    'Mercury': ephem.Mercury(date), 
    'Venus': ephem.Venus(date), 
    'Mars': ephem.Mars(date),
    'Jupiter': ephem.Jupiter(date),
    'Saturn': ephem.Saturn(date),
    'Uranus': ephem.Uranus(date),
    'Neptune': ephem.Neptune(date),
}

def calculate_consellation(planet):
    if planet in planets:
        return ephem.constellation(planets[planet])

# Способ 3 (через getattr)

