import unittest
from typing import List, Tuple


def boruvka(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    mst = []
    rep = [i for i in range(n)]
    weight = [float('inf')] * n
    while len(mst) < n - 1:
        for i in range(n):
            rep[i] = i
        for u, v, w in edges:
            if rep[u] != rep[v]:
                ru, rv = rep[u], rep[v]
                if w < weight[ru]:
                    weight[ru] = w
                    mst.append((u, v))
                if w < weight[rv]:
                    weight[rv] = w
                    mst.append((u, v))
                for i in range(n):
                    if rep[i] == ru:
                        rep[i] = rv
    return mst


class TestBoruvka(unittest.TestCase):
    def test_valid_input(self):
        # Test case 1: a valid input
        n = 4
        edges = [(0, 1, 1), (0, 2, 3), (1, 2, 1), (2, 3, 5)]
        result = boruvka(n, edges)
        expected_result = [(0, 1), (1, 2), (0, 2)]
        self.assertEqual(result, expected_result)

    def test_disconnected_graph(self):
        # Test case 2: a disconnected graph
        n = 5
        edges = [(0, 1, 3), (2, 3, 2), (3, 4, 4)]
        result = boruvka(n, edges)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_large_input(self):
        # Test case 3: a large input
        n = 10
        edges = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (2, 3, 5), (3, 4, 8),
                 (4, 5, 2), (5, 6, 9), (6, 7, 6), (7, 8, 3), (8, 9, 1)]
        result = boruvka(n, edges)
        expected_result = [(0, 2), (2, 1), (4, 5), (8, 9), (7, 8), (6, 7)]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
