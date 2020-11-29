# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]
# частный случай [93, 46, -85, -76, 1, -62, -90, 84, 86, -88]
# позиция минмального элемента больше позции максимального элемента
min_digit = array[0]
max_digit = array[0]
max_el = 0
min_el = 0
result = 0

print(f'Массив случайных целых чисел до изменения \n{array}')
for i, item in enumerate(array):
    max_digit = (item if item > max_digit else max_digit)
    min_digit = (item if item < min_digit else min_digit)
    max_el = (i if max_digit == item else max_el)
    min_el = (i if min_digit == item else min_el)

step = 1 if min_el < max_el else -1  # учитываем последовательность перебора элементов массива для частного случая

for i in range(min_el + step, max_el, step):
    result += array[i]
print(f'{"*"*50}')
print(f'Сумма чисел между элементами {min_el if step ==1 else max_el} и '
      f'{max_el if step ==1 else min_el} равна {result}')
