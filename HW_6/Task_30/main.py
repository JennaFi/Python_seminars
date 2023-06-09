# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


n = int(input('Input quantity of elements: '))

a = [0] * n

a[0] = int(input('Input first element: '))
d = int(input('Input difference: '))

for i in range(n):
    print(a[0] + i * d, end=' ')
