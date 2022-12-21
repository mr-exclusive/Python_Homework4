# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов.

def read_polynom(file_name):
    with open(file_name, 'r') as f:
        return f.readline()


def sum_polynoms(dic_polynom: dict, equation: str):
    list_eq = equation.replace('+', ' ').replace('-', ' -').split()
    for item in list_eq:
        if item != '':
            list_parts = [int(i) for i in item.split('x^')]
            if list_parts[1] in dic_polynom:
                dic_polynom[list_parts[1]] += list_parts[0]
            else:
                dic_polynom[list_parts[1]] = list_parts[0]


def get_polynom(dic_polynom: dict):
    polynom = ''
    for power, coeff in sorted(dic_polynom.items(), key=lambda t: t[0], reverse=True):
        if coeff != 0:
            if coeff > 0 and polynom != '':
                polynom += '+'
            polynom += f'{coeff}x^{power}'

    return polynom


eq1 = read_polynom('equation1.txt')
eq2 = read_polynom('equation2.txt')
print(eq1)
print(eq2)

dic_equation = dict()
sum_polynoms(dic_equation, eq1)
sum_polynoms(dic_equation, eq2)

# print(dic_equation)
polynom = get_polynom(dic_equation)
# print(polynom)

with open('equation_sum.txt', 'w') as f:
    f.write(polynom)
