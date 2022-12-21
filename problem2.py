# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Enter a whole number: '))

if n == 1:
    print(n)
else:
    multipliers = []
    i = 2
    while n > 1:
        if n % i == 0:
            n //= i
            multipliers.append(i)
            i = 2
        else:
            i += 1

    print(multipliers)
