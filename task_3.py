str = input("Введите числа через пробел: ")
str = str.split()

numbers = []
for num_str in str:
    numbers.append(int(num_str))

uniq = list(set(numbers))

uniq.sort()

if len(uniq) >= 2:
    sec = uniq[-2]
    print("Второе по величине число: ", sec)
else:
    print("В списке меньше двух различных чисел")