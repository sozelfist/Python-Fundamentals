import unittest
from typing import List, Tuple


def dfs(graph: List[List[int]], start: int, end: int) -> Tuple[bool, List[int]]:
    """
    Given a graph represented as an adjacency list,
    this function performs a depth-first search
    starting from the 'start' vertex and returns
    whether the 'end' vertex is reachable or not,
    and the path from start to end vertex if exists
    """
    stack = []
    visited = [False] * len(graph)
    path = [-1] * len(graph)
    path[start] = start
    stack.append(start)
    visited[start] = True

    while stack:
        vertex = stack.pop()

        if vertex == end:
            res = []
            while path[vertex] != vertex:
                res.append(vertex)
                vertex = path[vertex]
            res.append(vertex)
            return True, res

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True
                path[neighbor] = vertex

    return False, []


class TestDFS(unittest.TestCase):
    def test_dfs_valid_input(self):
        graph = [[1, 2, 3], [2], [3], []]
        start = 0
        end = 3
        expected_output = (True, [0, 1, 2, 3])
        self.assertEqual(dfs(graph, start, end), expected_output)

    def test_dfs_invalid_input(self):
        graph = [[1, 2, 3], [2], [3], []]
        start = -1
        end = 3
        expected_output = (False, [])
        self.assertEqual(dfs(graph, start, end), expected_output)

    def test_dfs_unreachable_end(self):
        graph = [[1, 2], [2], []]
        start = 0
        end = 3
        expected_output = (False, [])
        self.assertEqual(dfs(graph, start, end), expected_output)

    def test_dfs_same_start_and_end(self):
        graph = [[1, 2], [2], []]
        start = 0
        end = 0
        expected_output = (True, [0])
        self.assertEqual(dfs(graph, start, end), expected_output)

    def test_dfs_large_graph(self):
        graph = [[1, 2, 3, 4], [2, 4], [3, 4], [4], []]
        start = 0
        end = 4
        expected_output = (True, [0, 1, 2, 3, 4])
        self.assertEqual(dfs(graph, start, end), expected_output)


if __name__ == '__main__':
    unittest.main()
