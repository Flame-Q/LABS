def are_anagrams(str1, str2):
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    
    return sorted(str1_clean) == sorted(str2_clean)


import pytest

def test_are_anagrams_simple():
    """Тест простых анаграмм"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("evil", "vile") == True

def test_are_anagrams_not_anagrams():
    """Тест не анаграмм"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False
    assert are_anagrams("apple", "pale") == False

def test_are_anagrams_with_spaces():
    """Тест анаграмм с пробелами"""
    assert are_anagrams("dormitory", "dirty room") == True
    assert are_anagrams("school master", "the classroom") == True
    assert are_anagrams("conversation", "voices rant on") == True

def test_are_anagrams_case_insensitive():
    """Тест регистронезависимости"""
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("ABC", "cab") == True
    assert are_anagrams("Hello", "Olleh") == True

def test_are_anagrams_different_length():
    """Тест строк разной длины"""
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("short", "longer") == False

def test_are_anagrams_empty_strings():
    """Тест пустых строк"""
    assert are_anagrams("", "") == True
    assert are_anagrams("", "a") == False

def test_are_anagrams_single_character():
    """Тест одного символа"""
    assert are_anagrams("a", "a") == True
    assert are_anagrams("a", "b") == False

def test_are_anagrams_same_word():
    """Тест одинаковых слов"""
    assert are_anagrams("hello", "hello") == True
    assert are_anagrams("test", "test") == True

def test_are_anagrams_with_punctuation():
    """Тест со знаками препинания"""
    assert are_anagrams("hello!", "!olleh") == True
    assert are_anagrams("test!", "test") == False

def test_are_anagrams_numbers():
    """Тест с числами в строках"""
    assert are_anagrams("123", "321") == True
    assert are_anagrams("a1b2", "2b1a") == True

def test_are_anagrams_whitespace_only():
    """Тест только с пробелами"""
    assert are_anagrams("   ", "  ") == True
    assert are_anagrams("  a  ", "a") == True

def test_are_anagrams_famous_examples():
    """Тест известных анаграмм"""
    assert are_anagrams("William Shakespeare", "I am a weakish speller") == True
    assert are_anagrams("eleven plus two", "twelve plus one") == True


if __name__ == "__main__":
    print("Примеры работы функции:")
    print(f'are_anagrams("listen", "silent") = {are_anagrams("listen", "silent")}')
    print(f'are_anagrams("hello", "world") = {are_anagrams("hello", "world")}')
    print(f'are_anagrams("dormitory", "dirty room") = {are_anagrams("dormitory", "dirty room")}')
    print(f'are_anagrams("Listen", "Silent") = {are_anagrams("Listen", "Silent")}')
    print(f'are_anagrams("", "") = {are_anagrams("", "")}')
    
    print("\nЗапуск тестов...")
    pytest.main([__file__, "-v"])