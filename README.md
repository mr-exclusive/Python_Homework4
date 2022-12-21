1. Пользователь вводит число, нужно вывести чило pi с заданной точностью. (БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

---

2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

---

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
последовательности.

---

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

---

5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму 
многочленов.

---

6. Друзья друзей

Теория шести рукопожатий — социологическая теория, согласно которой любые два человека на Земле разделены не более, 
чем пятью уровнями общих знакомых (и, соответственно, шестью уровнями связей). Формальная математическая формулировка 
теории: диаметр графа знакомств не превышает 6. Мы не станем так сильно углубляться в дружественные связи и пока нам 
хватит только двух уровней. Напишите программу, которая по списку дружественных пар для каждого человека определяет 
список «друзей 2-го уровня».

**Формат ввода**

- В каждой строке записывается два имени.
- Окончанием ввода служит пустая строка.

**Формат вывода**

Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.

_Пример 1_

Ввод

Иванов Петров

Иванов Сергеев

Васильев Петров

Сергеев Яковлев

Петров Кириллов

Петров Яковлев


Вывод

Васильев: Иванов, Кириллов, Яковлев

Иванов: Васильев, Кириллов, Яковлев

Кириллов: Васильев, Иванов, Яковлев

Петров: Сергеев

Сергеев: Петров

Яковлев: Васильев, Иванов, Кириллов

_Пример 2_

Ввод

Николай Фёдор

Николай Женя

Фёдор Женя

Фёдор Илья

Илья Фёдор


Вывод

Женя: Илья

Илья: Женя, Николай

Николай: Илья

Фёдор: