import random

r_num = random.randint(1, 100)
while True:
    num = int(input("Введите число от 1 до 100: "))
    if (num > r_num):
        num = print("Меньше")
    elif (num < r_num):
        num = print("Больше")
    else:
        print("Вы угадали число!", num)
        break