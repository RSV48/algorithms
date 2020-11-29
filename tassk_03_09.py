# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
MIN_ITEM = 0
MAX_ITEM = 1000
LINE = 10
COLUMN = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for j in range(COLUMN)] for i in range(LINE)]
min_column = matrix[0]

print(f'Матрица случайных элементов\n{"*"*50}')
for line in matrix:
    for j, el in enumerate(line):
        min_column[j] = el if el < min_column[j] else min_column[j]
        print(f'{el:>5}', end='')
    print()

print(f'{"*"*50}\n Минимальные значения столбцов:')
max_el = min_column[0]
for el in min_column:
    max_el = el if el > max_el else max_el
    print(f'{el:>5}', end='')
print()
print(f'{"*"*50}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_el}')

