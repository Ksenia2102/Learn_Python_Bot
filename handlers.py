import os
from glob import glob
from random import choice, randint

from emoji import emojize

from db import (db, get_image_rating, get_or_create_user, save_cat_image_vote,
                subscribe_user, unsubscribe_user, user_voted)
from jobs import alarm
from utils import (cat_rating_inline_keyboard, is_cat, main_keyboard,
                   play_random_number)


def greet_user(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    update.message.reply_text(
        f'Привет, пользователь! {user["emoji"]}',
        reply_markup = main_keyboard()
    )

def user_cordinates(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    cords = update.message.location
    update.message.reply_text(
        f'Ваши координаты: {cords}',
        reply_markup = main_keyboard()
    )

def send_cat_image(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    cat_img_list = glob('img/cat*.jp*')
    cat_img = choice(cat_img_list)
    chat_id = update.effective_chat.id
    if user_voted(db, cat_img, user["user_id"]):
        rating = get_image_rating(db, cat_img)
        keyboard = None
        caption = f'Рейтинг картинки: {rating}'
    else: 
        keyboard = cat_rating_inline_keyboard(cat_img)
        caption = None
    
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_img, 'rb'), reply_markup=keyboard, caption=caption)

def cat_picture_rating(update, context):
    update.callback_query.answer()
    callback_type, image_name, vote = update.callback_query.data.split('|')
    vote = int(vote)
    user = get_or_create_user(db, update.effective_user, update.effective_chat.id)
    save_cat_image_vote(db, user, image_name, vote)
    rating = get_image_rating(db, image_name)
    update.callback_query.edit_message_caption(caption=f'Рейтинг картинки: {rating}')

def guess_number(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
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
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
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


def subscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    subscribe_user(db, user)
    update.message.reply_text('Вы успешно подписались')


def unsubscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    unsubscribe_user(db, user)
    update.message.reply_text('Вы отписались от рассылки')


def set_alarm(update, context):
    try:
        alarm_seconds = abs(int(context.args[0]))
        context.job_queue.run_once(alarm, alarm_seconds, context=update.message.chat.id)
        update.message.reply_text(f'Уведомление придет через {alarm_seconds} сек')
    except (ValueError, TypeError):
        update.message.reply_text('Введите число')
