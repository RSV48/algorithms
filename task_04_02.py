# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена». Второй — без использования «Решета Эратосфена».

import timeit
import cProfile


def sEratosfen(n):
    k = n * 10
    sieve = [i for i in range(k)]
    sieve[1] = 0
    for i in range(2, k):
        if sieve[i] != 0:
            j = i + i
            while j < k:
                sieve[j] = 0
                j += i
    result = [item for item in sieve if item != 0]
    if len(result) >= n:
        return result[n - 1]
    else:
        return sEratosfen(k)


def primeNum(n):
    i = 0
    x = 2
    while i < n:
        result = 0
        for j in range(2, n + 1):
            if j != x and x % j == 0:
                result = 1
        i += 1 if result == 0 else 0
        x += 1
    return x - 1


# print(sEratosfen(1000))
# print(primeNum(1000))


print(f'{"*" * 25} timeit {"*" * 25}')
print('№  Размер    sEratosfen      primeNum')
n = 1
for item in range(100, 1001, 100):
    print(f'{n} {item:>4}'
          f'{timeit.timeit("sEratosfen(item)", number=50, globals=globals()):>15.5f} '
          f'{timeit.timeit("primeNum(item)", number=50, globals=globals()):>15.5f} ')
    n += 1

# ************************* timeit *************************
# №  Размер    sEratosfen      primeNum
# 1  100        0.01131         0.14907
# 2  200        0.02446         0.66438
# 3  300        0.03524         1.65242
# 4  400        0.04732         3.15437
# 5  500        0.06046         5.16078
# 6  600        0.07051         7.82331
# 7  700        0.08475        11.11101
# 8  800        0.09533        15.08325
# 9  900        0.11677        20.24360
# 10 1000        0.12299        24.64543

print(f'{"*" * 25} sEratosfen {"*" * 25}')
for item in [100, 500, 1000]:
    cProfile.run('sEratosfen(item)')
# ************************* sEratosfen *************************
#          7 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:19(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:9(sEratosfen)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          7 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:19(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_04_02.py:9(sEratosfen)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          7 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_04_02.py:19(<listcomp>)
#         1    0.002    0.002    0.002    0.002 task_04_02.py:9(sEratosfen)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(f'{"*" * 25} primeNum {"*" * 25}')
for item in [100, 500, 1000]:
    cProfile.run('primeNum(item)')

# ************************* primeNum *************************
#          4 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task_04_02.py:26(primeNum)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.102 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.102    0.102 <string>:1(<module>)
#         1    0.102    0.102    0.102    0.102 task_04_02.py:26(primeNum)
#         1    0.000    0.000    0.102    0.102 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.515 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.515    0.515 <string>:1(<module>)
#         1    0.515    0.515    0.515    0.515 task_04_02.py:26(primeNum)
#         1    0.000    0.000    0.515    0.515 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ****************************** ВЫВОД ******************************

# Проведено тестирвоание двух алгоримов по расчету n-го простого числа.
#
# Первый алгорим "Решето Эратосфена" (sEratosfen).На основе замеров timeit можно сказать
# асимптотика алгорима O(n). Оценка cProfile не выявила явных слабых мест.
#
# Второй алгорим primeNum основан на последовательной проверке каждого числа на принадленость к простому. На основе
# замеров timeit можно сказать, что асимпотика алгоритма O(n**2). Оценка cProfile показала, что функция primeNum
# является слабым местом алгоритма.


