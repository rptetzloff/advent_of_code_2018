import os
from collections import Counter
from typing import List, Tuple
from typing import Counter as CounterType


def generate_data(input_file):
    data = []
    with open(os.path.abspath(input_file), 'r') as f_in:
        for i in f_in:
            data.append(i.strip())

    return data


def generate_counter(data: List[str]):
    res = Counter()
    for i in data:
        c = Counter(i)

        _values = set(c.values())
        print(_values)
        for val in _values:
            res.update(str(val))

    return res


def generate_checksum(counter: CounterType, multiples:Tuple[int] = (2, 3)) -> \
        int:
    checksum = 1
    for i in multiples:
        checksum *= counter[str(i)]

    return checksum


def day02a(input_file):
    data = generate_data(input_file)
    c = generate_counter(data)
    checksum = generate_checksum(c)
    return f'Checksum is {checksum}.'


def count_string_differences(str1, str2):
    """
    Compare two strings
    What to return?
    """

    # If strings are equal, return no differences
    if str1 == str2:
        return 0

    # If strings are not the same length, fail
    # TODO: implement exception here
    if len(str1) != len(str2):
        return -1

    # Count total non-matching characters
    c = 0
    for idx, val in enumerate(str1):
        if str2[idx] != val:
            c += 1

    return c


def generate_matches(data: List[str]) -> List[Tuple[str, str]]:
    """
    Get the
    :param data:
    :return:
    """
    matches = []
    for idx, val in enumerate(data):
        for num in range(idx + 1, len(data)):
            if count_string_differences(val, data[num]) == 1:
                matches.append((val, data[num]))
    return matches


def identify_matched_letters(data: List[Tuple[str, str]]) -> List[str]:
    matches = []
    for _tuple in data:
        match = []

        str1 = _tuple[0]
        str2 = _tuple[1]

        for idx, val in enumerate(str1):
            if str2[idx] == val:
                match.append(val)

        matches.append(''.join(match))

    return matches


def day02b(input_file):
    data = generate_data(input_file)
    matches = generate_matches(data)
    matching_letters = identify_matched_letters(matches)
    if len(matching_letters) == 1:
        return matching_letters.pop()
    print(f'Too many matches: {matches}')
    return False