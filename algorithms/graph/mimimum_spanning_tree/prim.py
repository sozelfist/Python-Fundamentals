import unittest
from typing import List, Tuple
import heapq


def prim(n: int, edges: List[Tuple[int, int, int]], start: int) -> List[Tuple[int, int]]:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    mst = []
    visited = [False] * n
    heap = [(0, start, -1)]
    heapq.heapify(heap)
    while heap:
        w, u, p = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if p != -1:
            mst.append((p, u))
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v, u))
    return mst


class TestPrim(unittest.TestCase):
    def test_valid_input(self):
        # Test case 1: a valid input
        n = 4
        edges = [(0, 1, 1), (0, 2, 3), (1, 2, 1), (2, 3, 5)]
        start = 0
        result = prim(n, edges, start)
        expected_result = [(0, 1), (1, 2), (0, 2)]
        self.assertEqual(result, expected_result)

    def test_disconnected_graph(self):
        # Test case 2: a disconnected graph
        n = 5
        edges = [(0, 1, 3), (2, 3, 2), (3, 4, 4)]
        start = 0
        result = prim(n, edges, start)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_large_input(self):
        # Test case 3: a large input
        n = 10
        edges = [(0, 1, 5), (0, 2, 3), (1, 2, 1), (2, 3, 5), (3, 4, 8),
                 (4, 5, 2), (5, 6, 9), (6, 7, 6), (7, 8, 3), (8, 9, 1)]
        start = 0
        result = prim(n, edges, start)
        expected_result = [(0, 2), (2, 1), (4, 5), (8, 9), (7, 8), (6, 7)]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
