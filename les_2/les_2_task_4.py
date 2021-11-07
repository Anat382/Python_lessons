"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def sum(number):
    exit_ = float(input('Для завершения ввода введите 0, для продожения введите число: '))
    if exit_ == 0:
        number
    else:
        number = sum(number + exit_)
    return number


num = float(input('Введите число: '))

res = sum(num)

print(res)

