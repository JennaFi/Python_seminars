# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Input the quantity of coins: "))

count_head = 0
count_tail = 0
# head = 0
# tail = 1

for i in range(n):
    head = int(input("Input head or tail is the next coin: "))
    if head == 0:
        count_head += 1
    else:
        count_tail += 1
if count_head > count_tail:
    print(f"The minimum of coins needed to turned out is: {count_tail}")
else:
    print(f"The minimum of coins needed to turned out is: {count_head}")



