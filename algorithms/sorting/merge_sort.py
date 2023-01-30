import unittest
from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([-1, 2, -3]), [-3, -1, 2])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([]), [])


if __name__ == '__main__':
    unittest.main()
