from random import randint
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from clarifai.rest import ClarifaiApp
import settings


def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = 'Ваше число больше, вы выиграли'
    elif user_number == bot_number:
        message = 'Числа одинаковые, ничья'
    else: 
        message = 'Ваше число меньше, вы проиграли'
    return message

def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Прислать котика', KeyboardButton('Мои координаты', request_location=True), 'Заполнить анкету']], resize_keyboard=True)

def is_cat(file_name):
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    responce = model.predict_by_filename(file_name, max_concepts=5)
    if responce['status']['code'] == 10000:
        for concept in responce['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                return True
    return False

def cat_rating_inline_keyboard(image_name):
    callback_text = f'rating|{image_name}|'
    inlinekeyboard = [
        [
            InlineKeyboardButton("Нравится", callback_data=callback_text + '1'),
            InlineKeyboardButton("Не нравится", callback_data=callback_text +'-1')
        ]
    ]
    return InlineKeyboardMarkup(inlinekeyboard)

if __name__ == '__main__':
    print(is_cat('img\cat1.jpg'))
    print(is_cat('img\\not_cat.jpg'))
