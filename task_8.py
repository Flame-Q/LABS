import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        exec_time = (end_time - start_time) * 1000
        
        print("Функция '" + func.__name__ + "' выполнилась за " + str(round(exec_time, 2)) + " мс")
        
        return result
    return wrapper

@timing
def sum_numbers(a, b):
    print("Складываем числа: " + str(a) + " и " + str(b))
    time.sleep(0.05)
    return a + b

print("Тестирование декоратора @timing:")
result1 = sum_numbers(10, 20)
print("Результат сложения: " + str(result1))