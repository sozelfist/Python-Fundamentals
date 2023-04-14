import unittest


def quickselect(arr, k):
    """
    Returns the k-th largest element in the array using the
    Quickselect algorithm.
    """
    if not arr or k > len(arr) or k <= 0:
        raise IndexError("k is out of bounds")

    pivot = arr[0]
    left = [x for x in arr if x > pivot]
    right = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k > len(left) + len(equal):
        return quickselect(right, k - len(left) - len(equal))
    else:
        return equal[0] if len(equal) == 1 else\
            quickselect(equal[1:] + right, k - len(left))


class TestQuickselect(unittest.TestCase):
    def test_kth_largest(self):
        arr = [3, 7, 2, 1, 8, 6, 5, 4]
        self.assertEqual(quickselect(arr, 3), 6)
        self.assertEqual(quickselect(arr, 1), 8)
        self.assertEqual(quickselect(arr, 7), 2)

    def test_kth_smallest(self):
        arr = [3, 7, 2, 1, 8, 6, 5, 4]
        self.assertEqual(quickselect(arr, len(arr) - 2), 3)
        self.assertEqual(quickselect(arr, len(arr) - 1), 2)
        self.assertEqual(quickselect(arr, len(arr)), 1)

    def test_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            quickselect(arr, 1)

    def test_out_of_bounds(self):
        arr = [3, 7, 2, 1, 8, 6, 5, 4]
        with self.assertRaises(IndexError):
            quickselect(arr, 0)
        with self.assertRaises(IndexError):
            quickselect(arr, len(arr) + 1)


if __name__ == '__main__':
    unittest.main()
