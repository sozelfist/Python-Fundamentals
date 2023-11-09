import unittest


class Iterator:
    """
    A custom iterator that iterates over a range of numbers based on the provided parameters.
    """

    def __init__(self, start: int, stop: int | None = None, step: int = 1):
        """
        Initializes the Iterator with start, stop, and step values.

        Args:
            start (int): The starting value of the range.
            stop (int | None): The ending value of the range. Defaults to None.
            step (int): The step value for iterating the range. Defaults to 1.

        Raises:
            ValueError: If the step is 0 or the start and stop values are not compatible with the step.
        """
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
                raise ValueError("start must be less than stop with a positive step")
        else:
            if self.start <= self.stop:
                raise ValueError("start must be greater than stop with a negative step")

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the range based on the step value.

        Returns:
            int: The next element in the range.

        Raises:
            StopIteration: If the iteration is complete.
        """
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
        """
        Tests the Iterator with start and stop arguments.
        """
        it = Iterator(0, 5)
        self.assertEqual(list(it), [0, 1, 2, 3, 4])

    def test_iterator_with_three_arguments(self):
        """
        Tests the Iterator with start, stop, and step arguments.
        """
        it = Iterator(0, 5, 2)
        self.assertEqual(list(it), [0, 2, 4])

    def test_iterator_with_one_argument(self):
        """
        Tests the Iterator with a single argument.
        """
        it = Iterator(5)
        self.assertEqual(list(it), [0, 1, 2, 3, 4])

    def test_iterator_with_negative_step(self):
        """
        Tests the Iterator with a negative step.
        """
        it = Iterator(5, 0, -1)
        self.assertEqual(list(it), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
