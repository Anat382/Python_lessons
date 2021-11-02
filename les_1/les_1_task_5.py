"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://drive.google.com/file/d/1Jj1mSL0hqVAIcZt_FKijFNLEo7idMwxA/view?usp=sharing
"""


letter1 = str(input('Введите первую букву от a-z:\t'))
letter2 = str(input('Введите вторую букву от a-z:\t'))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
count_alphabet = 25

index_letter1 = alphabet.index(letter1)
index_letter2 = alphabet.index(letter2)
count_beetwen_alphabets = abs((count_alphabet - index_letter1) - (count_alphabet - index_letter2)) - 1

print(' Индекс 1 буквы: {} \n Индекс 2 буквы: {} \n Количество букв между первой и второй буквами: {}'
      .format(index_letter1, index_letter2, count_beetwen_alphabets) )
