import unittest
from typing import List


def insertion_sort(arr: List[int], left=0, right=None) -> List[int]:
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge(left: List[int], right: List[int]) -> List[int]:
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:

        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def timsort(arr: List[int]) -> List[int]:
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1]
            )
            arr[start:start + len(merged_array)] = merged_array
        size *= 2
    return arr


class TestTimsort(unittest.TestCase):
    def test_timsort_basic(self):
        self.assertEqual(timsort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])
        self.assertEqual(timsort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(timsort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(timsort([1]), [1])
        self.assertEqual(timsort([]), [])

    def test_timsort_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(timsort(arr), sorted(arr))

    def test_timsort_reverse_sorted(self):
        arr = [6, 5, 4, 3, 2, 1]
        self.assertEqual(timsort(arr), sorted(arr))

    def test_timsort_with_duplicates(self):
        arr = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]
        self.assertEqual(timsort(arr), sorted(arr))


if __name__ == '__main__':
    unittest.main()
