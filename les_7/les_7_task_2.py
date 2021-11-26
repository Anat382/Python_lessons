"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, з
аданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

def My_list(n_start, n_end):
    return [random.randint(n_start, n_end) for _ in range(n_start, n_end)]


def Merge_to_list(l, r):
    list_ = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            list_.append(l[i])
            i += 1
        else:
            list_.append(r[j])
            j += 1
    if i < len(l):
        list_ += l[i:]
    if j < len(r):
        list_ += r[j:]
    return list_


def Merge_sort(array):
    array_sort = array.copy()
    if len(array_sort) == 1:
        return array_sort
    middle = len(array_sort) // 2
    left_ = Merge_sort(array_sort[:middle])
    rigth_ = Merge_sort(array_sort[middle:])
    return Merge_to_list(left_, rigth_)


n_start = 0
n_end = 50

array = My_list(n_start, n_end)

print(array)
print(Merge_sort(array))
