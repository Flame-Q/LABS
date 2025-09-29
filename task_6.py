def uniq_elements(input_list):
    result = []
    
    def flatten(lst):
        for item in lst:
            if type(item) == list:
                flatten(item)
            else:
                if item not in result:
                    result.append(item)
    
    flatten(input_list)
    
    return result

print("Исходный вложенный список:")
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(list_a)

print("Уникальные элементы:")
uniq = uniq_elements(list_a)
print(uniq)