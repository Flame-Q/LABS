num = input("Введите числа через пробел: ")
num = num.split()
nums = []

for n in num:
    if '.' in n:
        nums.append(float(n))
    else:
        nums.append(int(n))
        
rnum = []
for n in nums:
    if nums.count(n) > 1 and n not in rnum:
        rnum.append(n)
print("2. Повторяющиеся числа:", rnum)

unique_nums = [n for n in nums if n not in rnum]
print("1. Уникальные числа:", unique_nums)

even = []
odd = []
odd_processed = []

for n in nums:
    if isinstance(n, float):
        continue
    
    if n % 2 == 0:
        even.append(n)
    else:
        if n in rnum:
            if n not in odd_processed:
                odd.append(n)
                odd_processed.append(n)
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

sum_kr = 0
for n in nums:
    if n % 5 == 0:
        sum_kr += n
print("6. Сумма чисел, кратных 5:", sum_kr)

print("7. Самое большое число:", max(nums))
print("8. Самое маленькое число:", min(nums))