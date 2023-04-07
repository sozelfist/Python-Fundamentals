import unittest


def bucket_sort(arr: list[float]) -> list[float]:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(n * arr[i])
        buckets[index].append(arr[i])
    return [val for bucket in buckets for val in sorted(bucket)]


class TestBucketSort(unittest.TestCase):
    def test_already_sorted(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        sorted_arr = bucket_sort(arr)
        self.assertEqual(sorted_arr, [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_reverse_sorted(self):
        arr = [0.5, 0.4, 0.3, 0.2, 0.1]
        sorted_arr = bucket_sort(arr)
        self.assertEqual(sorted_arr, [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_random_unsorted(self):
        arr = [0.3, 0.5, 0.2, 0.1, 0.4]
        sorted_arr = bucket_sort(arr)
        self.assertEqual(sorted_arr, [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_duplicates(self):
        arr = [0.3, 0.5, 0.3, 0.1, 0.4]
        sorted_arr = bucket_sort(arr)
        self.assertEqual(sorted_arr, [0.1, 0.3, 0.3, 0.4, 0.5])


if __name__ == '__main__':
    unittest.main()
