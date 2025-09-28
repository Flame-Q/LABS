def func(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            func(lst[i])
            lst[i:i+1] = lst[i]
        else:
            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]

print("Исходный список:")
print(list_a)

func(list_a)

print("Плоский список:")
print(list_a)