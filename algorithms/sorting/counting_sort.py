import unittest


def counting_sort(arr: list[int], exp: int):
    n = len(arr)
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    output = [0] * n
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

    return arr


class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(counting_sort([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(counting_sort([42], 1), [42])

    def test_sorted_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(counting_sort([5, 4, 3, 2, 1], 1), [1, 2, 3, 4, 5])

    def test_negative_elements(self):
        self.assertEqual(
            counting_sort([-5, -4, -3, -2, -1], 1),
            [-5, -4, -3, -2, -1]
        )


if __name__ == '__main__':
    unittest.main()
