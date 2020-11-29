# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

M = 5
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, 2 * M + 1)]

min_diff = len(arr)-1

for i in range(len(arr)):
    pos_min = 0
    pos_max = 0

    for j in range(len(arr)):

        pos_min += 1 if arr[i] >= arr[j] else 0
        pos_max += 1 if arr[i] <= arr[j] else 0

    if min_diff > abs(pos_max - pos_min):

        min_diff = abs(pos_max - pos_min)
        median_idx = i

median = arr[median_idx]

print(f'Медиана массива: \n{arr} \nРавна: {median}')

print(f'{"*"*50}\nПроверка:\n {sorted(arr)[len(arr) // 2]}')
print(sorted(arr))

