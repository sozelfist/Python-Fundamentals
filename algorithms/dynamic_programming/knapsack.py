import unittest
from typing import List, Tuple


def knapsack(items: List[Tuple[int, int]], capacity: int) -> int:
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[n][capacity]


class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 50), 220)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 0), 0)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 30), 160)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 60), 280)
        self.assertEqual(knapsack([], 60), 0)
        self.assertEqual(knapsack([(100, 100), (100, 100)], 10), 0)


if __name__ == '__main__':
    unittest.main()
