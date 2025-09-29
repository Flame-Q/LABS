def merge_sorted_list(list1, list2):
    result = []
    i = 0
    j = 0
    
    print("Начало объединения списков")
    print("Первый список:", list1)
    print("Второй список:", list2)
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            print("Добавили элемент из первого списка:", list1[i])
            i += 1
        else:
            result.append(list2[j])
            print("Добавили элемент из второго списка:", list2[j])
            j += 1
        print("Текущий результат:", result)
    
    while i < len(list1):
        result.append(list1[i])
        print("Добавили оставшийся элемент из первого списка:", list1[i])
        i += 1
        print("Текущий результат:", result)
    
    while j < len(list2):
        result.append(list2[j])
        print("Добавили оставшийся элемент из второго списка:", list2[j])
        j += 1
        print("Текущий результат:", result)
    
    print("Финальный отсортированный список:", result)
    return result

list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]
print("Пример 1:")
merged = merge_sorted_list(list_a, list_b)