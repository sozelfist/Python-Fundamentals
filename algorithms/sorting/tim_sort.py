import bisect
import unittest


def insertion_sort(arr: list[int], left=0, right=None) -> list[int]:
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = bisect.bisect_left(arr[:i], key_item, lo=left, hi=i)
        arr[j + 1:i + 1] = arr[j:i]
        arr[j] = key_item
    return arr


def merge(left: list[int], right: list[int]) -> list[int]:
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:

        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def timsort(arr: list[int]) -> list[int]:
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


class TestTimSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_random_unsorted(self):
        arr = [3, 5, 2, 1, 4]
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [3, 5, 3, 1, 4]
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [1, 3, 3, 4, 5])

    def test_negative_elements(self):
        arr = [3, -5, 2, -1, 4]
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [-5, -1, 2, 3, 4])

    def test_empty_list(self):
        arr = []
        sorted_arr = timsort(arr)
        self.assertEqual(sorted_arr, [])


if __name__ == '__main__':
    unittest.main()
