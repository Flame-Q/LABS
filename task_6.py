list = input("Введите элементы списка через пробел: ")
list = list.split()

uniq_list = []
for n in list:
    if n not in uniq_list:
        uniq_list.append(n)

print("Список без дубликатов:", uniq_list)