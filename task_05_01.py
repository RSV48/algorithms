# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, defaultdict

Company = namedtuple('Company', 'name, profit')
count_company = int(input('Введите количество предприятий: '))
c_col =[]
for i in range(1, count_company + 1):
    name = input(f'Введите наименование {i}-й компании: ')
    for j in range(1,5):
        p = float(input(f'Ведите прибыль за {j}-й квартал, руб.: '))
        c_col.append(Company(name, p))
year_profit = defaultdict(list)
for company, profit in c_col:
    year_profit[company].append(profit)

avg_year_profit = sum([sum(item) for item in year_profit.values()])/len(year_profit)
print('*'*50)
print(f'Среднеговдая прибыль по всем компаниям: {avg_year_profit:3.2f}')
print('*'*50)
print('Компании с прибылью выше или равной средней прибыли:',
      *[' '.join(map(str, [key, sum(item), 'руб']))
        for key, item in year_profit.items() if sum(item) >= avg_year_profit], sep='\n')
print('*'*50)
print('Компании с прибылью ниже среднего:',
      *[' '.join(map(str, [key, sum(item), 'руб']))
        for key, item in year_profit.items() if sum(item) < avg_year_profit], sep='\n')








