from typing import Dict
import unittest


class Vertex:
    def __init__(self, value: str):
        self.value = value
        self.edges: Dict[str, int] = {}

    def add_edge(self, vertex: str, weight: int):
        self.edges[vertex] = weight


class Graph:
    def __init__(self):
        self.graph_dict: Dict[str, Vertex] = {}

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int):
        self.graph_dict[from_vertex].add_edge(to_vertex, weight)


class TestGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        a = Vertex('A')
        b = Vertex('B')
        g.add_vertex(a)
        g.add_vertex(b)
        self.assertEqual(len(g.graph_dict), 2)
        self.assertIn('A', g.graph_dict)
        self.assertIn('B', g.graph_dict)

    def test_add_edge(self):
        g = Graph()
        a = Vertex('A')
        b = Vertex('B')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_edge('A', 'B', 1)
        self.assertIn('B', g.graph_dict['A'].edges)
        self.assertEqual(g.graph_dict['A'].edges['B'], 1)


if __name__ == '__main__':
    unittest.main()
