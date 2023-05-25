# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("The sum of X and Y is: "))
p = int(input("The multiplication of X and Y is: "))

# x + y = s
# x * y = p
# x*x -s*y +p = 0


if s > 1000 or p > 1000:
    print("Please input digits under 1000")

for x in range(s):
    for y in range(p):
        if (x + y == s) and (x * y == p):
            print(f'x = {x} and y = {y}')


