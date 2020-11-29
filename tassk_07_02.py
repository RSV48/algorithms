# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random

SIZE = 10
MAX_ITEM = 50
array_no_sort = [random.random() * MAX_ITEM for _ in range(0, SIZE)]


def selection_sort(arr, ascending_sort=True):
    len_arr = len(arr)
    for i in range(len_arr):
        idx = i
        for j in range(i + 1, len_arr):
            if ascending_sort:
                if arr[j] < arr[idx]:
                    idx = j
            else:
                if arr[j] > arr[idx]:
                    idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    return arr


def merge_sort(array, ascending_sort=True):
    len_array = len(array)
    if len_array > 2:
        array = merge_sort(array[:len_array // 2]) + merge_sort(array[len_array // 2:])
    selection_sort(array, ascending_sort)
    return array


print(f'{"*"*15} Массив до сортировки {"*"*15}\n{array_no_sort}')
array_no_sort = merge_sort(array_no_sort)
print(f'{"*"*7} Массив после сортировки по возрастанию {"*"*7}\n{array_no_sort}')

