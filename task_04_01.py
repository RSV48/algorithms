# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков. Примечание. Идеальным решением будет: ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть), ● проанализировать 3 варианта и выбрать оптимальный, ● результаты
# анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import random
import cProfile
import timeit

# Формируем статчиный массив даных в формате матрицы 1000х1000
LINE = 100
COLUMN = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array_static = []
for i in range(LINE):
    array_static.append([random.randint(MIN_ITEM, MAX_ITEM) for j in range(COLUMN)])


# Функция для получения матрицы заданного размера из ранее сформированного массива данных
def arrayMatrix(num, array):
    result_matrix = []
    for i in range(0, num):
        result_matrix.append([array[i][j] for j in range(0, num)])
    return result_matrix


# ВАРИАНТ 1 FOR IN

def mForIn(num, array):
    matrix = arrayMatrix(num, array)
    min_column = matrix[0]
    for line in matrix:
        for j, el in enumerate(line):
            min_column[j] = el if el < min_column[j] else min_column[j]
    max_el = min_column[0]
    for el in min_column:
        max_el = el if el > max_el else max_el
    return max_el


# ВАРИАНТ 2 WHILE

def mWhile(num, array):
    matrix = arrayMatrix(num, array)
    max_el = None
    j = 0
    while j < len(matrix[0]):
        min_el = matrix[0][j]
        i = 0
        while i < len(matrix):
            min_el = matrix[i][j] if matrix[i][j] < min_el else min_el
            i += 1
        if max_el is None or max_el < min_el:
            max_el = min_el
        j += 1
    return max_el


# ВАРИАНТ 3 встроенные функции min max

def mMinMax(num, array):
    matrix = arrayMatrix(num, array)
    min_el = []
    for i in range(len(matrix[0])):
        min_el.append(min([line[i] for line in matrix]))
    return max(min_el)


# print(mForIn(10, array_static))
# print(mWhile(10, array_static))
# print(mMinMax(10, array_static))

print(f'{"*" * 25} timeit {"*" * 25}')
print('№  Размер     mForIn    mWhile    mMinMax')
n = 1
for item in range(10, 101, 10):
    print(f'{n}{item:>4}х{item:<8}'
          f'{timeit.timeit("mForIn(item,array_static)", number=5000, globals=globals()):<4.5f} '
          f'  {timeit.timeit("mWhile(item,array_static)", number=5000, globals=globals()):4.5f} '
          f'  {timeit.timeit("mMinMax(item,array_static)", number=5000, globals=globals()):4.5f}')
    n += 1

# ************************* timeit *************************
# №  Размер     mForIn    mWhile    mMinMax
# 1  10х10      0.12394   0.12438   0.09979
# 2  20х20      0.32623   0.38974   0.28550
# 3  30х30      0.67279   0.79695   0.56047
# 4  40х40      1.14488   1.37481   0.95370
# 5  50х50      1.73530   2.08068   1.39144
# 6  60х60      2.48590   2.97586   2.00359
# 7  70х70      3.33205   3.97673   2.62665
# 8  80х80      4.32258   5.19030   3.49778
# 9  90х90      5.47613   6.53047   4.41871
# 10 100х100     6.72096   8.03496   5.39745

print(f'{"*" * 25} mForIn {"*" * 25}')
for item in [10, 50, 100]:
    cProfile.run('mForIn(item, array_static)')
# ************************* mForIn *************************
#          25 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        10    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:28(mForIn)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          105 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        50    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:28(mForIn)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          205 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 task_04_01.py:21(arrayMatrix)
#       100    0.001    0.000    0.001    0.000 task_04_01.py:24(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_04_01.py:28(mForIn)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(f'{"*" * 25} mWhile {"*" * 25}')
for item in [10, 50, 100]:
    cProfile.run('mWhile(item, array_static)')

# ************************* mWhile *************************
# 146 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        10    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:40(mWhile)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       121    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          2706 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        50    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.001    0.001 task_04_01.py:40(mWhile)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      2601    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          10406 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 task_04_01.py:21(arrayMatrix)
#       100    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.002    0.002    0.003    0.003 task_04_01.py:40(mWhile)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#     10201    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(f'{"*" * 25} mMinMax {"*" * 25}')
for item in [10, 50, 100]:
    cProfile.run('mMinMax(item, array_static)')

# ************************* mMinMax *************************
#          57 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        10    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:56(mMinMax)
#        10    0.000    0.000    0.000    0.000 task_04_01.py:60(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          257 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:21(arrayMatrix)
#        50    0.000    0.000    0.000    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_01.py:56(mMinMax)
#        50    0.000    0.000    0.000    0.000 task_04_01.py:60(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#        50    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          507 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 task_04_01.py:21(arrayMatrix)
#       100    0.001    0.000    0.001    0.000 task_04_01.py:24(<listcomp>)
#         1    0.000    0.000    0.001    0.001 task_04_01.py:56(mMinMax)
#       100    0.000    0.000    0.000    0.000 task_04_01.py:60(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#       200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ****************************** ВЫВОД **************************************
# Проведена оценка трех алгоримоов по расчету макмимального значения из минимальных значений столбцов матрицы.

# В первом алгориме использован цикл for in и для поиска значения алгоритм проверяет каждое значение матрицы один раз
# с использованием if else, соотвественно асимптотика алгоритма O(n), что подтвредается замерами timeit. Оценка
# cProfile слабых мест в алгоритме не показала.

# Во втором алгоритме использован цикл while и для поиска значения алгоритм проверяет каждое значение матрицы один
# раз c использованием if else, соответственно асимптотика алгоритма О(n), что также подтверждается замерами timeit.
# Оценка cProfile слабых мест в алгоритме не показала. При это наблюдается увеличеное, по отношению к другим
# алгоритмам, количество вызовов функции. Данный факт обясняется использованием цикла while, в котором каждый новый
# шаг вычисляется длинна массива, что приводит к увеличению времени работы алгоритма.

# В третьем алгоритме использован цикл for in и для поиска значения алгоритм проверяет каждое значение матрицы один раз,
# соответственно асимптотика алгорима О(n), что также потверждается замерами timeit. Оценка cProfile слабых мест в
# алгоритме не показала. При этом количество вызовов функции минимально, по отношению к двум другим алгоритмам, что
# объясняется использованием скомпилированных встроеных функций min max.

# Таким образом, наиболее эффективный алгоритм по скорости работы и количеству вызовов функции - mMinMax,
# использующий цикл for in и втсроенные функции min max.
