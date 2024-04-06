import itertools
import unittest
from collections import deque


def moving_average(iterable, n=3, output_type="generator"):
    # moving_average([40, 30, 50, 46, 39, 44]) --> [40.0, 42.0, 45.0, 43.0]
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.extendleft(itertools.repeat(0, n - 1))
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


class TestMovingAverage(unittest.TestCase):
    def test_simple_case(self):
        data = [1, 2, 3, 4, 5]
        expected = [2.0, 3.3333333333333335, 4.666666666666667]
        self.assertEqual(list(moving_average(data, n=3)), expected)

    def test_odd_window_size(self):
        data = [10, 20, 30, 40, 50, 60, 70]
        expected = [
            20.0,
            33.333333333333336,
            46.666666666666664,
            60.0,
            73.33333333333333,
        ]
        self.assertEqual(list(moving_average(data, n=3)), expected)

    def test_even_window_size(self):
        data = [10, 20, 30, 40, 50, 60, 70]
        expected = [25.0, 37.5, 52.5, 67.5]
        self.assertEqual(list(moving_average(data, n=4)), expected)

    def test_empty_input(self):
        data = []
        expected = []
        self.assertEqual(list(moving_average(data)), expected)

    def test_single_value_input(self):
        data = [5]
        expected = []
        self.assertEqual(list(moving_average(data)), expected)


if __name__ == "__main__":
    unittest.main()
