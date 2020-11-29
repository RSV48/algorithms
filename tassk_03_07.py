# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(0, SIZE)]

set_array = {item: 0 for item in array}
md1 = array[0]
md2 = array[0]
for key in array:
    set_array[key] += 1
    md1 = (key if key < md1 else md1)
    md2 = (key if md1 < key < md2 else md2)


print(f'Массив случайных целых чисел до изменения \n{array}')
print(f'{"*"*50}')
print(f'В массиве {set_array[md1]} минимальных элемента {md1}' if set_array[md1] > 1
      else f'Два минимальных элемента массива: {md1} и {md2}')


