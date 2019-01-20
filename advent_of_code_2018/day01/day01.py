import os
from typing import List, Set


def generate_data(input_file):
    data = []
    with open(os.path.abspath(input_file), 'r') as f_in:
        for i in f_in:
            data.append(int(i.strip()))

    return data


def calculate_frequency(data: List[int]):
    """
    Calculate frequency
    :param data: List of ints
    :return: int of final value
    """
    frequency = 0

    for change in data:
        result = frequency + change
        yield result


def day01a(input_file):
    frequency = 0
    data = generate_data(input_file)
    res = calculate_frequency(data)
    for i in res:
        frequency += i

    return frequency


def is_duplicate(value: int, results: Set[int]) -> bool:
    if value in results:
        return True
    return False


def day01b(input_file):
    data = generate_data(input_file)
    frequency = 0
    frequencies = {frequency}
    duplicated = False

    while not duplicated:
        res = calculate_frequency(data)

        for i in res:
            frequency += i

            if is_duplicate(frequency, frequencies):
                duplicated = True
                break

            frequencies.add(frequency)

    return frequency
