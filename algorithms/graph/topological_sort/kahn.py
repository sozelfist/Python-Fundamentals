import unittest
from typing import List, Dict


def kahn_topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    indegrees = [0] * len(graph)
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1
    queue = [node for node, degree in enumerate(indegrees) if degree == 0]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == len(graph) else []


class TestKahnTopologicalSort(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        self.assertEqual(kahn_topological_sort(graph), [])

    def test_single_node_graph(self):
        graph = {0: []}
        self.assertEqual(kahn_topological_sort(graph), [0])

    def test_dag(self):
        graph = {0: [1, 2], 1: [2], 2: []}
        self.assertEqual(kahn_topological_sort(graph), [0, 1, 2])

    def test_cyclic_graph(self):
        graph = {0: [1], 1: [2], 2: [0]}
        self.assertEqual(kahn_topological_sort(graph), [])

    def test_complex_dag(self):
        graph = {0: [1, 2, 3], 1: [2, 3], 2: [4], 3: [4], 4: []}
        self.assertEqual(kahn_topological_sort(graph), [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
