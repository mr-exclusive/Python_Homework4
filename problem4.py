# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

p = int(input('Enter power of the equation: '))

for i in range(p, -1, -1):
    c = rnd(-100, 100)

    if c > 0 and i != p:
        print('+', end='')

    if c < -1 or c > 1 or (i == 0 and c != 0):
        print(c, end='')
        if i != 0:
            print('*', end='')

    if c != 0 and i != 0:
        print('x', end='')

    if i > 1:
        print(f'^{i}', end='')

print('=0')
