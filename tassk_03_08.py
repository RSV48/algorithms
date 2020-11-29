# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

# import random
# MIN_ITEM = -10
# MAX_ITEM = 10
# matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for j in range(0, 3)] for i in range(0, 5)]

matrix = [[int(input(f'Введите {j + 1} элемент (целое число) '
                     f'{i + 1}-й строки матрицы: ')) for j in range(0, 3)] for i in range(0, 5)]
print(f'{"*"*50}')
for i, line in enumerate(matrix):
    s = 0
    for y in line:
        s += y
        print(f'{y:>8}', end='')
    matrix[i] += [s]
    print(f'{s:>8}')
