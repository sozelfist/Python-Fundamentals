import unittest
from collections import deque


def validate_input(graph: list[list[int]], start: int, n: int):
    if not graph:
        raise ValueError("Not a valid graph")
    if start >= n or start < 0:
        raise ValueError("Not a valid start vertex")


def bfs(graph: list[list[int]], start: int) -> list[int]:
    n = len(graph)
    validate_input(graph, start, n)
    visited = [False] * n
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            for neighbor in graph[vertex]:
                queue.append(neighbor)
    return result


class TestBFS(unittest.TestCase):
    def test_valid_input(self):
        graph = [[1, 2], [0, 3], [0], [1]]
        start = 0
        result = bfs(graph, start)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_start_vertex_out_of_bounds(self):
        graph = [[1, 2], [0, 3], [0], [1]]
        start = 4
        with self.assertRaises(ValueError):
            bfs(graph, start)

    def test_empty_graph(self):
        graph = []
        start = 0
        with self.assertRaises(ValueError):
            bfs(graph, start)


if __name__ == '__main__':
    unittest.main()
