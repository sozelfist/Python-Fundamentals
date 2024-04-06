import unittest


def coin_change(coins: list[int], amount: int) -> int | float:
    dp = [float("inf") for _ in range(amount + 1)]
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


class TestCoinChange(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([186, 419, 83, 408], 6249), 20)
        self.assertEqual(coin_change([1, 3, 5], 8), 2)


if __name__ == "__main__":
    unittest.main()
