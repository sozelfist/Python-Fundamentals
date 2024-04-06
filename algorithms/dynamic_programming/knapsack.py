import unittest


def knapsack(items: list[tuple[int, int]], capacity: int) -> int:
    len(items)
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 50), 220)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 0), 0)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 30), 160)
        self.assertEqual(knapsack([(10, 60), (20, 100), (30, 120)], 60), 280)
        self.assertEqual(knapsack([], 60), 0)
        self.assertEqual(knapsack([(100, 100), (100, 100)], 10), 0)


if __name__ == "__main__":
    unittest.main()
