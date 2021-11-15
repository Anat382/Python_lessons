"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
    на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
    его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""

"""
0    1    2     3    4     5     6    7     8     9
10    11     12    13    ...
"""
import timeit
import cProfile

def Sieve1(n_size, show):
    sieve = [i for i in range(n_size)]
    sieve[1] = 0

    for i in range(2, n_size):
        if sieve[i] != 0:
            j = i + i
            while j < n_size:
                sieve[j] = 0
                j += i
    print(sieve) if show == 1 else None
    res = [i for i in sieve if i != 0]
    return res if show == 1 else None


def Sieve2(n_size, show):
    my_list = []
    n_count = 0
    n = 1
    for i in range(2, n_size):
        while n < n_size:
            if i % n == 0:
                n_count += 1
            n += 1
        n = 1
        if n_count == 2:
            my_list += [i]
        n_count = 0
    return my_list if show == 1 else None


def Sieve3(n_size, show):
    sieve = [i for i in range(n_size)]
    sieve[1] = 0
    n_count = 0
    for i in sieve:
        if i != 0:
            for n in range(2, n_size):
                if i % n == 0:
                    n_count += 1
            if n_count != 1:
                sieve[i] = 0
            n_count = 0
    return [i for i in sieve if i != 0] if show == 1 else None


num = int(input('До какого числа просеиваем: '))
simb = "=" * 30

n_start = num
n_end = n_start
inc = 1.5
n_test = 10
timeit_number = 1000

num_prof = num * 10
n_start_prof = num_prof
n_end_prof = n_start_prof
inc_prof = 100
n_test_prof = 3
sol = 4

print(f'\n {simb} Решение 1 {simb} ')
print(Sieve1(num, 1))
print(f'\n {simb} Решение 2 {simb} ')
print(Sieve2(num, 1))
print(f'\n {simb} Решение 3 {simb} ')
print(Sieve3(num, 1))

print('\n\n\n ', simb + "=" * 20, 'Замеры', simb + "=" * 20)


for n in range(1, sol):
    print(f'\n\n {simb + "=" * 10} Решение {n} {simb + "=" * 10} \n ')
    for t in range(1, n_test + 1):
        print(f'Замер {t}: размер списка {int(n_start)}, время выполнения кода',
              timeit.timeit(f'Sieve{n}({int(n_start)}, 0)', number=timeit_number, globals=globals()))
        n_start *= inc
    n_start = n_end


for n in range(1, sol):
    print(f'\n\n {simb + "=" * 10} Решение {n} {simb + "=" * 10} \n ')
    for t in range(1, n_test_prof + 1):
        print(f'\n {simb} Замер: {t} {simb} \n')
        cProfile.run(f'Sieve{n}({int(n_start_prof)}, 0)')
        n_start_prof *= inc
    n_start_prof = n_end_prof

# ============================================================================================================

"""

  ================================================== Замеры ==================================================
Выполнено 10 замеров по времени и 3 замера используя профайл для каждого решения

Решение 1 показало наилучшие результаты, за счёт того сто мало ветвлений и итерации выполняются отлько по одному списку,
    исключая нули, тем самым сокращая кол-во итераций

Третье решение отработало дольше так как больше ветвлений и больше вложенных итераций и опреаций сравнения

Второе решение отработоло хуже всего, помимо недостатков перечисленных в 3 решениии, создаётся новый список занимает
 память и время 

Рейтинг решений от лучшего к худшему:
    - решение 1
    - решение 3
    - решение 2
    
 ========================================= Решение 1 ======================================== 
 
Замер 1: размер списка 100, время выполнения кода 0.027225300000000008
Замер 2: размер списка 150, время выполнения кода 0.03536910000000004
Замер 3: размер списка 225, время выполнения кода 0.06055229999999989
Замер 4: размер списка 337, время выполнения кода 0.07894049999999986
Замер 5: размер списка 506, время выполнения кода 0.1256109000000003
Замер 6: размер списка 759, время выполнения кода 0.20110769999999967
Замер 7: размер списка 1139, время выполнения кода 0.2971265999999999
Замер 8: размер списка 1708, время выполнения кода 0.4791726999999999
Замер 9: размер списка 2562, время выполнения кода 0.6836769999999999
Замер 10: размер списка 3844, время выполнения кода 1.0832547000000003


 ======================================== Решение 2 ======================================== 
 
Замер 1: размер списка 100, время выполнения кода 0.7332225999999995
Замер 2: размер списка 150, время выполнения кода 1.6263002999999996
Замер 3: размер списка 225, время выполнения кода 3.7494143000000006
Замер 4: размер списка 337, время выполнения кода 8.492230600000001
Замер 5: размер списка 506, время выполнения кода 19.968618500000005
Замер 6: размер списка 759, время выполнения кода 46.641431499999996
Замер 7: размер списка 1139, время выполнения кода 108.6075745
Замер 8: размер списка 1708, время выполнения кода 250.4801567
Замер 9: размер списка 2562, время выполнения кода 576.3665065999999
Замер 10: размер списка 3844, время выполнения кода 1371.3541058


 ======================================== Решение 3 ======================================== 
 
Замер 1: размер списка 100, время выполнения кода 0.42746549999992567
Замер 2: размер списка 150, время выполнения кода 0.9604190000000017
Замер 3: размер списка 225, время выполнения кода 2.1361378999999943
Замер 4: размер списка 337, время выполнения кода 5.7140894000003755
Замер 5: размер списка 506, время выполнения кода 12.180830499999956
Замер 6: размер списка 759, время выполнения кода 28.776939299999867
Замер 7: размер списка 1139, время выполнения кода 69.22433060000003
Замер 8: размер списка 1708, время выполнения кода 163.0212219
Замер 9: размер списка 2562, время выполнения кода 376.6483291000004
Замер 10: размер списка 3844, время выполнения кода 883.6677316


 ======================================== Решение 1 ======================================== 
 

 ============================== Замер: 1 ============================== 

         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:30(Sieve1)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:31(<listcomp>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         6 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 les_4_task_2.py:30(Sieve1)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:31(<listcomp>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         6 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_2.py:30(Sieve1)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:31(<listcomp>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




 ======================================== Решение 2 ======================================== 
 

 ============================== Замер: 1 ============================== 

         4 function calls in 0.085 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.085    0.085 <string>:1(<module>)
        1    0.085    0.085    0.085    0.085 les_4_task_2.py:45(Sieve2)
        1    0.000    0.000    0.085    0.085 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         4 function calls in 0.198 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.198    0.198 <string>:1(<module>)
        1    0.198    0.198    0.198    0.198 les_4_task_2.py:45(Sieve2)
        1    0.000    0.000    0.198    0.198 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         4 function calls in 0.476 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.476    0.476 <string>:1(<module>)
        1    0.476    0.476    0.476    0.476 les_4_task_2.py:45(Sieve2)
        1    0.000    0.000    0.476    0.476 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




 ======================================== Решение 3 ======================================== 
 

 ============================== Замер: 1 ============================== 

         5 function calls in 0.049 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.049    0.049 <string>:1(<module>)
        1    0.049    0.049    0.049    0.049 les_4_task_2.py:61(Sieve3)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:62(<listcomp>)
        1    0.000    0.000    0.049    0.049 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 2 ============================== 

         5 function calls in 0.125 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.125    0.125 <string>:1(<module>)
        1    0.125    0.125    0.125    0.125 les_4_task_2.py:61(Sieve3)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:62(<listcomp>)
        1    0.000    0.000    0.125    0.125 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



 ============================== Замер: 3 ============================== 

         5 function calls in 0.273 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.273    0.273 <string>:1(<module>)
        1    0.273    0.273    0.273    0.273 les_4_task_2.py:61(Sieve3)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:62(<listcomp>)
        1    0.000    0.000    0.273    0.273 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0

            
"""