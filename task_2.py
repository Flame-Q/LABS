def find_unique(elements):
    result = []
    for item in elements:
        if elements.count(item) == 1:
            result.append(item)
    return result


import pytest

def test_find_unique_empty_list():
    """Тест для пустого списка"""
    assert find_unique([]) == []

def test_find_unique_all_unique():
    """Тест когда все элементы уникальны"""
    assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_find_unique_all_duplicates():
    """Тест когда все элементы дублируются"""
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_find_unique_mixed():
    """Тест со смешанными элементами"""
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]

def test_find_unique_strings():
    """Тест со строками"""
    assert find_unique(["a", "b", "b", "c", "d", "d", "e"]) == ["a", "c", "e"]

def test_find_unique_mixed_types():
    """Тест с разными типами данных"""
    assert find_unique([3, "hello", 3, 2.5, "hello", True]) == [2.5, True]

def test_find_unique_single_element():
    """Тест с одним элементом"""
    assert find_unique([42]) == [42]

def test_find_unique_multiple_duplicates():
    """Тест с элементами, которые повторяются много раз"""
    assert find_unique([1, 1, 1, 2, 2, 2, 3]) == [3]

def test_find_unique_preserve_order():
    """Тест сохранения порядка элементов"""
    assert find_unique([1, 2, 3, 2, 4, 1, 5]) == [3, 4, 5]

def test_find_unique_none_values():
    """Тест со значениями None"""
    assert find_unique([None, 1, None, 2, 3]) == [1, 2, 3]

def test_find_unique_booleans():
    """Тест с булевыми значениями"""
    assert find_unique([True, False, True, False, True]) == []

def test_find_unique_large_list():
    """Тест с большим списком"""
    input_list = [1] * 100 + [2] * 50 + [3]
    assert find_unique(input_list) == [3]


if __name__ == "__main__":
    print("Примеры работы функции:")
    print(f'find_unique([1, 2, 2, 3, 4, 4, 5]) = {find_unique([1, 2, 2, 3, 4, 4, 5])}')
    print(f'find_unique(["a", "b", "b", "c"]) = {find_unique(["a", "b", "b", "c"])}')
    print(f'find_unique([]) = {find_unique([])}')
    print(f'find_unique([1, 1, 2, 3, 3]) = {find_unique([1, 1, 2, 3, 3])}')
    
    print("\nЗапуск тестов...")
    pytest.main([__file__, "-v"])