import unittest
from typing import Any


class Generator:
    """
    A class that generates a range of numbers based on the given parameters.
    """

    def __init__(self, start: float, end: float | None = None, step: float = 1):
        """
        Initializes the Generator with start, end, and step values.

        Args:
            start (float): The starting value of the range.
            end (float | None): The ending value of the range. Defaults to None.
            step (float): The step value for generating the range. Defaults to 1.
        """
        self.start = start
        self.step = step
        if end is not None:
            self.end = end
        else:
            self.end = start
            self.start = 0

    def generate_numbers(self) -> Any:
        """
        Generates a range of numbers based on the provided parameters.

        Yields:
            Any: The generated numbers within the specified range and step.
        """
        yield from range(int(self.start), int(self.end), int(self.step))


class TestGenerator(unittest.TestCase):
    def test_generate_numbers_with_one_argument(self):
        """
        Tests the generation of numbers with a single argument.
        """
        generator = Generator(10)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_generate_numbers_with_two_arguments(self):
        """
        Tests the generation of numbers with two arguments.
        """
        generator = Generator(2, 12)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_generate_numbers_with_step(self):
        """
        Tests the generation of numbers with a custom step.
        """
        generator = Generator(2, 12, step=2)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [2, 4, 6, 8, 10])

    def test_generate_numbers_with_negative_step(self):
        """
        Tests the generation of numbers with a negative step.
        """
        generator = Generator(12, 2, step=-2)
        numbers = list(generator.generate_numbers())
        self.assertEqual(numbers, [12, 10, 8, 6, 4])


if __name__ == "__main__":
    unittest.main()
