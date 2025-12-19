def combine_dicts(dict1, dict2):
    result = dict1.copy()  
    result.update(dict2) 
    return result


import pytest

def test_combine_dicts_basic():
    """Тест базового объединения"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_overlapping_keys():
    """Тест с перекрывающимися ключами"""
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'c': 30, 'd': 4, 'e': 5}
    expected = {'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_empty_first():
    """Тест когда первый словарь пустой"""
    dict1 = {}
    dict2 = {'a': 1, 'b': 2}
    expected = {'a': 1, 'b': 2}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_empty_second():
    """Тест когда второй словарь пустой"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {}
    expected = {'a': 1, 'b': 2}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_both_empty():
    """Тест когда оба словаря пустые"""
    assert combine_dicts({}, {}) == {}

def test_combine_dicts_nested_dicts():
    """Тест со вложенными словарями"""
    dict1 = {'a': {'x': 1}, 'b': 2}
    dict2 = {'b': 20, 'c': {'y': 3}}
    expected = {'a': {'x': 1}, 'b': 20, 'c': {'y': 3}}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_different_value_types():
    """Тест с разными типами значений"""
    dict1 = {'a': 1, 'b': 'hello', 'c': [1, 2, 3]}
    dict2 = {'c': 'replaced', 'd': 4.5, 'e': True}
    expected = {'a': 1, 'b': 'hello', 'c': 'replaced', 'd': 4.5, 'e': True}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_preserves_second_dict_values():
    """Тест что значения из второго словаря сохраняются"""
    dict1 = {'key': 'value1'}
    dict2 = {'key': 'value2'}
    result = combine_dicts(dict1, dict2)
    assert result['key'] == 'value2'

def test_combine_dicts_original_dicts_unchanged():
    """Тест что исходные словари не изменяются"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 20, 'c': 3}
    dict1_original = dict1.copy()
    dict2_original = dict2.copy()
    
    combine_dicts(dict1, dict2)
    
    assert dict1 == dict1_original
    assert dict2 == dict2_original

def test_combine_dicts_with_none_values():
    """Тест со значениями None"""
    dict1 = {'a': None, 'b': 2}
    dict2 = {'b': None, 'c': 3}
    expected = {'a': None, 'b': None, 'c': 3}
    assert combine_dicts(dict1, dict2) == expected

def test_combine_dicts_large_dicts():
    """Тест с большими словарями"""
    dict1 = {f'key{i}': i for i in range(100)}
    dict2 = {f'key{i}': i*10 for i in range(50, 150)}
    result = combine_dicts(dict1, dict2)
    
    assert len(result) == 150
    for i in range(50, 100):
        assert result[f'key{i}'] == i * 10


if __name__ == "__main__":
    print("Примеры работы функции:")
    
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 20, 'c': 3}
    print(f"dict1 = {dict1}")
    print(f"dict2 = {dict2}")
    print(f"combine_dicts(dict1, dict2) = {combine_dicts(dict1, dict2)}")
    
    dict3 = {'name': 'Alice', 'age': 25}
    dict4 = {'age': 26, 'city': 'Moscow'}
    print(f"\ndict3 = {dict3}")
    print(f"dict4 = {dict4}")
    print(f"combine_dicts(dict3, dict4) = {combine_dicts(dict3, dict4)}")
    
    print("\nЗапуск тестов...")
    pytest.main([__file__, "-v"])