# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Input quantity of the first set: "))
m = int(input("Input quantity of the second set: "))

print("Input numbers in the first set: ")

    
first_list =  [int(i) for i in input().split()]
print(first_list)

print("Input numbers in the first set: ")

second_list = [int(i) for i in input().split()]
print(second_list)

inter_set = set(first_list) & set(second_list)

print(sorted(inter_set))