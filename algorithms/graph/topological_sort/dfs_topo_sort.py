import unittest
from typing import List, Dict


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    def dfs(node: int, visited: List[bool], stack: List[int]):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

    n = len(graph)
    visited = [False] * n
    stack = []
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, stack)
    return list(reversed(stack))


class TopologicalSortTest(unittest.TestCase):
    def test_case_1(self):
        graph = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: []
        }
        result = topological_sort(graph)
        self.assertListEqual(result, [0, 2, 1, 3])

    def test_case_2(self):
        graph = {
            0: [2, 0],
            1: [0, 1],
            2: [3],
            3: [1],
        }
        result = topological_sort(graph)
        self.assertListEqual(result, [0, 2, 3, 1])

    def test_case_3(self):
        graph = {
            0: [],
            1: [],
            2: []
        }
        result = topological_sort(graph)
        self.assertListEqual(result, [2, 1, 0])

    def test_case_4(self):
        graph = {
            0: [1, 2],
            1: [2],
            2: [3],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        self.assertListEqual(result, [0, 1, 2, 3, 4])

    def test_case_5(self):
        graph = {
            3: [2, 0],
            2: [1],
            1: [0],
            0: []
        }
        result = topological_sort(graph)
        self.assertListEqual(result, [3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
