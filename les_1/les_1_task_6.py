"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
https://drive.google.com/file/d/1Jj1mSL0hqVAIcZt_FKijFNLEo7idMwxA/view?usp=sharing
"""


index_letter = int(input('Введите номер буквы от 0 до 25 :\t'))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter = alphabet[index_letter]

print(' Номер буквы: {} \n Буква: {}'.format(index_letter, letter))
