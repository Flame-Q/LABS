d = int(input("Введите день рождения: "))
m = int(input("Введите месяц рождения (числом): "))
if (1 <= d <= 31 and 1 <= m <= 12):
    if (m == 3 and d >= 21) or (m == 4 and d <= 20):
        z = "Овен"
    elif (m == 4 and d >= 21) or (m == 5 and d <= 20):
        z = "Телец"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 21):
        z = "Близнецы"
    elif (m == 6 and d >= 22) or (m == 7 and d <= 22):
        z = "Рак"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
        z = "Лев"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        z = "Дева"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 23):
        z = "Весы"
    elif (m == 10 and d >= 24) or (m == 11 and d <= 22):
        z = "Скорпион"
    elif (m == 11 and d >= 23) or (m == 12 and d <= 21):
        z = "Стрелец"
    elif (m == 12 and d >= 22) or (m == 1 and d <= 20):
        z = "Козерог"
    elif (m == 1 and d >= 21) or (m == 2 and d <= 18):
        z = "Водолей"
    else:
        z = "Рыбы"
    print("Ваш знак зодиака:", z)
else:
    print("Введите корректную дату рождения!")
