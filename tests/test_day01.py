from advent_of_code_2018.day01.day01 import (
    calculate_frequency, day01a, generate_data,
    is_duplicate,
    day01b,
)


def test_generate_data():
    res = generate_data('./files/day01a_test.txt')
    assert res == [1, 1, -2]


def test_calculate_frequency():
    data = [1, 1, -2]
    res = calculate_frequency(data)
    assert len(list(res)) == 3


def test_day01a():
    res = day01a('./files/day01a_test.txt')
    assert res == 0


def test_is_duplicate():
    test_results = {0, -6, -3, 5, 10, 4}
    test_value = -3
    res = is_duplicate(test_value, test_results)
    assert res


def test_day01b():
    res = day01b('./files/day01b_test.txt')
    assert res == 5
