import unittest
from typing import List
from collections import deque


def bfs(graph: List[List[int]], start: int) -> List[int]:
    if not graph:
        raise ValueError("Not a valid graph")
    if start >= len(graph) or start < 0:
        raise ValueError("Not a valid start vertex")
    visited = [False] * len(graph)
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
    def test_bfs_basic(self):
        self.assertEqual(bfs([[1, 2], [3], [4], [], []], 0), [0, 1, 2, 3, 4])
        self.assertEqual(bfs([[1, 2], [0, 3], [1, 4], [2], [3]], 2), [2, 1, 4, 0, 3])

    def test_bfs_exception(self):
        self.assertRaises(ValueError, bfs, [], 0)
        self.assertRaises(ValueError, bfs, [[1, 2], [3], [4], [], []], 5)
        self.assertRaises(ValueError, bfs, [[1, 2], [3], [4], [], []], -1)


if __name__ == '__main__':
    unittest.main()
