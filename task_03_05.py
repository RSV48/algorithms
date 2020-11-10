# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(0, SIZE)]

if [j for j in array if j < 0]:
    md = array[0]
    pos = 0
    for i, item in enumerate(array):
        md = item if (item < md >= 0) or (md < item < 0) else md
        pos = i if md == item else pos
    print(f'Массив значений:\n {array}')
    print(f'{"*" * 50}')
    print(f'Максимальный отрицательный элемент массива {md} в позиции {pos}')
else:
    print('Массив не содержит отрицательных элементов')


