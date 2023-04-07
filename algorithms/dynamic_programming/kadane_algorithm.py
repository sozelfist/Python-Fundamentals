import unittest


def kadane(arr: list[int]) -> int:
    max_so_far = max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here = max(max_ending_here + arr[i], 0)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


class TestKadane(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(kadane([]), 0)

    def test_all_negative(self):
        self.assertEqual(kadane([-1, -2, -3, -4]), 0)

    def test_all_positive(self):
        self.assertEqual(kadane([1, 2, 3, 4]), 10)

    def test_mixed_array(self):
        self.assertEqual(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_single_element(self):
        self.assertEqual(kadane([5]), 5)

    def test_multiple_maximum_subarrays(self):
        self.assertEqual(kadane([-2, 1, -3, 4, -1, 2, 1, 5, -6]), 11)


if __name__ == '__main__':
    unittest.main()
