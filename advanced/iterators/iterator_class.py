import unittest
from typing import Union


class Iterator:
    def __init__(self, start: int, stop: Union[int, None] = None, step: int = 1):
        if step == 0:
            raise ValueError("step cannot be 0")
        self.step = step
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        if self.step > 0:
            if self.start >= self.stop:
                raise ValueError("start must be less than stop with positive step")
        else:
            if self.start <= self.stop:
                raise ValueError("start must be greater than stop with negative step")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start < self.stop:
            current = self.start
            self.start += self.step
            return current
        elif self.step < 0 and self.start > self.stop:
            current = self.start
            self.start += self.step
            return current
        else:
            raise StopIteration


class TestIterator(unittest.TestCase):
    def test_iterator_with_two_arguments(self):
        it = Iterator(0, 5)
        self.assertEqual(list(it), [0, 1, 2, 3, 4])

    def test_iterator_with_three_arguments(self):
        it = Iterator(0, 5, 2)
        self.assertEqual(list(it), [0, 2, 4])

    def test_iterator_with_one_argument(self):
        it = Iterator(5)
        self.assertEqual(list(it), [0, 1, 2, 3, 4])

    def test_iterator_with_negative_step(self):
        it = Iterator(5, 0, -1)
        self.assertEqual(list(it), [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
