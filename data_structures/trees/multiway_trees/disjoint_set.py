import unittest


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x: int):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.make_set(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[self.parent[x]])
        return self.parent[x]

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.ds = DisjointSet()

    def test_make_set(self):
        self.ds.make_set(1)
        self.ds.make_set(2)
        self.ds.make_set(3)
        self.assertEqual(self.ds.parent, {1: 1, 2: 2, 3: 3})
        self.assertEqual(self.ds.rank, {1: 0, 2: 0, 3: 0})

    def test_find_set(self):
        self.ds.make_set(1)
        self.ds.make_set(2)
        self.ds.make_set(3)
        self.ds.union(1, 2)
        self.assertEqual(self.ds.find(1), 1)
        self.assertEqual(self.ds.find(2), 1)
        self.assertEqual(self.ds.find(3), 3)

    def test_union(self):
        self.ds.make_set(1)
        self.ds.make_set(2)
        self.ds.make_set(3)
        self.ds.union(1, 2)
        self.ds.union(2, 3)
        self.assertEqual(self.ds.parent, {1: 1, 2: 1, 3: 1})


if __name__ == '__main__':
    unittest.main()
