
def tell_amount_of_words(update, context):
    print(context.__dict__)
    user_words = context.args
    words_amount_answer = count_words(user_words)
    update.message.reply_text(words_amount_answer)


def check_is_word(word):
    for letter in word:
        if letter.isalpha():
            return True


def count_words(words): 
    words_counter = 0
    for word in words:
        if word.isdigit() == True:
            return 'Вы ввели число'
        elif not check_is_word(word):
            return 'В вашем вводе нету букв'
        else: 
            words_counter += 1

    if words_counter == 1:
        return f'{words_counter} слово'
    elif words_counter >= 5 or words_counter == 0:
        return f'{words_counter} слов'
    else:
        return f'{words_counter} слова'

