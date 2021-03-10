from glob import glob
import os
from random import choice, randint
from emoji import emojize
from utils import get_smile, play_random_number, main_keyboard, is_cat

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

def check_user_photo(update, context):
    update.message.reply_text('Фото в обработке')
    os.makedirs('downloads', exist_ok=True)
    user_photo = context.bot.get_file(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{user_photo.file_id}.jpg')
    user_photo.download(file_name)
    if is_cat(file_name):
        update.message.reply_text('На фото котик, добавляю его в библиотеку!')
        new_filename = os.path.join('img', f'cat_{user_photo.file_id}.jpg')
        os.rename(file_name, new_filename)
    else:
        os.remove(file_name)
        update.message.reply_text('На фото нет котика!')
