import unittest
from typing import List


def dfs(graph: List[List[int]], start: int) -> List[int]:
    if not graph:
        raise ValueError("Not a valid graph")
    if start >= len(graph) or start < 0:
        raise ValueError("Not a valid start vertex")
    visited = [False] * len(graph)
    stack = [start]
    result = []
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    return result


class TestDFS(unittest.TestCase):
    def test_dfs_basic(self):
        self.assertEqual(dfs([[1, 2], [3], [4], [], []], 0), [0, 2, 4, 1, 3])
        self.assertEqual(dfs([[1, 2], [0, 3], [1, 4], [2], [3]], 2), [2, 4, 3, 1, 0])

    def test_dfs_exception(self):
        self.assertRaises(ValueError, dfs, [], 0)
        self.assertRaises(ValueError, dfs, [[1, 2], [3], [4], [], []], 5)
        self.assertRaises(ValueError, dfs, [[1, 2], [3], [4], [], []], -1)


if __name__ == '__main__':
    unittest.main()
