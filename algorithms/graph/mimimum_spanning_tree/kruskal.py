import unittest
from typing import List, Tuple


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    result = []

    def find_parent(x: int) -> int:
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def merge_sets(x: int, y: int) -> None:
        parent[find_parent(x)] = find_parent(y)

    for u, v, w in edges:
        if find_parent(u) != find_parent(v):
            result.append((u, v))
            merge_sets(u, v)
    return result


class TestKruskal(unittest.TestCase):
    def test_kruskal(self):
        n = 4
        edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
        result = kruskal(n, edges)
        expected_result = [(2, 3), (0, 3), (0, 1)]
        self.assertEqual(result, expected_result)

        n = 5
        edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (3, 4, 5), (4, 2, 1)]
        result = kruskal(n, edges)
        expected_result = [(4, 2), (0, 1), (1, 2), (3, 4)]
        self.assertEqual(result, expected_result)

        n = 6
        edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (3, 4, 5), (4, 2, 1), (5, 2, 4)]
        result = kruskal(n, edges)
        expected_result = [(4, 2), (0, 1), (1, 2), (5, 2), (3, 4)]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
