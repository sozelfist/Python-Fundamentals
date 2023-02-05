import unittest
from collections import deque
from typing import List, Tuple


def bfs(graph: List[List[int]], start: int, end: int) -> Tuple[bool, List[int]]:
    queue = deque([start])
    visited = [False for _ in range(len(graph))]
    path = [-1 for _ in range(len(graph))]
    path[start] = start
    visited[start] = True

    while queue:
        vertex = queue.popleft()

        if vertex == end:
            return True, reconstruct_path(path, start, end)

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                path[neighbor] = vertex

    return False, []


def reconstruct_path(path: List[int], start: int, end: int) -> List[int]:
    result = []
    vertex = end
    while vertex != start:
        result.append(vertex)
        vertex = path[vertex]
    result.append(start)
    return result[::-1]


class TestBFS(unittest.TestCase):
    def test_BFS(self):
        graph = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4],
            []
        ]
        result = bfs(graph, 0, 4)
        self.assertTrue(result[0])
        self.assertEqual(result[1], [0, 2, 4])


if __name__ == '__main__':
    unittest.main()
