"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

lsmin = 2
lsmax = 99

rangmin = 2
rangmax = 9

count = 0

dict_ = dict()
for i in range(rangmin, rangmax + 1):
    for n in range(lsmin, lsmax + 1):
        if n % i == 0:
            count += 1
    dict_[i] = count
    count = 0
print(dict_)

