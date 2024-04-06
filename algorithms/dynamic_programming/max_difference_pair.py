import unittest


def max_difference_pairs(arr: list[int]) -> tuple[int, tuple[int, int]]:
    """
    Finds the maximum difference between pairs of elements in an array.

    Args:
        arr (List[int]): Input array of integers.

    Returns:
        Tuple[int, Tuple[int, int]]: Maximum difference between pairs
        of elements and the pair (i, j) where arr[i] and arr[j] gives
        the maximum difference.
    """
    if not arr or len(arr) < 2:
        return 0, None

    min_val = arr[0]
    max_diff = 0
    max_pair = (0, 0)

    strictly_decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > min_val:
            if arr[i] - min_val > max_diff:
                max_diff = arr[i] - min_val
                max_pair = (min_val, arr[i])
            strictly_decreasing = False
        elif arr[i] == min_val:
            continue
        else:
            min_val = arr[i]

    if strictly_decreasing:
        return 0, None

    return max_diff, max_pair


class TestMaxDifferencePairs(unittest.TestCase):
    def test_max_difference_pairs_empty_array(self):
        arr = []
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 0)
        self.assertIsNone(max_pair)

    def test_max_difference_pairs_single_element_array(self):
        arr = [5]
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 0)
        self.assertIsNone(max_pair)

    def test_max_difference_pairs_increasing_order(self):
        arr = [1, 2, 3, 4, 5]
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 4)
        self.assertEqual(max_pair, (1, 5))

    def test_max_difference_pairs_decreasing_order(self):
        arr = [5, 4, 3, 2, 1]
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 0)
        self.assertIsNone(max_pair)

    def test_max_difference_pairs_mixed_order(self):
        arr = [1, 3, 2, 4, 5]
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 4)
        self.assertEqual(max_pair, (1, 5))

    def test_max_difference_pairs_duplicate_elements(self):
        arr = [1, 3, 3, 4, 4, 5]
        max_diff, max_pair = max_difference_pairs(arr)
        self.assertEqual(max_diff, 4)
        self.assertEqual(max_pair, (1, 5))


if __name__ == "__main__":
    unittest.main()
