# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить
# ровно k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите ширину шоколадки: "))
m = int(input("Введите длину шоколадки: "))
k = int(input("Введите кол-во долек, которое хотите отломить: "))

if k <= n*m and (k % m == 0 or k % n == 0):
    print('yes')
else:
    print('no')    