def sum_multiples_of_three(numbers):
    if not numbers:
        return 0
    
    total = 0
    for num in numbers:
        if num % 3 == 0:
            total += num

    return total


import pytest

@pytest.fixture
def numbers_all_multiples():
    """Все числа делятся на 3"""
    return [3, 6, 9, 12, 15]

@pytest.fixture
def numbers_mixed():
    """Смешанные числа"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

@pytest.fixture  
def numbers_empty():
    """Пустой список"""
    return []

def test_empty_list(numbers_empty):
    """Тест для пустого списка"""
    assert sum_multiples_of_three(numbers_empty) == 0

def test_all_multiples(numbers_all_multiples):
    """Тест, когда все числа делятся на 3"""
    assert sum_multiples_of_three(numbers_all_multiples) == 45

def test_mixed_numbers(numbers_mixed):
    """Тест со смешанными числами"""
    assert sum_multiples_of_three(numbers_mixed) == 18

def test_no_multiples():
    """Тест, когда нет чисел, кратных 3"""
    assert sum_multiples_of_three([1, 2, 4, 5, 7, 8]) == 0

def test_single_number():
    """Тест с одним числом"""
    assert sum_multiples_of_three([3]) == 3
    assert sum_multiples_of_three([4]) == 0

@pytest.mark.negative
def test_negative_numbers():
    """Тест с отрицательными числами"""
    assert sum_multiples_of_three([-3, -2, -1, 0, 1, 2, 3]) == 0

@pytest.mark.large
def test_large_numbers():
    """Тест с большими числами"""
    assert sum_multiples_of_three([100, 300, 999, 1000]) == 1299

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4, 5, 6], 9),
    ([9, 10, 11, 12], 21),
    ([], 0),
    ([7, 8, 10], 0),
])
def test_parametrized(input_list, expected):
    """Тест с разными наборами данных"""
    assert sum_multiples_of_three(input_list) == expected


if __name__ == "__main__":
    print("Примеры работы функции sum_multiples_of_three:")
    print("=" * 50)
    
    test_cases = [
        ([1, 2, 3, 4, 5, 6], "3 + 6 = 9"),
        ([3, 6, 9, 12], "3 + 6 + 9 + 12 = 30"),
        ([], "0 (пустой список)"),
        ([1, 2, 4, 5], "0 (нет чисел, кратных 3)"),
    ]
    
    for numbers, explanation in test_cases:
        result = sum_multiples_of_three(numbers)
        print(f"Числа: {numbers}")
        print(f"Объяснение: {explanation}")
        print(f"Результат: {result}")
        print("-" * 30)
    
    print("\nЗапуск тестов...")
    print("=" * 50)
    
    pytest.main([__file__, "-v"])