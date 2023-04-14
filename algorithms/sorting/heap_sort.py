import unittest


def heap_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    return arr


def _heapify(arr: list[int], n: int, i: int):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        self.assertEqual(heap_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(heap_sort([5, 2, 9, 1, 5]), [1, 2, 5, 5, 9])
        self.assertEqual(
            heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertEqual(
            heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])
        self.assertEqual(heap_sort([-5, 2, 9, 1, -2]), [-5, -2, 1, 2, 9])


if __name__ == '__main__':
    unittest.main()
