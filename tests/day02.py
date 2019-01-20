from collections import Counter

from advent_of_code_2018.day02.day02 import (
    count_string_differences, day02a, day02b, generate_checksum,
    generate_counter, generate_data, generate_matches,
    identify_matched_letters,
)


def test_generate_data():
    data = generate_data('./files/day02a_test.txt')
    assert data == ['abcdef',
                    'bababc',
                    'abbcde',
                    'abcccd',
                    'aabcdd',
                    'abcdee',
                    'ababab']


def test_generate_counter():
    data = ['abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab']
    res = generate_counter(data)
    assert res == Counter({
        '1': 6,
        '2': 4,
        '3': 3
    })


def test_generate_checksum():
    data = Counter({
        '1': 6,
        '2': 4,
        '3': 3
    })
    res = generate_checksum(data)
    assert res == 12


def test_day02a():
    res = day02a('./files/day02a_test.txt')
    assert res == "Checksum is 12."


def test_count_string_differences():
    str1 = 'abcdef'
    str2 = 'abddif'
    res = count_string_differences(str1, str2)

    assert res == 2


def test_generate_matches():
    data = ['abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz']
    res = generate_matches(data)
    assert res == [('fghij', 'fguij')]


def test_identify_matched_letters():
    data = [('fghij', 'fguij')]
    res = identify_matched_letters(data)
    assert res == ['fgij']


def test_day02b():
    res = day02b('./files/day02b_test.txt')
    assert res == 'fgij'
