import os
import re
from collections import Counter, namedtuple
from typing import List, Tuple, Set
from typing import Counter as CounterType

# Rectangle is a named tuple for cleaning information provided by data
Rectangle = namedtuple('Rectangle', 'entry, origin, size')


def parse_data_entry(data: str) -> Rectangle:
    """
    Parse a line of data and generate entry ID, origin, and size of rectangle
    :param data: (str) A line of data identifying a rectangle.
    :return: (Rectangle) A namedtuple provider usable information of the rectangle
    """
    # TODO: Do this without regex?
    # Compile a list of attributes to find using regex
    regex = re.compile(
        r'#(?P<entry>\d+)\s+@\s+(?P<left>\d+),(?P<top>\d+):\s+('
        r'?P<width>\d+)x(?P<height>\d+)')

    # Match string to regex
    match = re.match(regex, data)

    # Make matching information easier to use
    entry = int(match.group('entry'))
    left = int(match.group('left'))
    top = int(match.group('top'))
    width = int(match.group('width'))
    height = int(match.group('height'))

    # return rectangle information in a rectangle namedtuple
    return Rectangle(entry=entry, origin=(left, top), size=(width, height))


def generate_data(input_file: str) -> List[Rectangle]:
    """
    Take a data input file and convert to a list
    :param input_file: (str) Data input file
    :return: (List[Rectangle]) a list of namedtuples from the input file
    """
    # Initialize list
    rectangles = []

    # Parse data in each line of the file
    with open(os.path.abspath(input_file), 'r') as f_in:
        for i in f_in:
            # Parse string from file into named tuple
            rectangle = parse_data_entry(i)
            # Add Rectangle to list
            rectangles.append(rectangle)

    # Return list
    return rectangles


def generate_rectangle_points(left: int, top: int, width: int, height: int) -> List[Tuple[int, int]]:
    """
    Generate a list of points that the rectangle occupies.
    :param left: (int) The number of spaces from origin to left side of rectangle.
    :param top: (int) The number of spaces from origin to top of rectangle.
    :param width: (int) The width of the rectangle
    :param height: (int) The height of the rectangle
    :return: (List[Tuple[int, int]]) a list of points which the rectangle occupies.
    """
    # Initialize a set of points that the rectangle consumes
    # We only care about unique points, because a rectangle will not overlap itself
    rectangle = set()

    # Loop through each point in x direction
    for x in range(left + 1, left + width + 1):
        # Loop through each point in y direction
        for y in range(top + 1, top + height + 1):
            # Yield each point of the rectangle
            yield (x, y)


def calculate_points(data: List[Rectangle]) -> CounterType:
    """
    Create a counter of all points and the number of rectangles which occupy that space.
    :param data: (List[Rectangle]) a list of rectangles
    :return: (Counter) a count of the number of rectangles occupying each space
    """
    # Initialize counter
    c = Counter()

    # Loop through all rectangles
    for i in data:
        # Get list of points the current rectangle occupies
        rectangle = generate_rectangle_points(i.origin[0], i.origin[1],
                                              i.size[0], i.size[1])

        # For each point, update the counter
        for point in rectangle:
            # Increment the counter value for the given point.
            # The value to update must be the list
            # TODO: Try changing this to a tuple to identify the point
            c.update([point])

    # Return the counter
    return c


def check_non_overlapped(rectangles: List[Rectangle], counter: Counter) -> Set[int]:
    """
    Get a list of rectangles that do not overlap any other rectangle
    :param rectangles: (List[Rectangle]) A list of rectangles
    :param counter: (Counter) a counter of how many rectangles occupy each point
    :return: (Set[Rectangle]) A set containing any rectangle that occupies entirely unique points
    """
    # Get a list of points which are occupied only by a single rectangle
    non_overlaps = {key for key, val in counter.items() if val == 1}

    # Initialize result set
    unique_rectangles = set()

    # Loop through rectangle list to find non-overlapping rectangles
    for rectangle in rectangles:
        # get a list of points that the rectangle occupies
        points = set(generate_rectangle_points(rectangle.origin[0],
                                               rectangle.origin[1],
                                               rectangle.size[0],
                                               rectangle.size[1]))

        # If all of the rectangle's points are only occupied by this rectangle, add it to the results
        if points.issubset(non_overlaps):
            # Add entry number of rectangle to results
            unique_rectangles.add(rectangle.entry)

    # Return results
    return unique_rectangles


def count_overlaps(data: Counter) -> int:
    """
    Count the number of data points which are occupied by more than one rectangle.
    :param data: (str) A counter containing a list of data points
    :return: (int) the number of duplicated points
    """
    # Any point occupied by more than one rectangle gets added to the list
    duplicates = [val for val in data.values() if 1 < val]

    # Return the number of duplicate points
    return len(duplicates)


def day03a(input_file: str) -> int:
    """
    Solver for part 1 of day 3 of Advent of Code 2018. This wants a count of the number of
    points occupied by multiple rectangles.
    :param input_file: (str) a data input file using the AoC generated data for day 3
    :return: (int) the number of points occupied by overlapping rectangles
    """
    # Make list of rectangles
    data = generate_data(input_file)

    # Generate a counter of points occupied by some number of rectangles
    c = calculate_points(data)

    # Return the number of points occupied by multiple rectangles
    return count_overlaps(c)


def day03b(input_file: str) -> Set[int]:
    """
    Solver for part 2 of day 3 of Advent of Code 2018. This wants the entry ID of a rectangle that
    does not overlap with any other rectangle.
    :param input_file: (str) a data input file using the AoC generated data for day 3
    :return: (Set) a set of rectangles that do not overlap with other rectangles
    """
    # Make list of rectangles
    data = generate_data(input_file)

    # Calculate points occupied by rectangles
    c = calculate_points(data)

    # Check to see which rectangles do not overlap with other rectangles
    return check_non_overlapped(data, c)
