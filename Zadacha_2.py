'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного
минимума и не больше заданного максимума)
'''

import random
count = int(input('Введите длину списка: '))
list = [random.randint(-5, 15) for _ in range(count)]
print(list)

min = int(input('Введите минимум диапазона: '))
max = int(input('Введите максимум диапазона: '))
new_list = []

for i in range(0, len(list)):
    if min <= list[i] <= max:
        new_list.append(i)
print(new_list)