# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def cd(d, n):
    r = 0
    for j in n:
        if j == d:
            r += 1
    return r


if __name__ == '__main__':
    result = 0
    i = 0
    digit = input('Введите искомую цифру: ')
    count = int(input('Введи количество чисел: '))
    while i < count:
        num = input(f'Введи {i+1} число: ')
        result += cd(digit, num)
        i += 1
    print(f'Количество повторений цифры {digit}: {result}')