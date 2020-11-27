# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и
# строку целиком. Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib


def count_substring(string):
    len_str = len(string)
    result = set()

    for i in range(0, len_str):
        for j in range(i, len_str + i):
            if string[i:j] == '':
                continue
            result.add(hashlib.sha256(string[i:j].encode('utf-8')).hexdigest())
    return len(result)


str_g = input('Введите строку для анализа:')

print(f'{count_substring(str_g)} - подстрок в строке: {str_g}')
