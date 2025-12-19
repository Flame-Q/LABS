def count_words(sentence):
    if not sentence or sentence.isspace():
        return 0
    words = sentence.split()
    return len(words)


import pytest

def test_count_words_empty_string():
    """Тест для пустой строки"""
    assert count_words("") == 0

def test_count_words_only_spaces():
    """Тест для строки только с пробелами"""
    assert count_words("   ") == 0
    assert count_words("  \t  \n  ") == 0

def test_count_words_single_word():
    """Тест для одного слова"""
    assert count_words("hello") == 1
    assert count_words("  hello  ") == 1

def test_count_words_multiple_words():
    """Тест для нескольких слов"""
    assert count_words("hello world") == 2
    assert count_words("hello world python") == 3

def test_count_words_multiple_spaces():
    """Тест с несколькими пробелами между словами"""
    assert count_words("hello    world") == 2
    assert count_words("  hello    world  ") == 2

def test_count_words_with_tabs_and_newlines():
    """Тест с табуляцией и переносами строк"""
    assert count_words("hello\tworld") == 2
    assert count_words("hello\nworld") == 2
    assert count_words("hello\t\nworld") == 2

def test_count_words_punctuation():
    """Тест со знаками препинания"""
    assert count_words("hello, world!") == 2
    assert count_words("hello, world! how are you?") == 5

def test_count_words_numbers():
    """Тест с числами"""
    assert count_words("123 456 789") == 3
    assert count_words("I have 2 apples") == 4

def test_count_words_mixed_case():
    """Тест с разным регистром"""
    assert count_words("Hello World Python") == 3

def test_count_words_special_characters():
    """Тест со специальными символами"""
    assert count_words("@username #hashtag $price") == 3


if __name__ == "__main__":
    print("Примеры работы функции:")
    print(f'count_words("hello world") = {count_words("hello world")}')
    print(f'count_words("") = {count_words("")}')
    print(f'count_words("   multiple   spaces   ") = {count_words("   multiple   spaces   ")}')
    print(f'count_words("Python is awesome!") = {count_words("Python is awesome!")}')
    
    print("\nЗапуск тестов...")
    pytest.main([__file__, "-v"])