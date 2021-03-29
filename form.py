from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from db import db, get_or_create_user, save_form
from utils import main_keyboard


def form_start(update, context):
    update.message.reply_text(
        'Как тебя зовут?',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def form_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text('Введите имя и фамилию')
        return 'name'
    else: 
        context.user_data['form'] = {'name': user_name}
        reply_keyboard = [['1', '2', '3', '4' , '5']]
        update.message.reply_text(
            'Оцените бота', reply_markup=ReplyKeyboardMarkup(reply_keyboard, 
            one_time_keyboard=True, resize_keyboard=True) 
            )
        return 'rating'


def form_rating(update, context): 
    context.user_data['form']['rating'] = int(update.message.text)
    update.message.reply_text('Напишите комментарий или введите /skip')
    return 'comment'


def form_skip(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_form(db, user["user_id"], context.user_data['form'])
    user_text = format_form(context.user_data['form'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def form_comment(update, context):
    context.user_data['form']['comment'] = update.message.text
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_form(db, user["user_id"], context.user_data['form'])
    user_text = format_form(context.user_data['form'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def format_form(form):
    user_text = f"""<b>Имя Фамилия</b>: {form['name']}
<b>Оценка</b>: {form['rating']}
"""
    if 'comment' in form:
        user_text += f"<b>Комментарий</b>: {form['comment']}"
    return user_text

def form_dontknow(update, context):
    update.message.reply_text('Я вас не понимаю')
