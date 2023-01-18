import unittest
from typing import List


def fibonacci_search(arr: List[int], x: int) -> int:
    n = len(arr)
    fib2 = 0  # (m-2)'th Fibonacci Number
    fib1 = 1  # (m-1)'th Fibonacci Number
    fib = fib2 + fib1  # m'th Fibonacci
    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1
    while (fib > 1):
        idx = min(offset + fib2, n - 1)
        if (arr[idx] < x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = idx
        elif (arr[idx] > x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return idx
    if(fib1 and arr[offset + 1] == x):
        return offset + 1
    return -1


class TestFibonacciSearch(unittest.TestCase):
    def test_fibonacci_search_basic(self):
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 4)
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8), 7)

    def test_fibonacci_search_not_found(self):
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
        self.assertEqual(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)

    def test_fibonacci_search_edge_cases(self):
        self.assertEqual(fibonacci_search([], 11), -1)
        self.assertEqual(fibonacci_search([1], 1), 0)


if __name__ == '__main__':
    unittest.main()
