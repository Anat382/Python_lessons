"""
4.Определить, какое число в массиве встречается чаще всего.
"""

import random


def list_(size, min_item, max_item) -> list:
    list_rand = [random.randint(min_item, max_item) for _ in range(size)]
    [list_rand.append(list_rand[random.randint(2, size)-1]) for elem1 in range(random.randint(1, size))]
    [list_rand.append(list_rand[random.randint(2, size)-1]) for elem2 in range(random.randint(1, size))]
    return list_rand


mylist = list_(10, 2, 10)
print(mylist)

count = 0
count_list = []
for i in mylist:
    for n in mylist:
        if i == n:
            count += 1
    count_list.append(count)
    count = 0

print(count_list)
# print(len(count_list), len(mylist))

ind_0 = count_list[0]
for i in count_list:
    if i > ind_0:
        ind_0 = i


print(ind_0)
print('-----------')

ind_n = 0
for i in range(len(count_list)):
    if count_list[i] == ind_0:
        ind_n = i
        break

print('-----------')
print(f'Число: {mylist[ind_n]} встречается чаще всего')
# print(f'Число: {mylist[count_list.index(ind_0)]} встречается чаще всего')
