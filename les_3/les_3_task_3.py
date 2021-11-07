
"""
3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random


def list_(size, min_item, max_item) -> list:
    return [random.randint(min_item, max_item) for _ in range(size)]


mylist = list_(10, 1, 100)
print(mylist)

count_min = mylist[0]
count_max = mylist[0]

for i in mylist:
    if i < count_min:
        count_min = i

for i in mylist:
    if i > count_max:
        count_max = i

print(f' минимум: {count_min}, максимум: {count_max}')


indmin = mylist.index(count_min)
indmax = mylist.index(count_max)

mylist.insert(indmin, count_max)
mylist.pop(indmin + 1)

mylist.insert(indmax, count_min)
mylist.pop(indmax + 1)

print(mylist)




