# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума


from random import randint

my_list = [randint(1, 10) for i in range(20)]
new_list = []

print('Original list: ', my_list, sep='\n')

max_index = 10
min_index = 3

for i in range(len(my_list)):
    if my_list[i] >= min_index and my_list[i] <= max_index:
        new_list.append(i)

print(new_list)
