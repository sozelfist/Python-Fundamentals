import unittest
from math import comb


def catalan_number(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def generate_catalan_numbers(n: int) -> list[int]:
    return [catalan_number(i) for i in range(n)]


class TestCatalanNumbers(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_generate_catalan_numbers(self):
        self.assertEqual(generate_catalan_numbers(5), [1, 1, 2, 5, 14])


if __name__ == '__main__':
    unittest.main()
