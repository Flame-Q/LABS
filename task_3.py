def is_palindrome(word):
    word_str = str(word)
    return word_str == word_str[::-1]


import pytest

def test_is_palindrome_empty_string():
    """Тест для пустой строки"""
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    """Тест для одного символа"""
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True

def test_is_palindrome_simple_palindromes():
    """Тест для простых палиндромов"""
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deed") == True

def test_is_palindrome_not_palindromes():
    """Тест для не палиндромов"""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_is_palindrome_case_sensitive():
    """Тест с учетом регистра"""
    assert is_palindrome("Radar") == False 
    assert is_palindrome("Level") == False 

def test_is_palindrome_with_spaces():
    """Тест с пробелами"""
    assert is_palindrome("a man a plan a canal panama") == False
    assert is_palindrome("race car") == False

def test_is_palindrome_numbers():
    """Тест с числами"""
    assert is_palindrome(121) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(123) == False
    assert is_palindrome(12345) == False

def test_is_palindrome_special_cases():
    """Тест специальных случаев"""
    assert is_palindrome("a") == True
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False

def test_is_palindrome_long_palindromes():
    """Тест длинных палиндромов"""
    assert is_palindrome("abcdefghihgfedcba") == True
    assert is_palindrome("abcdefghhgfedcba") == True

def test_is_palindrome_mixed_characters():
    """Тест со смешанными символами"""
    assert is_palindrome("a1b1a") == True
    assert is_palindrome("a1b2a") == False

def test_is_palindrome_zero_and_negative():
    """Тест с нулем и отрицательными числами"""
    assert is_palindrome(0) == True
    assert is_palindrome(-121) == False

def test_is_palindrome_whitespace_only():
    """Тест только с пробелами"""
    assert is_palindrome("   ") == True


if __name__ == "__main__":
    print("Примеры работы функции:")
    print(f'is_palindrome("radar") = {is_palindrome("radar")}')
    print(f'is_palindrome("hello") = {is_palindrome("hello")}')
    print(f'is_palindrome(12321) = {is_palindrome(12321)}')
    print(f'is_palindrome(12345) = {is_palindrome(12345)}')
    print(f'is_palindrome("") = {is_palindrome("")}')
    print(f'is_palindrome("A") = {is_palindrome("A")}')
    
    print("\nЗапуск тестов...")
    pytest.main([__file__, "-v"])