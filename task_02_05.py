#  Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#  Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def view_ascll(a, b):
    s = ''
    if a + 10 < b:
        for i in range(a, a + 10):
            s += str(i) + ' - "' + chr(i) + '" '
        print(s)
        return view_ascll(a + 10, b)
    else:
        for i in range(a, b + 1):
            s += str(i) + ' - ' + chr(i) + ' '
        print(s)


if __name__ == '__main__':
    start = 32
    end = 127
    view_ascll(start, end)
