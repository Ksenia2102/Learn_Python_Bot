from glob import glob
from random import choice, randint
from emoji import emojize
from utils import get_smile, play_random_number, main_keyboard

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет, пользователь! {context.user_data["emoji"]}',
        reply_markup = main_keyboard()
    )

def user_cordinates(update, context):
    cords = update.message.location
    update.message.reply_text(
        f'Ваши координаты: {cords}',
        reply_markup = main_keyboard()
    )

def send_cat_image(update, context):
    cat_img_list = glob('img/cat*.jp*')
    cat_img = choice(cat_img_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_img, 'rb'), reply_markup = main_keyboard())

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
