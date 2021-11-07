"""
7.В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться
"""


import random


def list_(size, min_item, max_item) -> list:
    return [random.randint(min_item, max_item) for _ in range(size)]


mylist = list_(20, -5, 50)
print(mylist)

min1 = mylist[0]
for i in mylist:
    if i < min1 and i != 0:
        min1 = i

mylist.remove(min1)
# print(mylist)

min2 = mylist[0]
for i in mylist:
    if i < min2 and i != 0:
        min2 = i

print(f'Два наименьших элемента исключая 0: {min1}, {min2}')