from random import choice, randint
from emoji import emojize
from telegram import KeyboardButton, ReplyKeyboardMarkup
from clarifai.rest import ClarifaiApp
import settings


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

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

if __name__ == '__main__':
    print(is_cat('img\cat1.jpg'))
    print(is_cat('img\\not_cat.jpg'))
