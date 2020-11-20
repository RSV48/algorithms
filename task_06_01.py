# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание:
# По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:● выбрать хорошую задачу, которую имеет
# смысл оценивать по памяти; ● написать 3 варианта кода (один у вас уже есть);● проанализировать 3 варианта и выбрать
# оптимальный; ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев
# в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;● написать общий вывод:
# какой из трёх вариантов лучше и почему. Надеемся, что вы не испортили программы, добавив в них множество
# sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.


import random, platform, sys

# ********************** ВЫВОД ***********************

# Версия ОС Darwin, разрядность ОС ('64bit', ''), версия Python 3.8

# Проведена оценка выделенного объема памяти для трех вариантов алгорима по посику максимального элемента среди
# минимальных элементов столбцов матрицы 5Х5:
#
#   функция m_for_in объем выделнной памяти под переменные 2024
#   функция m_while объем выделнной памяти под переменные 1532
#   функция m_min_max объем выделнной памяти под переменные 2664
#
# По результатм проведенного анализа сделан вывод, что с точки зрения минимального выделния памяти наиболее
# оптимальный алгорим в функции m_while Не учтенный при оценке функций объем памяти выденной для констант 108

# #################### АНАЛИЗИРУЕМЫЙ КОД #########################
LINE = 5
COLUMN = 5
MIN_ITEM = 0
MAX_ITEM = 1000
array_static = [[random.randint(MIN_ITEM, MAX_ITEM) for j in range(COLUMN)] for i in range(LINE)]


# Переменная LINE            Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная COLUMN          Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная MIN_ITEM        Тип переменной = <class 'int'>, Выделено памяти = 24
# Переменная MAX_ITEM        Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная array_static    Тип переменной = <class 'list'>, Выделено памяти = 1420
# Всего выделено памяти =  1528


# ВАРИАНТ 1 FOR IN

def m_for_in(matrix=array_static):
    min_column = matrix[0]
    for line in matrix:
        for j, el in enumerate(line):
            min_column[j] = el if el < min_column[j] else min_column[j]
    max_el = min_column[0]
    for el in min_column:
        max_el = el if el > max_el else max_el
    return max_el


# Наименование функции: m_for_in
# Переменная matrix          Тип переменной = <class 'list'>, Выделено памяти = 1420
# Переменная min_column      Тип переменной = <class 'list'>, Выделено памяти = 260
# Переменная line            Тип переменной = <class 'list'>, Выделено памяти = 260
# Переменная j               Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная el              Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная max_el          Тип переменной = <class 'int'>, Выделено памяти = 28
# Всего выделено памяти =  2024


# ВАРИАНТ 2 WHILE

def m_while(matrix=array_static):
    max_el = None
    j = 0
    while j < len(matrix[0]):
        min_el = matrix[0][j]
        i = 0
        while i < len(matrix):
            min_el = matrix[i][j] if matrix[i][j] < min_el else min_el
            i += 1
        if max_el is None or max_el < min_el:
            max_el = min_el
        j += 1
    return max_el


# Наименование функции: m_while
# Переменная matrix          Тип переменной = <class 'list'>, Выделено памяти = 1420
# Переменная max_el          Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная j               Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная min_el          Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная i               Тип переменной = <class 'int'>, Выделено памяти = 28
# Всего выделено памяти =  1532


# ВАРИАНТ 3 встроенные функции min max

def m_min_max(matrix=array_static):
    min_el = []
    for i in range(len(matrix[0])):
        for line in matrix:
            min_el.append(min(line))
    return max(min_el)


# Наименование функции: m_min_max
# Переменная matrix          Тип переменной = <class 'list'>, Выделено памяти = 1420
# Переменная min_el          Тип переменной = <class 'list'>, Выделено памяти = 956
# Переменная i               Тип переменной = <class 'int'>, Выделено памяти = 28
# Переменная line            Тип переменной = <class 'list'>, Выделено памяти = 260
# Всего выделено памяти =  2664

# ############################# РЕШЕНИЕ ###############################
print(f'Версия ОС {platform.system()}, разрядность ОС {platform.architecture()}, '
      f'версия Python {sys.version_info.major}.{sys.version_info.minor}')


def trace(frame, event, arg):
    total_size = 0
    result = {}
    if event == 'return':
        co = frame.f_code
        func_name = co.co_name
        for key in frame.f_locals.keys():
            size = var_size(frame.f_locals[key])
            total_size += size
            result[key] = [type(frame.f_locals[key]), size]
        result['total_size'] = ['total_size', total_size]
        print('*' * 50)
        print(f'Наименование функции: {func_name}')
        for var, value in result.items():
            if var != 'total_size':
                print(f'Переменная {var:15} Тип переменной = {value[0]}, Выделено памяти = {value[1]:<15}')
            else:
                print(f'Всего выделено памяти = {value[1]:5}')

    return trace


def var_size(x):
    result = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result += var_size(key)
                result += var_size(value)
        elif not isinstance(x, str):
            for item in x:
                result += var_size(item)

    return result


def trace_module(loc):
    print(f'{"*"*50} \nПеременные модуля:')
    total_size = 0
    for var in loc.keys():
        t = str(type(loc[var]))
        if var[:2] != '__' and t not in ("<class 'module'>", "<class 'type'>", "<class 'function'>"):
            size = var_size(loc[var])
            print(f'Переменная {var:15} Тип переменной = {type(loc[var])}, Выделено памяти = {size:<15}')
            total_size += size
    print(f'Всего выделено памяти = {total_size:5}')


trace_module(locals())
sys.settrace(trace)

# ####################### ВЫЗОВ АНАЛИЗИРУЕМЫХ ФУНКЦИЙ ############################

m_for_in()
m_while()
m_min_max()
