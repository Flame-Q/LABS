def merge(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge(dict1[key], value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value
    
    return dict1

print("Пример 1")
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("Первый словарь:")
print("dict_a =", dict_a)
print("Второй словарь:")
print("dict_b =", dict_b)

result = merge(dict_a, dict_b)
print("Результат объединения:")
print("dict_a =", result)