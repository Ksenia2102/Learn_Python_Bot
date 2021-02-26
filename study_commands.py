from random import randint, choice
from glob import glob
from emoji import emojize

"""
Команды уроков по треку Телеграм-Бот
"""

# игра угадай число /guess
def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else: 
        message = 'Введите число'
    update.message.reply_text(message)

def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = 'Ваше число больше, вы выиграли'
    elif user_number == bot_number:
        message = 'Числа одинаковые, ничья'
    else: 
        message = 'Ваше число меньше, вы проиграли'
    return message

# отсылаем рандомную фотку котика /cat
def send_cat_image(update, context):
    cat_img_list = glob('img/cat*.jp*')
    print(cat_img_list)
    cat_img = choice(cat_img_list)
    print(cat_img)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_img, 'rb'))