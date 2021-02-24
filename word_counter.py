"""
Функция принимает ответ пользователя и выводит кол-во введенных слов
"""
def tell_amount_of_words(update, context): 
    user_text = update.message.text
    words_amount_answer = count_words(user_text)
    update.message.reply_text(words_amount_answer)


"""
Функция считает кол-во слов в введенном предложении
"""
def count_words(words): 
    words = words.split()
    words_counter = -1 # первое слово всегда вызов /wordcount, поэтому начинает с -1
    for word in words:
        if word.isdigit() == True:
            return 'Вы ввели число'
        else: 
            words_counter += 1

    if words_counter == 1:
        return f'{words_counter} слово'
    elif words_counter >= 5 or words_counter == 0:
        return f'{words_counter} слов'
    else:
        return f'{words_counter} слова'

