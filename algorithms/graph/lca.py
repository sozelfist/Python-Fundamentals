import unittest


class LCA:
    def __init__(self, tree, root):
        self.tree = tree
        self.root = root
        self.log_n = (len(tree) - 1).bit_length()
        self.parent = [[-1] * len(tree) for _ in range(self.log_n + 1)]
        self.depth = [0] * len(tree)
        self._dfs(root, -1)

        for k in range(1, self.log_n + 1):
            for v in range(len(tree)):
                if self.parent[k - 1][v] != -1:
                    self.parent[k][v] = self.parent[k - 1][self.parent[k - 1][v]]

    def _dfs(self, v, p):
        self.parent[0][v] = p
        self.depth[v] = self.depth[p] + 1
        for child in self.tree[v]:
            if child != p:
                self._dfs(child, v)

    def query(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.log_n, -1, -1):
            if self.depth[v] - (1 << k) >= self.depth[u]:
                v = self.parent[k][v]
        if u == v:
            return u
        for k in range(self.log_n, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


class TestLCA(unittest.TestCase):
    def test_lca_on_simple_binary_tree(self):
        # Test a simple binary tree
        tree = [[1, 2], [], []]
        lca = LCA(tree, 0)
        self.assertEqual(lca.query(1, 2), 0)
        self.assertEqual(lca.query(0, 1), 0)
        self.assertEqual(lca.query(0, 2), 0)

    def test_lca_on_more_complex_tree(self):
        tree = [[1, 2], [3, 4], [], [5, 6], [], [], [7, 8], [], []]
        lca = LCA(tree, 0)
        self.assertEqual(lca.query(1, 2), 0)
        self.assertEqual(lca.query(3, 4), 1)
        self.assertEqual(lca.query(5, 6), 3)
        self.assertEqual(lca.query(7, 8), 6)
        self.assertEqual(lca.query(3, 7), 3)
        self.assertEqual(lca.query(0, 7), 0)
        self.assertEqual(lca.query(0, 8), 0)
        self.assertEqual(lca.query(2, 5), 0)

    def test_lca_on_tree_with_multiple_lcas(self):
        tree = [[1, 2], [3, 4], [5, 6], [7], [], [8, 9], [], [10, 11], [], [], [], []]
        lca = LCA(tree, 0)
        self.assertEqual(lca.query(1, 2), 0)
        self.assertEqual(lca.query(3, 4), 1)
        self.assertEqual(lca.query(5, 6), 2)
        self.assertEqual(lca.query(7, 8), 0)
        self.assertEqual(lca.query(9, 10), 0)
        self.assertEqual(lca.query(11, 8), 0)
        self.assertEqual(lca.query(5, 9), 5)
        self.assertEqual(lca.query(6, 10), 0)
        self.assertEqual(lca.query(7, 11), 7)


if __name__ == '__main__':
    unittest.main()
