import unittest


def dfs(graph: list[list[int]], start: int) -> list[int]:
    if not graph:
        raise ValueError("Invalid graph")
    if start < 0 or start >= len(graph):
        raise ValueError("Invalid start vertex")

    visited = [False for _ in range(len(graph))]
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            stack.extend(neighbor for neighbor in reversed(graph[vertex]) if not visited[neighbor])

    return result


class TestDFS(unittest.TestCase):
    def test_valid_input(self):
        graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
        start = 0
        result = dfs(graph, start)
        self.assertEqual(result, [0, 1, 3, 2])

    def test_empty_graph(self):
        graph = []
        start = 0
        with self.assertRaises(ValueError, msg="Invalid graph"):
            dfs(graph, start)

    def test_invalid_start_vertex(self):
        graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
        start = 4
        with self.assertRaises(ValueError, msg="Invalid start vertex"):
            dfs(graph, start)

    def test_disconnected_graph(self):
        graph = [[1, 2], [0], []]
        start = 0
        result = dfs(graph, start)
        self.assertEqual(result, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
