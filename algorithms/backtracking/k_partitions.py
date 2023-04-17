import unittest


def k_partition(S: list[int], K: int) -> tuple[list[list[int]], int]:
    """
    Partitions a set S into K subsets with equal sum.

    Args:
        S: A list of positive integers representing the set to be partitioned
        K: An integer representing the number of subsets to partition S into

    Returns:
        A tuple containing:
            - A list of lists, each representing a subset in the partition
            - An integer representing the number of partitions
    """

    if not S:
        raise ValueError("Cannot partition on an empty array")

    total_sum = sum(S)
    if total_sum % K != 0:
        raise ValueError("Cannot partition set into equal sum subsets")

    target_sum = total_sum // K
    n = len(S)
    partition = [[] for _ in range(K)]

    def backtrack(index: int, current_sum: int, remaining_sets: int) -> bool:
        if remaining_sets == 0:
            return True
        if current_sum > target_sum:
            return False
        if current_sum == target_sum:
            return backtrack(0, 0, remaining_sets - 1)

        for i in range(index, n):
            if not used[i]:
                used[i] = True
                partition[remaining_sets - 1].append(S[i])
                if backtrack(i + 1, current_sum + S[i], remaining_sets):
                    return True
                partition[remaining_sets - 1].pop()
                used[i] = False

        return False

    used = [False] * n
    if not backtrack(0, 0, K):
        raise ValueError("Cannot partition set into equal sum subsets")

    return partition, K


class TestKPartition(unittest.TestCase):

    def test_k_partition(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        K = 3
        expected_partitions = [[7, 8], [6, 9], [1, 2, 3, 4, 5]]
        expected_num_partitions = 3
        partitions, num_partitions = k_partition(S, K)
        self.assertEqual(partitions, expected_partitions)
        self.assertEqual(num_partitions, expected_num_partitions)

    def test_k_partition_empty_set(self):
        S = []
        K = 3
        with self.assertRaises(ValueError):
            partitions, num_partitions = k_partition(S, K)

    def test_k_partition_impossible_partition(self):
        S = [1, 2, 3, 4, 5]
        K = 4
        with self.assertRaises(ValueError):
            partitions, num_partitions = k_partition(S, K)

    def test_k_partition_large_set(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        K = 5
        expected_partitions = [
            [11, 13], [10, 14], [9, 15],
            [5, 7, 12], [1, 2, 3, 4, 6, 8]
        ]
        expected_num_partitions = 5
        partitions, num_partitions = k_partition(S, K)
        self.assertEqual(partitions, expected_partitions)
        self.assertEqual(num_partitions, expected_num_partitions)


if __name__ == '__main__':
    unittest.main()
