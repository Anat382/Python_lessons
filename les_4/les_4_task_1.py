"""
Для каждого упражнения написать программную реализацию.
Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо
    сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_4_task_1, les_4_task_2, и т.д.
Для оценки «Отлично» необходимо выполнить оба задания.
Результаты анализа сохранить в виде комментариев в файле с кодом.

1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

# Задача: Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile


def list_(size, min_item, max_item) -> list:
    list_rand = [random.randint(min_item, max_item) for _ in range(size)]
    [list_rand.append(list_rand[random.randint(2, size) - 1]) for _ in range(random.randint(1, size))]
    [list_rand.append(list_rand[random.randint(2, size) - 1]) for _ in range(random.randint(1, size))]
    return list_rand


# решение 1
def max_count_1(my_list, show):
    count = 0
    count_list = []
    print(my_list) if show == 1 else None
    for i in my_list:
        for n in my_list:
            if i == n:
                count += 1
        count_list.append(count)
        count = 0

    print(count_list) if show == 1 else None
    # print(len(count_list), len(my_list))

    ind_0 = count_list[0]
    for i in count_list:
        if i > ind_0:
            ind_0 = i

    # print(ind_0)

    ind_n = 0
    for i in range(len(count_list)):
        if count_list[i] == ind_0:
            ind_n = i
            break

    return (f'Число: {my_list[ind_n]} встречается чаще всего' \
                if ind_0 > 1 else 'Все элементы уникальны') if show == 1 else None


# решение 2
def max_count_2(my_list, show):
    count_list = []
    count = 0
    print(my_list) if show == 1 else None
    for i in my_list:
        # print(i)
        for n in my_list:
            if i == n:
                count += 1
        count_list.append(count)
        count = 0
        if len(count_list) == len(my_list):
            print(count_list) if show == 1 else None
            const = count_list[0]
            my_index = 0
            for ind, item in enumerate(count_list):
                if item > const:
                    const = item
                    if ind > my_index:
                        my_index = ind
            return (f'Число: {my_list[my_index]} встречается чаще всего'
                    if const > 1 else 'Все элементы уникальны') if show == 1 else None


# решение 3
def max_count_3(my_list, show) -> dict:
    my_dict = {}
    count = 0
    print(my_list) if show == 1 else None
    for i in set(my_list):
        for n in my_list:
            if i == n:
                count += 1
        my_dict[i] = count
        count = 0

    num_count = {}
    for num, cn in my_dict.items():
        if cn == max(my_dict.values()):
            num_count[num] = cn
    return num_count if show == 1 else None


# решение 4 изменение метода получения числа в конце функции
def max_count_4(my_list, show) -> str:
    my_dict = {}
    count = 0
    print(my_list) if show == 1 else None
    for i in set(my_list):
        for n in my_list:
            if i == n:
                count += 1
        my_dict[i] = count
        count = 0
        max_value = max(my_dict.values())
    return (f'Число {list(my_dict.keys())[list(my_dict.values()).index(max_value)]} ' \
           f'встречется {max_value} раз(а)' if max_value > 1 else 'Все элементы уникальны') if show == 1 else None


# решение 5 из разбора ДЗ
def max_count_5(my_list, show):
    num = my_list[0]
    frequency = 1
    print(my_list) if show == 1 else None
    for i in range(len(my_list)):
        spam = 1
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = my_list[i]

    return (f'Число {num} встречется {frequency} раз(а)' \
        if frequency > 1 else 'Все элементы уникальны') if show == 1 else None


size, min_item, max_item = 20, 2, 50
my_list = list_(size, min_item, max_item)
simb = "="*30

print('\n\n\n ', simb + "="*20, 'Замеры', simb + "="*20)
n_start = 20
n_end = n_start
inc = 1.5
n_test = 10
timeit_number = 1000


n_start_prof = n_start * 100
n_end_prof = n_start_prof
inc_prof = 1000
n_test_prof = 3

sol = 6


print(f'{simb} Решение 1 {simb} ')
print(max_count_1(my_list, 1))
print(f'{simb} Решение 2 {simb} ')
print(max_count_2(my_list, 1))
print(f'{simb} Решение 3 {simb} ')
print(max_count_3(my_list, 1))
print(f'{simb} Решение 4 {simb} ')
print(max_count_4(my_list, 1))
print(f'{simb} Решение 5 {simb} ')
print(max_count_5(my_list, 1))


for n in range(1, sol):
    print(f'\n\n {simb + "="*10} Решение {n} {simb + "="*10} \n ')
    for t in range(1, n_test + 1):
        my_list = list_(int(n_start), min_item, max_item)
        print(f'Замер {t}: размер списка {int(n_start)}, время выполнения кода',
              timeit.timeit(f'max_count_{n}(my_list, 0)', number=timeit_number, globals=globals()))
        n_start *= inc
    n_start = n_end


for n in range(1, sol):
    print(f'\n\n {simb + "=" * 10} Решение {n} {simb + "=" * 10} \n ')
    for t in range(1, n_test_prof + 1):
        print(f'\n {simb} Замер: {t} {simb} \n')
        my_list = list_(int(n_start), min_item, max_item)
        cProfile.run(f'max_count_{n}(my_list, 0)')
        n_start_prof *= inc_prof
    n_start_prof = n_end_prof

# ============================================================================================================

"""

  ================================================== Замеры ==================================================
Выполнено 10 замеров по времени и 3 замера используя профайл для каждого решения

Наихудшее второе решение, время увеличивается квадратично, большое кол-во вызова функций, основные проблемы
 вызваны функциями len и append, хуше всего влияет функция len
 
Наилучшее третье решение, время увеличивается линейно, наименьшее кол-во вызова функции, встроенная функция max имеет
 преимущество над циклом  

Решение 4 - иммет небольшое отстование от третьего, но создание списка и поиск индекса занимают больше памяти

Рейтинг решений от лучшего к худшему:
    - решение 3
    - решение 4
    - решение 5
    - решение 1
    - решение 2

 ============================== Решение 1 ============================== 
 
Замер 1: размер списка 20, время выполнения кода 0.045740699999999995
Замер 2: размер списка 30, время выполнения кода 0.046852099999999994
Замер 3: размер списка 45, время выполнения кода 0.1974472
Замер 4: размер списка 67, время выполнения кода 0.5360938
Замер 5: размер списка 101, время выполнения кода 1.0301677999999999
Замер 6: размер списка 151, время выполнения кода 1.0505955
Замер 7: размер списка 227, время выполнения кода 4.4787424
Замер 8: размер списка 341, время выполнения кода 7.8223302
Замер 9: размер списка 512, время выполнения кода 50.1381411
Замер 10: размер списка 768, время выполнения кода 89.1543144


 ============================== Решение 2 ============================== 
 
Замер 1: размер списка 20, время выполнения кода 0.04451270000001273
Замер 2: размер списка 30, время выполнения кода 0.06895689999998922
Замер 3: размер списка 45, время выполнения кода 0.3846728999999982
Замер 4: размер списка 67, время выполнения кода 0.8822676999999999
Замер 5: размер списка 101, время выполнения кода 1.061399399999999
Замер 6: размер списка 151, время выполнения кода 2.452645899999993
Замер 7: размер списка 227, время выполнения кода 6.516886399999976
Замер 8: размер списка 341, время выполнения кода 13.759047400000014
Замер 9: размер списка 512, время выполнения кода 21.261770000000013
Замер 10: размер списка 768, время выполнения кода 74.11134420000002


 ============================== Решение 3 ============================== 
 
Замер 1: размер списка 20, время выполнения кода 0.02566949999999224
Замер 2: размер списка 30, время выполнения кода 0.06766830000003665
Замер 3: размер списка 45, время выполнения кода 0.10999170000002323
Замер 4: размер списка 67, время выполнения кода 0.1669641000000297
Замер 5: размер списка 101, время выполнения кода 0.27168970000002446
Замер 6: размер списка 151, время выполнения кода 0.4252286000000254
Замер 7: размер списка 227, время выполнения кода 0.7144771000000105
Замер 8: размер списка 341, время выполнения кода 0.9666438999999514
Замер 9: размер списка 512, время выполнения кода 1.5495018999999957
Замер 10: размер списка 768, время выполнения кода 1.0950084000000402


 ============================== Решение 4 ============================== 
 
Замер 1: размер списка 20, время выполнения кода 0.023836299999970834
Замер 2: размер списка 30, время выполнения кода 0.05231539999999768
Замер 3: размер списка 45, время выполнения кода 0.0632085000000302
Замер 4: размер списка 67, время выполнения кода 0.1092251000000033
Замер 5: размер списка 101, время выполнения кода 0.25771950000000743
Замер 6: размер списка 151, время выполнения кода 0.3736814000000095
Замер 7: размер списка 227, время выполнения кода 0.5009233000000108
Замер 8: размер списка 341, время выполнения кода 0.9947766999999885
Замер 9: размер списка 512, время выполнения кода 1.4931581999999821
Замер 10: размер списка 768, время выполнения кода 1.5081802999999923


 ============================== Решение 5 ============================== 
 
Замер 1: размер списка 20, время выполнения кода 0.05345479999999725
Замер 2: размер списка 30, время выполнения кода 0.11474490000000515
Замер 3: размер списка 45, время выполнения кода 0.28860120000001643
Замер 4: размер списка 67, время выполнения кода 0.5476045999999997
Замер 5: размер списка 101, время выполнения кода 0.6934482000000344
Замер 6: размер списка 151, время выполнения кода 1.8906690000000026
Замер 7: размер списка 227, время выполнения кода 4.838314999999966
Замер 8: размер списка 341, время выполнения кода 19.299313600000005
Замер 9: размер списка 512, время выполнения кода 48.9495134
Замер 10: размер списка 768, время выполнения кода 30.35129919999997


 ============================== Решение 1 ============================== 
 

 ============================== Замер: 1 ============================== 

         40 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(max_count_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       35    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         70 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(max_count_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       65    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         90 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(max_count_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       85    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




 ============================== Решение 2 ============================== 
 

 ============================== Замер: 1 ============================== 

         166 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:65(max_count_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      108    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       54    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         136 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:65(max_count_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       88    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       44    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         379 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_1.py:65(max_count_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      250    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      125    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




 ============================== Решение 3 ============================== 
 

 ============================== Замер: 1 ============================== 

         35 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:90(max_count_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       15    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}



 ============================== Замер: 2 ============================== 

         47 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:90(max_count_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       21    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       21    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}



 ============================== Замер: 3 ============================== 

         61 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:90(max_count_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       28    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       28    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}




 ============================== Решение 4 ============================== 
 

 ============================== Замер: 1 ============================== 

         36 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:109(max_count_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       16    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       16    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}



 ============================== Замер: 2 ============================== 

         56 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:109(max_count_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       26    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       26    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}



 ============================== Замер: 3 ============================== 

         64 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:109(max_count_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       30    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       30    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}




 ============================== Решение 5 ============================== 
 

 ============================== Замер: 1 ============================== 

         42 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:125(max_count_5)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       38    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         73 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:125(max_count_5)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       69    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         122 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:125(max_count_5)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      118    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""