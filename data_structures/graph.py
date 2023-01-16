
from typing import Dict, List
import unittest


class Graph:
    def __init__(self, directed: bool = False):
        self.graph = dict()
        self.directed = directed

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if not self.directed:
            if vertex2 in self.graph:
                self.graph[vertex2].append(vertex1)
            else:
                self.graph[vertex2] = [vertex1]

    def get_vertices(self) -> List[int]:
        return list(self.graph.keys())

    def get_edges(self) -> Dict[int, List[int]]:
        return self.graph

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return str(self.graph)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)

    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertIn(4, self.graph.get_vertices())

    def test_add_edge(self):
        self.graph.add_edge(3, 1)
        self.assertIn(1, self.graph.get_edges()[3])

    def test_get_vertices(self):
        self.assertEqual(self.graph.get_vertices(), [1, 2, 3])

    def test_get_edges(self):
        self.assertEqual(self.graph.get_edges(), {1: [2], 2: [1, 3], 3: [2]})

    def test_str(self):
        self.assertEqual(str(self.graph), "{1: [2], 2: [1, 3], 3: [2]}")


if __name__ == '__main__':
    unittest.main()
