"""
2.Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,второй массив надо заполнить значениями 0, 3, 4, 5,
 (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random


def list_(size, min_item, max_item) -> list:
    return [random.randint(min_item, max_item) for _ in range(size)]


list1 = list_(10, 1, 100)
list2 = list_(10, 1, 100)
print(f'{list1} \n{list2}')

for i in list1:
    if i % 2 == 0:
        list2.insert(list1.index(i), i)

print(list2)