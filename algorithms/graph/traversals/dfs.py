import unittest


def bfs(graph: list[list[int]], start: int, end: int) -> list[int] | None:
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for next_vertex in graph[vertex]:
            if next_vertex == end:
                return path + [end]
            queue.append((next_vertex, path + [next_vertex]))
    return None


class TestBFS(unittest.TestCase):
    def test_case_1(self):
        graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
        start = 0
        end = 5
        expected = [0, 2, 5]
        result = bfs(graph, start, end)
        self.assertEqual(result, expected)

    def test_case_2(self):
        graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
        start = 0
        end = 4
        expected = [0, 1, 4]
        result = bfs(graph, start, end)
        self.assertEqual(result, expected)

    def test_case_3(self):
        graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
        start = 0
        end = 6
        expected = None
        result = bfs(graph, start, end)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
