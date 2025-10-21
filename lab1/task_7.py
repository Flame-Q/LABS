sec = int(input("Введите кол-во секунд: "))
min = sec // 60
sec = sec % 60
print(f"Минуты - {min}. Секунды - {sec}")