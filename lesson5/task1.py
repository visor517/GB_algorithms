"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

companies = []

Company = namedtuple('Company', 'name, total_profit')

global_profit = 0

num = int(input('Введите число компаний: '))

for i in range(1, num + 1):
    name = input(f'Введите название компании {i}: ')

    while True:
        values = input('Введите прибыль за 4 квартала через пробел: ')
        profits = values.split(" ")
        if len(profits) == 4:
            try:  
                total_profit = sum([int(item) for item in profits])
            except ValueError:
                print('Нужно вводить числа!!!')
            else:
                companies.append(Company(name, total_profit))
                global_profit += total_profit
                break
                    
        else:
            print('Нужно ввести 4 числа!!!')

avg_profit = global_profit / num

print(f'Средняя прибыль: {avg_profit}')

print('Компании с прибылью выше средней:')
for company in companies:
    if company.total_profit > avg_profit:
        print(f'{company.name} : {company.total_profit}')

print('Компании с прибылью ниже средней:')
for company in companies:
    if company.total_profit < avg_profit:
        print(f'{company.name} : {company.total_profit}')
