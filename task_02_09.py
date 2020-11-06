# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.


def sum_digit(a):
    result = 0
    if a.isdigit():
        for i in a:
            result += int(i)
    return result


if __name__ == '__main__':
    num = 1
    max_sum = 0
    num_max = 0
    while num != '0':
        num = input('Введите натуральное число или ноль для завершения программы:')
        s = sum_digit(num)
        if s >= max_sum:
            max_sum = s
            num_max = num
    if max_sum != 0:
        print(f'Максимальная сумма цифр {max_sum} в числе {num_max}')
    else:
        print('Не введено ни одного натурального числа')
