import os
from typing import List, Set


def generate_data(input_file: str) -> List[int]:
    """
    Generate list of integers from input file
    :param input_file: (str) location of input file to use
    :return: list of integers of values generated from input file
    """
    # Initialize list
    data = []
    with open(os.path.abspath(input_file), 'r') as f_in:
        # Add integer values of lines to list
        for i in f_in:
            data.append(int(i.strip()))

    # Return list
    return data


def calculate_frequency(data: List[int]):
    """
    Calculate final frequency after running through frequency changes in list
    :param data: List of ints
    :return: int of final frequency
    """
    # Initialize frequency
    frequency = 0

    # For each data point, add value and yield
    for change in data:
        result = frequency + change
        yield result


def day01a(input_file):
    """
    The solver for Day 1, part A.
    :param input_file: (str) The input file of data from Advent of Code
    :return: (int) The frequency (solution) of the problem
    """
    # Initialize frequency
    frequency = 0

    # Generate list from input file
    data = generate_data(input_file)

    # Initialize generator
    res = calculate_frequency(data)

    # Run through generator and add to frequency
    for i in res:
        frequency += i

    # Return result
    return frequency


def is_duplicate(value: int, results: Set[int]) -> bool:
    """
    Part B of Day 1 requires checking to see if a value has been duplicated
    in a stored list of resulting frequencies. This checks to see which of
    those have already been returned
    :param value: (int) A frequency to check
    :param results: (Set[int]) A set, containing all unique values of the
    resulting frequencies.
    :return: (bool) True, if frequency has been seen; False, if it has not
    """
    if value in results:
        return True
    return False


def day01b(input_file):
    """
    The solver for day 1, part B of Advent of Code 2018.
    :param input_file: (str) input file of data provided
    :return: (int) The frequency that is first duplicated.
    """
    # Generate list of frequency changes from input file
    data = generate_data(input_file)

    # Initialize frequency
    frequency = 0

    # Initialize frequency set with 0 is the starting value
    frequencies = {frequency}

    # Initialize boolean for while loop
    duplicated = False

    # Loop through calculate_frequency until a duplicate is found
    # TODO: Simplify this
    while not duplicated:
        # Initialize generator
        res = calculate_frequency(data)

        # Loop through generator, like day01a, but check for a duplicate
        # after each frequency is added
        for i in res:
            frequency += i

            # If frequency is duplicated, break loop
            if is_duplicate(frequency, frequencies):
                duplicated = True
                break

            # Insert frequency into frequencies set and proceed
            frequencies.add(frequency)

    # Return the frequency value
    return frequency
