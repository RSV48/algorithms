# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


def func_rec(n, x=1):
    if n == 1:
        return x
    else:
        return x + func_rec(n - 1, -x / 2)


def func_cycle(n, x=1):
    y = 0
    for i in range(1, n + 1):
        y += x
        x = - x / 2
    return y


if __name__ == '__main__':
    count = int(input('Ведите количество элементом (целое положительное число): '))
    print(f'Рекурсия: {func_rec(count)}')
    print(f'Цикл: {func_cycle(count)}')
