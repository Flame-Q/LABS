num = input("Введите числа через пробел: ")
num = num.split()

nums = []
for n in num:
    if '.' in n:
        nums.append(float(n))
    else:
        nums.append(int(n))

print("1. Уникальные числа:", list(set(nums)))

rnum = []
for n in nums:
    if nums.count(n) > 1 and n not in rnum:
        rnum.append(n)
print("2. Повторяющиеся числа:", rnum)

even = []
odd = []
for n in nums:
    is_even = (n % 2 == 0)
    if is_even:
        even.append(n)
    else:
        odd.append(n)
print("3. Четные числа:", even)
print("   Нечетные числа:", odd)

minus = []
for n in nums:
    is_minus = (n < 0)
    if is_minus:
        minus.append(n)
print("4. Отрицательные числа:", minus)

floats = []
for n in nums:
    is_float = isinstance(n, float)
    if is_float:
        floats.append(n)
print("5. Числа с плавающей точкой:", floats)

sum = 0
for n in nums:
    is_kr = (n % 5 == 0)
    if is_kr:
        sum += n
print("6. Сумма чисел, кратных 5:", sum)

print("7. Самое большое число:", max(nums))
print("8. Самое маленькое число:", min(nums))