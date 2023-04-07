import unittest


def rod_cutting(prices: list[int], n: int) -> int:
    memo = [0] * (n + 1)

    for i in range(1, n + 1):
        max_revenue = 0
        for j in range(i):
            max_revenue = max(max_revenue, prices[j] + memo[i - j - 1])
        memo[i] = max_revenue

    return memo[n]


class TestRodCutting(unittest.TestCase):
    def test_rod_cutting_example_1(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20]
        n = 4

        self.assertEqual(rod_cutting(prices, n), 10)

    def test_rod_cutting_example_2(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20]
        n = 8

        self.assertEqual(rod_cutting(prices, n), 22)

    def test_rod_cutting_empty_rod(self):
        prices = []
        n = 0

        self.assertEqual(rod_cutting(prices, n), 0)

    def test_rod_cutting_single_piece(self):
        prices = [2]
        n = 1

        self.assertEqual(rod_cutting(prices, n), 2)

    def test_rod_cutting_identical_prices(self):
        prices = [5, 5, 5, 5]
        n = 4

        self.assertEqual(rod_cutting(prices, n), 20)

    def test_rod_cutting_large_input(self):
        list(range(1, 101))
        prices = list(range(100, 0, -1))
        n = 100

        self.assertEqual(rod_cutting(prices, n), 10000)


if __name__ == '__main__':
    unittest.main()
