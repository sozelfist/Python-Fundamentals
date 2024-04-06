import unittest


def fibonacci_search(arr: list[int], x: int) -> int:
    if not arr:
        return -1
    n = len(arr)
    fib2 = 0  # (m-2)'th Fibonacci Number
    fib1 = 1  # (m-1)'th Fibonacci Number
    fib = fib2 + fib1  # m'th Fibonacci
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1
    while fib > 1:
        idx = min(offset + fib2, n - 1)
        if arr[idx] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = idx
        elif arr[idx] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return idx
    if fib1 and arr[offset + 1] == x:
        return offset + 1
    return -1


class TestFibonacciSearch(unittest.TestCase):
    def test_empty_list(self):
        result = fibonacci_search([], 2)
        self.assertEqual(result, -1)

    def test_element_not_present(self):
        result = fibonacci_search([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)

    def test_element_present_at_first_index(self):
        result = fibonacci_search([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, 0)

    def test_element_present_at_last_index(self):
        result = fibonacci_search([1, 2, 3, 4, 5], 5)
        self.assertEqual(result, 4)

    def test_element_present_in_middle(self):
        result = fibonacci_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
