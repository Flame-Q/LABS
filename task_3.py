import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            
            log_entry = current_time + " - Функция '" + func.__name__ + "' вызвана с аргументами: args=" + str(args) + ", kwargs=" + str(kwargs) + "\n"
            
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(log_entry)
            
            print("Запись в лог выполнена: " + func.__name__)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("log.txt")
def multiply(a, b):
    result = a * b
    print("Результат умножения: " + str(a) + " * " + str(b) + " = " + str(result))
    return result

@log_calls("log.txt")
def say_hello(name, age):
    message = "Привет, " + name + "! Сейчас " + str(age) + "-ый год."
    print(message)
    return message

print("Тест 1")
multiply(4, 5)

print("Тест 2")
say_hello("Мир", 25)

print("Логи записаны в файл: log.txt")