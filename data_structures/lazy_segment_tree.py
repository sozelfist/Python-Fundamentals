import unittest
from typing import List


class LazySegmentTree:
    def __init__(self, arr: List[int]) -> None:
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr: List[int], v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self._build(arr, 2 * v, tl, tm)
            self._build(arr, 2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def _push(self, v: int, tl: int, tr: int) -> None:
        if self.lazy[v] != 0:
            self.tree[v] += (tr - tl + 1) * self.lazy[v]
            if tl != tr:
                self.lazy[2 * v] += self.lazy[v]
                self.lazy[2 * v + 1] += self.lazy[v]
            self.lazy[v] = 0

    def _update(self, v: int, tl: int, tr: int, l: int, r: int, add: int) -> None:
        self._push(v, tl, tr)
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] += add
            self._push(v, tl, tr)
        else:
            tm = (tl + tr) // 2
            self._update(2 * v, tl, tm, l, min(r, tm), add)
            self._update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def _query(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        self._push(v, tl, tr)
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self._query(2 * v, tl, tm, l, min(r, tm)) + self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def range_update(self, l: int, r: int, add: int) -> None:
        self._update(1, 0, self.n - 1, l, r, add)

    def range_query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.n - 1, l, r)


class TestLazySegmentTree(unittest.TestCase):
    def test_range_query(self):
        arr = [1, 3, 2, 4, 5]
        tree = LazySegmentTree(arr)
        result = tree.range_query(0, 4)
        expected = 15
        self.assertEqual(result, expected)

    def test_range_update_query(self):
        arr = [1, 3, 2, 4, 5]
        tree = LazySegmentTree(arr)
        tree.range_update(1, 3, 2)
        result = tree.range_query(0, 4)
        expected = 21
        self.assertEqual(result, expected)

    def test_multiple_range_queries(self):
        arr = [1, 3, 2, 4, 5]
        tree = LazySegmentTree(arr)
        result1 = tree.range_query(0, 2)
        result2 = tree.range_query(2, 4)
        expected1 = 6
        expected2 = 11
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

    def test_out_of_range_updates(self):
        arr = [1, 3, 2, 4, 5]
        tree = LazySegmentTree(arr)
        with self.assertRaises(IndexError):
            tree.range_update(-1, 2, 2)
        with self.assertRaises(IndexError):
            tree.range_update(1, 6, 2)

    def test_out_of_range_queries(self):
        arr = [1, 3, 2, 4, 5]
        tree = LazySegmentTree(arr)
        with self.assertRaises(IndexError):
            tree.range_query(-1, 2)
        with self.assertRaises(IndexError):
            tree.range_query(1, 6)


if __name__ == '__main__':
    unittest.main()
