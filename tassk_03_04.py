# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]
set_array = {item: 0 for item in array}
max_count = 0

for key in array:
    set_array[key] += 1
    max_count = (set_array[key] if set_array[key] > max_count else max_count)

print(array)
print('*' * 50)
# Выводим все элементы массива имеющие максимальное количество повторений
print(f'Максимальное число повторений {max_count} у следующих чисел:\n'
      f'{[key for key, item in set_array.items() if item == max_count]}')
