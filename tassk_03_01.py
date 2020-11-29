# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99
MIN_DIV = 2
MAX_DIV = 9

# Варинат 1
print(f'{"*"*20} Вариант 1 {"*"*20}')
result1 = {i: 0 for i in range(MIN_DIV, MAX_DIV + 1)}
for key in result1:
    for j in range(MIN_ITEM, MAX_ITEM + 1):
        result1[key] += 1 if j % key == 0 else 0

print(result1)

# Вариант 2
print(f'{"*"*20} Вариант 2 {"*"*20}')
for div in range(MIN_DIV, MAX_DIV + 1):
    result2 = 0
    for j in range(MIN_ITEM, MAX_ITEM + 1):
        result2 += 1 if j % div == 0 else 0
    print(f'{result2} натуральных чисел от {MIN_ITEM} до {MAX_ITEM} кратны {div}')
#
