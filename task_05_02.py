# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’].

# Немного расширил условие задачи: программа примает не ограниченное количество чисел и производит их сложение или
# умноедение

from collections import deque


def sum_table(digit_one, digit_two, rem=0):
    """Функция принимает массив с двумя цифрами шестнадцатитричной шкалы и выдет их сумму в виде массива.
    Альтернативный вариант использовать готовую таблицу с резултатми сложения цифр """
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    len_digit = len(digit)
    sum_index = digit[digit_one] + digit[digit_two] + rem
    rem_result = sum_index // len_digit
    d_result = sum_index - rem_result * len_digit
    digit_k = None
    rem_k = None
    for k, item in digit.items():
        rem_k = k if rem_result == item else rem_k
        digit_k = k if d_result == item else digit_k
    if rem_result != 0:
        return [rem_k, digit_k]
    else:
        return [digit_k]


def summation(array):
    """Функция принимает массив
    [[‘A’,‘2’] и [‘C’, ‘4’, ‘F’]]
    шестнадцатитеричных числе и выдет их сумму в виде массива аналогичного формата"""
    rem = 0
    result = deque()
    max_len_num = len(array[0])
    num = deque()
    for item in array:
        max_len_num = len(item) if max_len_num < len(item) else max_len_num
    for i in range(0, len(array)):
        a = ['0' for _ in range(abs(len(array[i]) - max_len_num))]
        a.extend(array[i])
        num.append(a)
    num1 = num.popleft()
    num2 = num.popleft()
    for i in range(max_len_num - 1, -1, -1):
        i_result = sum_table(num1[i], num2[i], rem)
        if len(i_result) == 2:
            result.appendleft(i_result[1])
            rem = int(i_result[0])
        else:
            result.appendleft(i_result[0])
            rem = 0
    if rem == 1:
        result.appendleft(str(rem))
    if len(num) >= 1:
        num.appendleft(result)
        return summation(num)
    else:
        return result


def multiply_table(digit_one, digit_two, rem=0):
    """Функция принимает двe шестнадцатитричные цифры  выдет их сумму в виде массива.
    Альтерниатвный вартант использовать готовую таблицу умножения"""
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    len_digit = len(digit)
    sum_index = digit[digit_one] * digit[digit_two] + rem
    rem_result = sum_index // len_digit
    d_result = sum_index - rem_result * len_digit
    digit_k = None
    rem_k = None
    for k, item in digit.items():
        rem_k = k if rem_result == item else rem_k
        digit_k = k if d_result == item else digit_k
    if rem_result != 0:
        return [rem_k, digit_k]
    else:
        return [digit_k]


def multiply(array):
    """Функция принимает массив [[‘A’,‘2’] и [‘C’, ‘4’, ‘F’]] шестнадцатитеричных числе и выдет их произведение в
    виде массива """
    num = deque()
    for i in range(0, len(array)):
        a = deque(array[i])
        num.append(a)
    num1 = num.popleft()
    num2 = num.popleft()
    if len(num2) < len(num1):
        num1, num2 = num2, num1
    result = deque()
    place_1 = deque()
    for i in range(len(num1) - 1, -1, -1):
        line = deque()
        place_2 = deque()
        for j in range(len(num2) - 1, -1, -1):
            line.append(deque(multiply_table(num1[i], num2[j])))
            line[len(place_2)].extend(place_2)
            place_2.append('0')
        if len(line) > 1:
            result.append(summation(line))
        else:
            result.append(line[0])
        result[len(place_1)].extend(place_1)
        place_1.append('0')
    if len(num) >= 1:
        if len(result) > 1:
            num.appendleft(summation(result))
        else:
            num.appendleft(result[0])
        return multiply(num)
    else:
        if len(result) > 1:
            return summation(result)
        else:
            return result[0]


def check(string):
    flag = True
    if string == '':
        print(f'Введено не корректное число {string}')
        flag = False
        return flag
    for j in string.upper():
        if j not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'):
            print(f'Введена не корретная цифра {j}')
            flag = False
    return flag


if __name__ == '__main__':
    while True:
        z = input('Ведите знак операции (+, *) или # для завершения программы: ')
        if z == '#':
            break
        elif z in ('+', '*'):
            array_num = []
            i = 1
            while True:
                rec = input(f'Введите {i}-е шестнадцатитеричное число \n'
                            f'или введите # для завершения ввода чисел:')
                flag = 0
                if rec != '#':
                    if check(rec):
                        array_num.append(rec.upper())
                        i += 1
                else:
                    break
            if len(array_num) < 2:
                print('Введено мало аргументов. Минимальное число аргументов два')
            elif z == '+':
                operation = 'Сумма'
                result = summation(array_num)
                print(' + '.join(array_num), '=', ''.join(result), sep=' ')
            else:
                result = multiply(array_num)
                print(' * '.join(array_num), '=', ''.join(result), sep=' ')
        else:
            print('Введена не корректная операция')
    print('Программа завершена')
