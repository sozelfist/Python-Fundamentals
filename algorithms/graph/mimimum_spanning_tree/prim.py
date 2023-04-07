import heapq
import unittest


def prim(n: int, edges: list[tuple[int, int, int]], start: int) -> list[tuple[int, int]]:
    if n == 0:
        return []

    graph = create_graph(n, edges)
    mst = []
    visited = [False] * n
    heap = [(0, start, -1)]
    heapq.heapify(heap)
    while heap:
        weight, node, parent = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        if parent != -1:
            mst.append((parent, node))
        add_neighbors_to_heap(graph, node, visited, heap)
    return mst


def create_graph(n: int, edges: list[tuple[int, int, int]]) -> list[list[tuple[int, int]]]:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def add_neighbors_to_heap(
    graph: list[list[tuple[int, int]]],
    node: int, visited: list[bool],
    heap: list[tuple[int, int, int]]
):
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            heapq.heappush(heap, (weight, neighbor, node))


class TestPrim(unittest.TestCase):
    def test_empty_graph(self):
        n = 0
        edges = []
        start = 0
        result = prim(n, edges, start)
        self.assertEqual(result, [])

    def test_single_node(self):
        n = 1
        edges = []
        start = 0
        result = prim(n, edges, start)
        self.assertEqual(result, [])

    def test_small_graph(self):
        n = 5
        edges = [(0, 1, 1), (0, 2, 2), (1, 2, 3), (1, 3, 4), (2, 3, 5), (3, 4, 6)]
        start = 0
        result = prim(n, edges, start)
        expected = [(0, 1), (0, 2), (1, 3), (3, 4)]
        self.assertCountEqual(result, expected)

    def test_large_graph(self):
        n = 10
        edges = [(0, 1, 1), (0, 2, 2), (1, 2, 3), (1, 3, 4), (2, 3, 5), (3, 4, 6),
                 (4, 5, 7), (5, 6, 8), (6, 7, 9), (7, 8, 10), (8, 9, 11)]
        start = 0
        result = prim(n, edges, start)
        expected = [(0, 1), (1, 3), (0, 2), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
