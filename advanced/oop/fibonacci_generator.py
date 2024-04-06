import unittest


class FibonacciNumbers:
    def __init__(self, limit: int):
        self.limit = limit
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.first >= self.limit:
            raise StopIteration
        next = self.first
        self.first, self.second = self.second, self.first + self.second
        return next


class TestFibonacciNumbers(unittest.TestCase):
    def test_fibonacci_numbers(self):
        fib = FibonacciNumbers(limit=100)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        result = [i for i in fib]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
