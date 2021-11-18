"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
    для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
    и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

# def Description_company(name_, profit):
#     Company = namedtuple('Company', 'name cash', defaults=(None, []))
#     return Company(name_, profit)

COUNT_COMPANY = int(input('Введите кол-во компаний: '))
COMPANY = namedtuple('Company', 'name, cash', defaults=(None, []))
COUNT_PERIODS = 4

# profit_q = [0, 0, 0, 0]
profit_q = []

company_profit = dict()
total_profit = 0
count = 1
while count <= COUNT_COMPANY:
    name_ = str(input('Введите название компании: '))
    if name_:
        for i in range(COUNT_PERIODS):
            while len(profit_q) < COUNT_PERIODS:
                profit = str(input('Введите прибыль компании: '))
                if profit:
                    profit = int(profit)
                    # profit_q[i] = profit
                    profit_q.append(profit)
                else:
                    continue

        result = COMPANY(name_, profit_q)
        company_profit[result.name] = result.cash

        total_profit += sum(result.cash)

        # print(company_profit, total_profit)
        if count == COUNT_COMPANY:
            print('\n\n', company_profit)
            mean_ = round(total_profit / COUNT_COMPANY)
            for name, value in company_profit.items():
                # print('dict', name, value, mean_ )
                profit_periods = sum(value)
                if profit_periods > mean_:
                    print(f'Комапнии с прибылью за период выше среднего({mean_}): {name},'
                          f' прибыль за период: {profit_periods}')
                elif profit_periods < mean_:
                    print(f'Комапнии с прибылью за период ниже среднего({mean_}): {name},'
                          f' прибыль за период: {profit_periods}')

        profit_q = []
        count += 1
