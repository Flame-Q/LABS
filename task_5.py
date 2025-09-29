def cache(func):
    cache_dict = {}
    
    def wrapper(*args):
        if args in cache_dict:
            print("Результат взят из кэша для аргументов ", args)
            return cache_dict[args]
        
        print("Вычисляем результат для аргументов ",args)
        result = func(*args)
        cache_dict[args] = result
        return result
    
    return wrapper

@cache
def multiply(a, b):
    return a * b

# Тестируем
print("Первый вызов")
result1 = multiply(2, 3)
print("Результат: ", result1)

print("Второй вызов с теми же аргументами")
result2 = multiply(2, 3)
print("Результат: ", result2)

print("Вызов с другими аргументами")
result3 = multiply(4, 5)
print("Результат: ", result3)

print("Еще один вызов с первыми аргументами")
result4 = multiply(2, 3)
print("Результат: ", result4)