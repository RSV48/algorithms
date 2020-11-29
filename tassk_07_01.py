# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные
# версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array_no_sort = [random.randint(MIN_ITEM, MAX_ITEM-1) for _ in range(0, SIZE)]


def bubble_sort(array, ascending_sort=True):
    """Функция принмает массив числе и производит его сортировку методом пузирьков
        по умолчанию ascending_sort=True сортировка производится по возрастанию
        ascending_sort=False сортировка производится по убыванию
    """
    len_array = len(array)
    for n in range(1, len_array):

        for i in range(len_array - n):
            if ascending_sort:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            else:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(f'{"*"*15} Массив до сортировки {"*"*15}\n{array_no_sort}')
bubble_sort(array_no_sort, False)
print(f'{"*"*7} Массив после сортировки по убыванию {"*"*7}\n{array_no_sort}')

