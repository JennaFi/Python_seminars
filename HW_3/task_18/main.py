# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов
# в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

n = int(input("Input quantity of elements in list: "))

myList = [randint(1, 11) for i in range(n)]
# myList = set(myList)

x = int(input("Input X: "))

number = x

for i in range(len(myList)):
    if abs(x - myList[i]) < number:
        number = myList[i]

print(myList)

print(f'The closest element in list to X is: {myList[i]}')