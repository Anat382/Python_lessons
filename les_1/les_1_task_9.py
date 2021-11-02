"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
https://drive.google.com/file/d/1Jj1mSL0hqVAIcZt_FKijFNLEo7idMwxA/view?usp=sharing


"""

number1 = int(input('Введите целое число :\t'))
number2 = int(input('Введите целое число :\t'))
number3 = int(input('Введите целое число :\t'))

if number2 < number1 < number3:
    result = number1
if number3 < number1 < number2:
    result = number1
if number1 < number2 < number3:
    result = number2
if number3 < number2 < number1:
    result = number2
if number1 < number3 < number2:
    result = number3
if number2 < number3 < number1:
    result = number3

print(result)

