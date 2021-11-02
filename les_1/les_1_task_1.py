"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1Jj1mSL0hqVAIcZt_FKijFNLEo7idMwxA/view?usp=sharing
"""

number = int(input('Введите трехзначное  число: '))

if number > 0:
    if 1 <= number // 100 < 10:
        summa = (number // 100) + (number // 10 % 10) + (number % 10)
        multiplication = (number // 100) * (number // 10 % 10) * (number % 10)
        print('Сумма чисел: {}, Произведение чисел: {} '.format(summa, multiplication))
    else:
        print('Число не трехзначное')
else:
    print('Число меньше либо равно  0')


