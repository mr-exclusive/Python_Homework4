# 1. Пользователь вводит число, нужно вывести чило pi с заданной точностью. (БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

precision = int(input('Enter precision: '))

pi = 0
for n in range(precision):
    pi += (1 / 16 ** n) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
print(f'Pi = {round(pi, precision)}')
