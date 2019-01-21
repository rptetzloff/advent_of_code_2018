from collections import Counter

from advent_of_code_2018.day03.day03 import (
    Rectangle, calculate_points, check_non_overlapped, count_overlaps,
    generate_data, generate_rectangle_points, parse_data_entry,
    day03a,
    day03b,
)


def test_parse_data_entry():
    data = '#1 @ 1,3: 4x4'
    res = parse_data_entry(data)
    assert res == Rectangle(entry=1, origin=(1, 3), size=(4, 4))


def test_generate_data():
    res = generate_data('./files/day03a_test.txt')
    assert res == [Rectangle(entry=1, origin=(1, 3), size=(4, 4)),
                   Rectangle(entry=2, origin=(3, 1), size=(4, 4)),
                   Rectangle(entry=3, origin=(5, 5), size=(2, 2))]


def test_generate_rectangle_points():
    r = Rectangle(entry=1, origin=(1, 3), size=(4, 4))
    res = generate_rectangle_points(r.origin[0], r.origin[1],
                                    r.size[0], r.size[1])
    assert list(res) == [(2, 4),
                         (2, 5),
                         (2, 6),
                         (2, 7),
                         (3, 4),
                         (3, 5),
                         (3, 6),
                         (3, 7),
                         (4, 4),
                         (4, 5),
                         (4, 6),
                         (4, 7),
                         (5, 4),
                         (5, 5),
                         (5, 6),
                         (5, 7)]


def test_calculate_points():
    data = [Rectangle(entry=1, origin=(1, 3), size=(4, 4)),
            Rectangle(entry=2, origin=(3, 1), size=(4, 4)),
            Rectangle(entry=3, origin=(5, 5), size=(2, 2))]
    res = calculate_points(data)
    assert res == Counter({
        (4, 4): 2,
        (4, 5): 2,
        (5, 4): 2,
        (5, 5): 2,
        (2, 4): 1,
        (2, 5): 1,
        (2, 6): 1,
        (2, 7): 1,
        (3, 4): 1,
        (3, 5): 1,
        (3, 6): 1,
        (3, 7): 1,
        (4, 6): 1,
        (4, 7): 1,
        (5, 6): 1,
        (5, 7): 1,
        (4, 2): 1,
        (4, 3): 1,
        (5, 2): 1,
        (5, 3): 1,
        (6, 2): 1,
        (6, 3): 1,
        (6, 4): 1,
        (6, 5): 1,
        (7, 2): 1,
        (7, 3): 1,
        (7, 4): 1,
        (7, 5): 1,
        (6, 6): 1,
        (6, 7): 1,
        (7, 6): 1,
        (7, 7): 1
    })


def test_check_non_overlapped():
    rectangles = [Rectangle(entry=1, origin=(1, 3), size=(4, 4)),
                  Rectangle(entry=2, origin=(3, 1), size=(4, 4)),
                  Rectangle(entry=3, origin=(5, 5), size=(2, 2))]
    counter = Counter({
        (4, 4): 2,
        (4, 5): 2,
        (5, 4): 2,
        (5, 5): 2,
        (2, 4): 1,
        (2, 5): 1,
        (2, 6): 1,
        (2, 7): 1,
        (3, 4): 1,
        (3, 5): 1,
        (3, 6): 1,
        (3, 7): 1,
        (4, 6): 1,
        (4, 7): 1,
        (5, 6): 1,
        (5, 7): 1,
        (4, 2): 1,
        (4, 3): 1,
        (5, 2): 1,
        (5, 3): 1,
        (6, 2): 1,
        (6, 3): 1,
        (6, 4): 1,
        (6, 5): 1,
        (7, 2): 1,
        (7, 3): 1,
        (7, 4): 1,
        (7, 5): 1,
        (6, 6): 1,
        (6, 7): 1,
        (7, 6): 1,
        (7, 7): 1
    })
    res = check_non_overlapped(rectangles, counter)
    assert res == {3}


def test_count_overlaps():
    data = Counter({
        (4, 4): 2,
        (4, 5): 2,
        (5, 4): 2,
        (5, 5): 2,
        (2, 4): 1,
        (2, 5): 1,
        (2, 6): 1,
        (2, 7): 1,
        (3, 4): 1,
        (3, 5): 1,
        (3, 6): 1,
        (3, 7): 1,
        (4, 6): 1,
        (4, 7): 1,
        (5, 6): 1,
        (5, 7): 1,
        (4, 2): 1,
        (4, 3): 1,
        (5, 2): 1,
        (5, 3): 1,
        (6, 2): 1,
        (6, 3): 1,
        (6, 4): 1,
        (6, 5): 1,
        (7, 2): 1,
        (7, 3): 1,
        (7, 4): 1,
        (7, 5): 1,
        (6, 6): 1,
        (6, 7): 1,
        (7, 6): 1,
        (7, 7): 1
    })
    res = count_overlaps(data)
    assert res == 4


def test_day03a():
    res = day03a('./files/day03a_test.txt')
    assert res == 4


def test_day03b():
    res = day03b('./files/day03a_test.txt')
    assert res == {3}
