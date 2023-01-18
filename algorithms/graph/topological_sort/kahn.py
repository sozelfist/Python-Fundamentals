import unittest
from typing import List, Dict


def kahn_topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    indegrees = [0 for _ in range(len(graph))]
    for v in graph:
        for neighbor in graph[v]:
            indegrees[neighbor] += 1
    queue = []
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)
    result = []
    while queue:
        u = queue.pop(0)
        result.append(u)
        for neighbor in graph[u]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(graph):
        return []
    return result


class TestKahnTopologicalSort(unittest.TestCase):
    def test_simple(self):
        graph = {
            0: [],
            1: [],
            2: [3],
            3: [1],
            4: [0, 1],
            5: [2, 0]
        }
        self.assertEqual(kahn_topological_sort(graph), [4, 5, 2, 0, 3, 1])

    def test_complex(self):
        graph = {
            0: [1, 2],
            1: [3],
            2: [3],
            3: [4],
            4: [5],
            5: []
        }
        self.assertEqual(kahn_topological_sort(graph), [0, 1, 2, 3, 4, 5])

    def test_cycle(self):
        graph = {
            0: [1],
            1: [2],
            2: [0]
        }
        self.assertEqual(kahn_topological_sort(graph), [])

    def test_disconnected_graph(self):
        graph = {
            0: [1, 2],
            1: [],
            2: [3],
            3: [4],
            4: [],
            5: [],
            6: [],
        }
        self.assertEqual(kahn_topological_sort(graph), [0, 5, 6, 1, 2, 3, 4])

    def test_empty_graph(self):
        graph = {}
        self.assertEqual(kahn_topological_sort(graph), [])


if __name__ == '__main__':
    unittest.main()
