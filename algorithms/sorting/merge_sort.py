import unittest


def merge_lists(left: list[int], right: list[int]) -> list[int]:
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_lists(left, right)


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_list_of_length_one(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_sorting_of_already_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorting_of_unsorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sorting_of_list_with_duplicate_elements(self):
        self.assertEqual(merge_sort([5, 4, 5, 2, 1]), [1, 2, 4, 5, 5])

    def test_sorting_of_list_with_all_duplicate_elements(self):
        self.assertEqual(merge_sort([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_sorting_of_list_with_negative_elements(self):
        self.assertEqual(merge_sort([-1, -5, -3, -2, -4]), [-5, -4, -3, -2, -1])

    def test_sorting_of_list_with_empty_list(self):
        self.assertEqual(merge_sort([]), [])


if __name__ == '__main__':
    unittest.main()
