"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
 в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""


number = str(input('Введите целое число: '))
even = ''
neven = ''
denum = 2

for elem in number:
    if int(elem) > 0:
        if int(elem) % denum == 0:
            even += elem + ', '
        else:
            neven += elem + ', '
    else:
        print('Не введено число')

print(f' Чётные числа: {even} \n Не чётные числа: {neven}')