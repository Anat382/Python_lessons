"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
    на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
    Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""
import random
import sys
import inspect
import timeit
import cProfile


def My_list(n_start, n_end):
    return [random.randint(n_start, n_end) for _ in range(n_start, n_end)]


def Evualate_qulity_code(n_start, n_end, function_list=[], inc=1.5, n_test=10, inc_prof=10, n_test_prof=3):
    simb = "=" * 30
    print('\n\n\n ', simb + "=" * 20, 'Замеры', simb + "=" * 20)
    qty_size = n_end
    qty_end = qty_size
    timeit_number = 1000

    n_start_prof = qty_size  # * 10
    n_end_prof = n_start_prof

    n = 0
    for funk in function_list:
        n += 1
        print(f'\n\n {simb + "=" * 10} Оценка времени: Решение {n} - {funk} {simb + "=" * 10} \n ')
        for t in range(1, n_test + 1):
            list_test = My_list(n_start, int(qty_size))
            print(f'Замер {t}: размер списка {len(list_test)}, время выполнения кода',
                  timeit.timeit(f'{funk}({list_test}, 0)', number=timeit_number, globals=globals()))
            qty_size *= inc
        qty_size = qty_end

    n = 0
    for funk in function_list:
        n += 1
        print(f'\n\n {simb + "=" * 10} Profile: Решение {n} - {funk} {simb + "=" * 10} \n ')
        for t in range(1, n_test_prof + 1):
            list_test = My_list(n_start, int(n_start_prof))
            print(f'\n {simb} Замер: {t} : размер списка {len(list_test)} {simb} \n')
            cProfile.run(f'{funk}({list_test}, 0)')
            n_start_prof *= inc_prof
        n_start_prof = n_end_prof


def My_getsizeof(*args):
    count = 0
    for elem in args:
        count += sys.getsizeof(elem)
    caller_locals = inspect.currentframe().f_back.f_locals
    variable_funk = [name for name in caller_locals.keys()]
    return print(f' Используемые переменные: {variable_funk} \n Кол-во переменных: {len(args)}'
                 f' \n Расходовано памяти(байт): {count}')


def Buble(array, print_=0):
    array_sort = array.copy()
    n = 1
    while n < len(array_sort):
        for i in range(len(array_sort) - n):
            if array_sort[i] < array_sort[i + 1]:
                array_sort[i], array_sort[i + 1] = array_sort[i + 1], array_sort[i]
        n += 1
        # print(array_sort) if print_ == 1 else None

    My_getsizeof(array_sort, n, i) if print_ == 1 else None
    return array_sort


# решение с развбора урока 8
def bubble_sort(array,  print_=0):
    reverse = True
    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] * sign < array[i + 1] * sign:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1
        # print(array) if print_ == 1 else None

    My_getsizeof(array, reverse, print_, sign, n, is_sorted, i) if print_ == 1 else None
    return array


functions = ['Buble', 'bubble_sort']

n_start = -100
n_end = 100

array = My_list(n_start, n_end)

print(array)
print('------- START ------ \n ')

print(Buble(array, 1))
print('\n -------------')
print(bubble_sort(array, print_=1))

Evualate_qulity_code(n_start, n_end, function_list=functions, inc=1.3, n_test=7, inc_prof=10, n_test_prof=3)


"""
решение 1 потребляеет меньше памяти и времени 

[-39, -24, 18, 42, -81, -39, -28, 51, -40, 60, 19, 13, 70, 6, 52, -52, 1, -64, 27, -62, 33, 68, 56, -86, 16, -80, -50, -98, 82, 91, 72, 91, 31, 64, -27, -3, 48, 63, -84, -49, -33, 78, -17, 69, 98, 22, -26, 69, 31, -43, -99, -24, 89, 62, 60, -80, 89, -68, -80, 49, -40, 81, 79, -71, -31, 45, 35, 5, -43, 16, 87, -18, -60, 15, -82, -70, 91, -62, -91, -43, 40, -80, 93, -32, 79, 20, -54, 37, 91, 85, -53, -91, -65, 77, 20, -62, 67, -40, -14, 79, -28, -60, 60, -75, 60, 58, -39, 62, -12, -22, -64, -80, 26, -53, 77, -21, 93, 82, 34, -14, 30, 21, -12, 31, -34, 57, -60, -51, 56, -40, 11, -31, 64, -61, -44, -37, -24, -86, -88, 49, 84, 29, -65, -15, 80, -62, -64, -60, 38, 6, -40, 3, 83, 19, 33, -44, 68, -44, -14, -72, -89, 56, 77, 53, -40, 31, -36, -39, -72, 27, -98, -83, -28, 49, 61, 100, 73, 53, -50, 78, 51, 96, 72, -94, -81, -78, -81, -23, 96, 0, 100, 68, -22, 80, -28, 0, -44, 48, -4, -29]
------- START ------ 
 
 Используемые переменные: ['array', 'print_', 'array_sort', 'n', 'i'] 
 Кол-во переменных: 3 
 Расходовано памяти(байт): 1708
[100, 100, 98, 96, 96, 93, 93, 91, 91, 91, 91, 89, 89, 87, 85, 84, 83, 82, 82, 81, 80, 80, 79, 79, 79, 78, 78, 77, 77, 77, 73, 72, 72, 70, 69, 69, 68, 68, 68, 67, 64, 64, 63, 62, 62, 61, 60, 60, 60, 60, 58, 57, 56, 56, 56, 53, 53, 52, 51, 51, 49, 49, 49, 48, 48, 45, 42, 40, 38, 37, 35, 34, 33, 33, 31, 31, 31, 31, 30, 29, 27, 27, 26, 22, 21, 20, 20, 19, 19, 18, 16, 16, 15, 13, 11, 6, 6, 5, 3, 1, 0, 0, -3, -4, -12, -12, -14, -14, -14, -15, -17, -18, -21, -22, -22, -23, -24, -24, -24, -26, -27, -28, -28, -28, -28, -29, -31, -31, -32, -33, -34, -36, -37, -39, -39, -39, -39, -40, -40, -40, -40, -40, -40, -43, -43, -43, -44, -44, -44, -44, -49, -50, -50, -51, -52, -53, -53, -54, -60, -60, -60, -60, -61, -62, -62, -62, -62, -64, -64, -64, -65, -65, -68, -70, -71, -72, -72, -75, -78, -80, -80, -80, -80, -80, -81, -81, -81, -82, -83, -84, -86, -86, -88, -89, -91, -91, -94, -98, -98, -99]

 -------------
 Используемые переменные: ['array', 'print_', 'reverse', 'sign', 'n', 'is_sorted', 'i'] 
 Кол-во переменных: 7 
 Расходовано памяти(байт): 1824
[100, 100, 98, 96, 96, 93, 93, 91, 91, 91, 91, 89, 89, 87, 85, 84, 83, 82, 82, 81, 80, 80, 79, 79, 79, 78, 78, 77, 77, 77, 73, 72, 72, 70, 69, 69, 68, 68, 68, 67, 64, 64, 63, 62, 62, 61, 60, 60, 60, 60, 58, 57, 56, 56, 56, 53, 53, 52, 51, 51, 49, 49, 49, 48, 48, 45, 42, 40, 38, 37, 35, 34, 33, 33, 31, 31, 31, 31, 30, 29, 27, 27, 26, 22, 21, 20, 20, 19, 19, 18, 16, 16, 15, 13, 11, 6, 6, 5, 3, 1, 0, 0, -3, -4, -12, -12, -14, -14, -14, -15, -17, -18, -21, -22, -22, -23, -24, -24, -24, -26, -27, -28, -28, -28, -28, -29, -31, -31, -32, -33, -34, -36, -37, -39, -39, -39, -39, -40, -40, -40, -40, -40, -40, -43, -43, -43, -44, -44, -44, -44, -49, -50, -50, -51, -52, -53, -53, -54, -60, -60, -60, -60, -61, -62, -62, -62, -62, -64, -64, -64, -65, -65, -68, -70, -71, -72, -72, -75, -78, -80, -80, -80, -80, -80, -81, -81, -81, -82, -83, -84, -86, -86, -88, -89, -91, -91, -94, -98, -98, -99]



  ================================================== Замеры ==================================================


 ======================================== Оценка времени: Решение 1 - Buble ======================================== 
 
Замер 1: размер списка 200, время выполнения кода 2.4195282
Замер 2: размер списка 230, время выполнения кода 3.347161
Замер 3: размер списка 269, время выполнения кода 4.4919213000000004
Замер 4: размер списка 319, время выполнения кода 6.531235100000002
Замер 5: размер списка 385, время выполнения кода 9.575510100000002
Замер 6: размер списка 471, время выполнения кода 14.703600699999996
Замер 7: размер списка 582, время выполнения кода 23.558489700000003


 ======================================== Оценка времени: Решение 2 - bubble_sort ======================================== 
 
Замер 1: размер списка 200, время выполнения кода 3.3123781999999977
Замер 2: размер списка 230, время выполнения кода 4.266379000000001
Замер 3: размер списка 269, время выполнения кода 5.7775694999999985
Замер 4: размер списка 319, время выполнения кода 8.352786600000002
Замер 5: размер списка 385, время выполнения кода 12.4901433
Замер 6: размер списка 471, время выполнения кода 19.212099699999996
Замер 7: размер списка 582, время выполнения кода 31.1538422


 ======================================== Profile: Решение 1 - Buble ======================================== 
 

 ============================== Замер: 1 : размер списка 200 ============================== 

         404 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 les_7_task_1.py:64(Buble)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
      399    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 : размер списка 1100 ============================== 

         2204 function calls in 0.088 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.086    0.086 <string>:1(<module>)
        1    0.086    0.086    0.086    0.086 les_7_task_1.py:64(Buble)
        1    0.002    0.002    0.088    0.088 {built-in method builtins.exec}
     2199    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 : размер списка 10100 ============================== 

         20204 function calls in 8.195 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.176    8.176 <string>:1(<module>)
        1    8.173    8.173    8.176    8.176 les_7_task_1.py:64(Buble)
        1    0.020    0.020    8.195    8.195 {built-in method builtins.exec}
    20199    0.002    0.000    0.002    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




 ======================================== Profile: Решение 2 - bubble_sort ======================================== 
 

 ============================== Замер: 1 : размер списка 200 ============================== 

         324 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.004    0.004    0.004    0.004 les_7_task_1.py:79(bubble_sort)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      320    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 : размер списка 1100 ============================== 

         2124 function calls in 0.122 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.120    0.120 <string>:1(<module>)
        1    0.120    0.120    0.120    0.120 les_7_task_1.py:79(bubble_sort)
        1    0.002    0.002    0.122    0.122 {built-in method builtins.exec}
     2120    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 : размер списка 10100 ============================== 

         19802 function calls in 10.862 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.842   10.842 <string>:1(<module>)
        1   10.840   10.840   10.842   10.842 les_7_task_1.py:79(bubble_sort)
        1    0.020    0.020   10.862   10.862 {built-in method builtins.exec}
    19798    0.002    0.000    0.002    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0


"""
