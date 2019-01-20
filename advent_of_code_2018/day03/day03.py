"""
The number of inches between the left edge of the fabric and the left edge
of the rectangle.
The number of inches between the top edge of the fabric and the top edge of
the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
"""
import os
import re
from collections import Counter, namedtuple
from typing import List

Rectangle = namedtuple('Rectangle', 'entry, origin, size')


def parse_data_entry(data):
    regex = re.compile(
        r'#(?P<entry>\d+)\s+@\s+(?P<left>\d+),(?P<top>\d+):\s+('
        r'?P<width>\d+)x(?P<height>\d+)')

    match = re.match(regex, data)

    entry = int(match.group('entry'))
    left = int(match.group('left'))
    top = int(match.group('top'))
    width = int(match.group('width'))
    height = int(match.group('height'))

    return Rectangle(entry=entry, origin=(left, top), size=(width, height))


def generate_data(input_file):
    rectangles = []
    with open(os.path.abspath(input_file), 'r') as f_in:
        for i in f_in:
            rectangle = parse_data_entry(i)
            rectangles.append(rectangle)

    return rectangles


def generate_rectangle_points(left, top, width, height):
    rectangle = set()
    for x in range(left + 1, left + width + 1):
        for y in range(top + 1, top + height + 1):
            yield (x, y)


def calculate_points(data: List[Rectangle]):
    c = Counter()
    for i in data:
        rectangle = generate_rectangle_points(i.origin[0], i.origin[1],
                                              i.size[0], i.size[1])
        for point in rectangle:
            c.update([point])

    return c


def check_non_overlapped(rectangles: List[Rectangle], counter: Counter):
    non_overlaps = {key for key, val in counter.items() if val == 1}
    unique_rectangles = set()
    for rectangle in rectangles:
        points = set(generate_rectangle_points(rectangle.origin[0],
                                                  rectangle.origin[1],
                                                  rectangle.size[0],
                                                  rectangle.size[1]))
        if points.issubset(non_overlaps):
            unique_rectangles.add(rectangle.entry)

    return unique_rectangles


def count_overlaps(data: Counter) -> int:
    duplicates = [val for val in data.values() if 1 < val]
    return len(duplicates)


def day03a(input_file):
    data = generate_data(input_file)
    c = calculate_points(data)
    return count_overlaps(c)


def day03b(input_file):
    data = generate_data(input_file)
    c = calculate_points(data)
    return check_non_overlapped(data, c)
