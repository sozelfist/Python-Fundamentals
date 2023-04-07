import unittest
from typing import Any


class Generator:
    def __init__(self, start: int | float, end: int | float | None = None, step: int | float = 1):
        self.start = start
        self.step = step
        if end is not None:
            self.end = end
        else:
            self.end = start
            self.start = 0

    def generate_numbers(self) -> Any:
        yield from range(int(self.start), int(self.end), int(self.step))


class TestGenerator(unittest.TestCase):
    def test_generate_numbers_with_one_argument(self):
        generator = Generator(10)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_generate_numbers_with_two_arguments(self):
        generator = Generator(2, 12)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_generate_numbers_with_step(self):
        generator = Generator(2, 12, step=2)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [2, 4, 6, 8, 10])

    def test_generate_numbers_with_negative_step(self):
        generator = Generator(12, 2, step=-2)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [12, 10, 8, 6, 4])


if __name__ == '__main__':
    unittest.main()
