nums1 = input("Введите первый набор чисел через пробел: ")
nums1 = nums1.split()
set1 = set()
for num in nums1:
    set1.add(int(num))

nums2 = input("Введите второй набор чисел через пробел: ")
nums2 = nums2.split()
set2 = set()
for num in nums2:
    set2.add(int(num))

common = set1 & set2
print("1. Числа в обоих наборах:", sorted(common))

in_first = set1 - set2
print("2. Числа только в первом наборе: ", sorted(in_first))

in_sec = set2 - set1
print("   Числа только во втором наборе: ", sorted(in_sec))

all = (set1 | set2) - common
print("3. Все числа кроме общих: ", sorted(all))