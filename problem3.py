# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

list_orig = [2, 6, 3, 3, 5, 9, 3, 2, 1, 1, 7, 8, 8]
list_unique = []

for n in list_orig:
    if n not in list_unique:
        list_unique.append(n)

print(list_unique)
