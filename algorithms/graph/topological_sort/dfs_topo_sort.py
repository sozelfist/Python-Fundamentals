import unittest
from typing import List, Dict


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    def dfs(v: int, visited: List[bool], stack: List[int]):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    n = len(graph)
    visited = [False for _ in range(n)]
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)
    return stack[::-1]


class TestTopologicalSort(unittest.TestCase):
    def test_simple(self):
        graph = {
            0: [],
            1: [],
            2: [3],
            3: [1],
            4: [0, 1],
            5: [2, 0]
        }
        self.assertEqual(topological_sort(graph), [5, 4, 2, 3, 1, 0])

    def test_complex(self):
        graph = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: [4],
            4: [5],
            5: []
        }
        self.assertEqual(topological_sort(graph), [0, 2, 1, 3, 4, 5])

    def test_cycle(self):
        graph = {
            0: [1],
            1: [2],
            2: [0]
        }
        with self.assertRaises(Exception):
            topological_sort(graph)


if __name__ == '__main__':
    unittest.main()
