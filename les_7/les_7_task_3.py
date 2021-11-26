"""
3).     Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
    медианы, в другой — не больше медианы.
        Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
    используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""


import random


def My_list(n=100):
    n_start, n_end = 1,  2
    rand = random.randint(n_start, n)
    return [random.randint(n_start, rand) for _ in range(n_start, n_end*rand)]


def Mediana(array):
    middle = len(array) // 2
    left_ = array[:middle]
    # array_copy = array.copy()
    if len(array) > 2:
        n = 0
        for i in array:
            for c in array:
                if i < c:
                    n += 1
            # print(i, n, len(left_), n - len(left_))
            if -1 <= n - len(left_) <= 1:
                # print(i)
                return f'Медиана: {i}'
                break
            n = 0
    else:
        return 'Список состоит из одного элемента'



array = My_list(30)


print(array)
print(Mediana(array))

print( '\n', '-'*200)
print( sorted(array))

