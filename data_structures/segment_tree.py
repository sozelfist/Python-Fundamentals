from typing import List
import unittest


class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr: List[int], v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, 2 * v, tl, tm)
            self.build(arr, 2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self._query(2 * v, tl, tm, l, min(r, tm)) + self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def update(self, pos: int, val: int) -> None:
        self._update(1, 0, self.n - 1, pos, val)

    def _update(self, v: int, tl: int, tr: int, pos: int, val: int) -> None:
        if tl == tr:
            self.tree[v] = val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(2 * v, tl, tm, pos, val)
            else:
                self._update(2 * v + 1, tm + 1, tr, pos, val)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]


class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        self.arr = [1, 3, 2, 4, 5, 7, 6, 8]
        self.seg_tree = SegmentTree(self.arr)

    def test_query(self):
        self.assertEqual(self.seg_tree.query(2, 5), 18)
        self.assertEqual(self.seg_tree.query(1, 7), 35)
        self.assertEqual(self.seg_tree.query(0, 7), 36)

    def test_update(self):
        self.seg_tree.update(3, 9)
        self.assertEqual(self.seg_tree.query(2, 5), 23)
        self.assertEqual(self.seg_tree.query(1, 7), 40)
        self.assertEqual(self.seg_tree.query(0, 7), 41)


if __name__ == '__main__':
    unittest.main()
