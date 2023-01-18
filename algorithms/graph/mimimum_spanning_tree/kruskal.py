import unittest
from typing import List, Tuple


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> None:
        parent[find(x)] = find(y)
    result = []
    for u, v, w in edges:
        if find(u) != find(v):
            result.append((u, v))
            union(u, v)
    return result


class TestKruskal(unittest.TestCase):
    def test_valid_input(self):
        # Test case 1: a valid input
        n = 4
        edges = [(0, 1, 1), (0, 2, 3), (1, 2, 1), (2, 3, 5)]
        result = kruskal(n, edges)
        expected_result = [(0, 1), (1, 2), (0, 2)]
        self.assertEqual(result, expected_result)

    def test_disconnected_graph(self):
        # Test case 2: a disconnected graph
        n = 5
        edges = [(0, 1, 3), (2, 3, 2), (3, 4, 4)]
        result = kruskal(n, edges)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_large_input(self):
        # Test case 3: a large input
        n = 10
        edges = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (2, 3, 5), (3, 4, 8),
                 (4, 5, 2), (5, 6, 9), (6, 7, 6), (7, 8, 3), (8, 9, 1)]
        result = kruskal(n, edges)
        expected_result = [(0, 2), (2, 1), (4, 5), (8, 9), (7, 8), (6, 7)]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
