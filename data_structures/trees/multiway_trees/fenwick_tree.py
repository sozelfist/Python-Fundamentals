import unittest


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i: int) -> int:
        cumulative_sum = 0
        while i > 0:
            cumulative_sum += self.tree[i]
            i -= i & -i
        return cumulative_sum

    def range_query(self, i: int, j: int) -> int:
        return self.query(j) - self.query(i - 1)


class TestFenwickTree(unittest.TestCase):
    def setUp(self) -> None:
        self.ft = FenwickTree(5)

    def test_query(self):
        self.ft.update(1, 2)
        self.ft.update(2, 3)
        self.ft.update(3, 1)
        self.assertEqual(self.ft.query(4), 6)
        self.assertEqual(self.ft.query(3), 6)
        self.assertEqual(self.ft.query(2), 5)
        self.assertEqual(self.ft.query(1), 2)
        self.assertEqual(self.ft.query(0), 0)

    def test_range_query(self):
        self.ft.update(1, 2)
        self.ft.update(2, 3)
        self.ft.update(3, 1)
        self.assertEqual(self.ft.range_query(2, 4), 4)
        self.assertEqual(self.ft.range_query(1, 3), 6)
        self.assertEqual(self.ft.range_query(3, 5), 1)
        self.assertEqual(self.ft.range_query(1, 5), 6)
        self.assertEqual(self.ft.range_query(2, 2), 3)

    def test_update(self):
        self.ft.update(1, 2)
        self.assertEqual(self.ft.query(1), 2)
        self.ft.update(1, -1)
        self.assertEqual(self.ft.query(1), 1)
        self.ft.update(3, 4)
        self.assertEqual(self.ft.query(4), 5)
        self.ft.update(4, -1)
        self.assertEqual(self.ft.query(4), 4)


if __name__ == "__main__":
    unittest.main()
