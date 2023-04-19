import unittest
from functools import cache

# from typing import Dict


# manual way to calculate factorial of n with dictionary caching
# factorial_lookup: Dict[int, int] = {0: 1}

# def factorial(n: int) -> int:
#     """
#     Returns the factorial of a non-negative integer n.
#     """
#     if n not in factorial_lookup:
#         factorial_lookup[n] = n * factorial(n-1)
#     return factorial_lookup[n]


@cache
def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer n.
    Raises a ValueError if n is negative.
    Raises a TypeError if n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    elif n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def test_factorial_base_case(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_small_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_invalid_input(self):
        with self.assertRaises((TypeError, ValueError)):
            factorial(3.14)
        with self.assertRaises((TypeError, ValueError)):
            factorial('5')


if __name__ == '__main__':
    unittest.main()
