def type_check(*expect_types):
    def decorator(orig_function):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                current_arg = args[i]
                expect_type = expect_types[i]
                if not isinstance(current_arg, expect_type):
                    error_message = "Аргумент " + str(i+1) + " должен быть типа " + expect_type.__name__ + ", но получен " + type(current_arg).__name__
                    raise TypeError(error_message)
            
            for i in range(len(args), len(expect_types)):
                param_name = orig_function.__code__.co_varnames[i]
                
                if param_name in kwargs:
                    named_arg = kwargs[param_name]
                    expect_type = expect_types[i]
                
                    if not isinstance(named_arg, expect_type):
                        error_message = "Аргумент '" + param_name + "' должен быть типа " + expect_type.__name__ + ", но получен " + type(named_arg).__name__
                        raise TypeError(error_message)
            
            return orig_function(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print("ТЕСТ 1: Правильные аргументы")
print("Вызываем add(5, 3)")
result = add(5, 3)
print("Результат: " + str(result))
print("Успех! Оба аргумента были числами")
    
print("ТЕСТ 2: Второй аргумент - строка")
print("Вызываем add(5, '3')")
try:
    add(5, "3")
except TypeError as error:
    print("Поймана ошибка: " + str(error))
    print("Это правильно! Второй аргумент должен быть числом")