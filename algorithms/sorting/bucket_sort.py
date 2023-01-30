import unittest
from typing import List


def bucket_sort(arr: List[float]) -> List[float]:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(n * arr[i])
        buckets[index].append(arr[i])
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        for val in bucket:
            result.append(val)
    return result


class TestBucketSort(unittest.TestCase):
    def test_bucket_sort_basic(self):
        self.assertEqual(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]), [
                         0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94])
        self.assertEqual(bucket_sort([]), [])


if __name__ == '__main__':
    unittest.main()
