import re
"""
Научите бота выполнять основные арифметические действия с двумя числами: 
сложение, вычитание, умножение и деление. 
Если боту дать команду /calc 2-3, он должен ответить “-1”.

Не забудьте обработать возможные ошибки во вводе: 
пробелы, отсутствие чисел, деление на ноль
Подумайте, как можно сделать поддержку действий с тремя и более числами
"""

def splitting_str(user_calc):
    
    sign_for_calc = ''
    for sign in user_calc:
        if not sign.isdigit():
            sign_for_calc += sign

    user_calc = re.split('-|\+|/|\*', user_calc)
    number_1 = int(user_calc[0])
    number_2 = int(user_calc[1])

    return number_1, number_2, sign_for_calc

def calculate(user_info): 
    try:
        number_to_calculate = splitting_str(user_info)

        number_1 = number_to_calculate[0]
        number_2 = number_to_calculate[1]
        sign = number_to_calculate[2]
        print(sign)

        try:
            if sign == '+':
                return number_1 + number_2
            elif sign == '-':
                return number_1 - number_2
            elif sign == '/':
                return number_1 / number_2
            elif sign == '*':
                return number_1 * number_2
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'
    except ValueError:
        return 'Неверный математический знак!'


def tell_result_of_calculation(update, context):
    user_info = context.args[0]
    result_of_calculation = calculate(user_info)
    update.message.reply_text(result_of_calculation)