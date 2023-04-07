import unittest


class WeightedGraph:
    def __init__(self, directed: bool = False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        self.graph[vertex1][vertex2] = weight
        if not self.directed:
            self.graph[vertex2][vertex1] = weight

    def get_vertices(self) -> list[int]:
        return list(self.graph.keys())

    def get_edges(self) -> dict[int, dict[int, int]]:
        return self.graph


class TestWeightedGraph(unittest.TestCase):
    def setUp(self):
        self.graph = WeightedGraph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(2, 3, 20)

    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertIn(4, self.graph.get_vertices())

    def test_add_edge(self):
        self.graph.add_edge(3, 1, 30)
        self.assertIn(1, self.graph.get_edges()[3])
        self.assertEqual(self.graph.get_edges()[3][1], 30)

    def test_get_vertices(self):
        self.assertEqual(self.graph.get_vertices(), [1, 2, 3])

    def test_get_edges(self):
        self.assertEqual(self.graph.get_edges(), {1: {2: 10}, 2: {1: 10, 3: 20}, 3: {2: 20}})


if __name__ == '__main__':
    unittest.main()
