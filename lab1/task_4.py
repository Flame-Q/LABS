sum = int(input("Введите сумму в рублях (целое число): "))
nominal_100 = sum // 100
sum = sum % 100
nominal_50 = sum // 50
sum = sum % 50
nominal_10 = sum // 10
sum = sum % 10
nominal_5 = sum // 5
sum = sum % 5
nominal_2 = sum // 2
sum = sum % 2
nominal_1 = sum // 1
print("Купюр по 100:", nominal_100)
print("Купюр по 50:", nominal_50)
print("Купюр по 10:", nominal_10)
print("Купюр по 5:", nominal_5)
print("Купюр по 2:", nominal_2)
print("Купюр по 1:", nominal_1)