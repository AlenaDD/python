import random
DIGITS = '0123456789'
LOWERCASE_LETTERS ='abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
number_password = int(input(' Введите количество генерируемых паролей: '))
len_password = int(input('Какова длина одного пароля?'))
chars = ''
if input('Включать в пароль цифры? (+/-)') == '+':
    chars += DIGITS
if input('Включать в пароль строчные буквы? (+/-)'):
    chars += LOWERCASE_LETTERS
if input('Включать в пароль прописные буквы? (+/-)'):
    chars += UPPERCASE_LETTERS
if input('Включать в пароль символы? (+/-)'):
    chars += PUNCTUATION
if input('Исключать ли неоднозначные  символы (il1Lo0O)? (+/-)'):
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')


def generate_password(number_password, len_password):
        for i in range(number_password):
            p = ''
            for j in range(len_password):
                p += random.choice(chars)
            print(p)

generate_password(number_password, len_password)

