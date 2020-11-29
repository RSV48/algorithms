# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

low_limit, up_limit = input('Для генерации случайного целого, вещественного числа или буквы от a до z, \n'
                            'верхний и нижний предел (наприме: 0 10): ').split()

if low_limit.isdigit() and up_limit.isdigit():
    result = random.randint(int(low_limit), int(up_limit))
elif low_limit.replace('.', '', 1).isdigit() and up_limit.replace('.', '', 1).isdigit():
    result = random.uniform(float(low_limit), float(up_limit))
elif low_limit.isalpha() and up_limit.isalpha():
    result = chr(random.randint(ord(low_limit), ord(up_limit)))
else:
    result = None
    print('Диапазон не определен!!! Верхня и нижняя границы должны быть одного типа.')
if result:
    print(f'Случайное значение в диапазоне от {low_limit} до {up_limit}: {result}')
