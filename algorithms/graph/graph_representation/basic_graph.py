import unittest
from typing import Any


class Graph:
    """
    A class representing a graph data structure.

    Attributes:
        vertices (dict): A dictionary to store the vertices of the graph
                         as keys and their associated values.
        edges (dict): A dictionary to store the edges of the graph as keys
                        and their associated values.
    """

    def __init__(self) -> None:
        """
        Initialize an empty graph.
        """
        self.vertices: dict = {}
        self.edges: dict = {}

    def adjacent(self, x: str, y: str) -> bool:
        """
        Tests whether there is an edge from vertex x to vertex y.

        Args:
            x (str): The starting vertex.
            y (str): The ending vertex.

        Returns:
            bool: True if there is an edge from x to y, False otherwise.
        """
        return y in self.vertices[x]['neighbors']

    def neighbors(self, x: str) -> list:
        """
        Lists all vertices y such that there is an edge from vertex x
        to vertex y.

        Args:
            x (str): The vertex for which neighbors need to be listed.

        Returns:
            list: A list of vertices that are neighbors of x.
        """
        return list(self.vertices[x]['neighbors'])

    def add_vertex(self, x: str, v: Any = None) -> None:
        """
        Adds a vertex x to the graph with an optional value v.

        Args:
            x (str): The vertex to be added.
            v (Any, optional): The value associated with the vertex.
            Defaults to None.
        """
        if x not in self.vertices:
            self.vertices[x] = {'value': v, 'neighbors': set()}

    def remove_vertex(self, x: str) -> None:
        """
        Removes a vertex x from the graph, along with its associated edges.

        Args:
            x (str): The vertex to be removed.
        """
        if x in self.vertices:
            del self.vertices[x]
            # Remove any edges that are connected to x
            for v in self.vertices:
                self.vertices[v]['neighbors'].discard(x)

    def add_edge(self, x: str, y: str, z: Any = None) -> None:
        """
        Adds an edge from vertex x to vertex y with an optional value z.

        Args:
            x (str): The starting vertex.
            y (str): The ending vertex.
            z (Any, optional): The value associated with the edge.
            Defaults to None.
        """
        if x in self.vertices and y in self.vertices:
            self.vertices[x]['neighbors'].add(y)
            self.edges[(x, y)] = z

    def remove_edge(self, x: str, y: str) -> None:
        """
        Removes an edge from vertex x to vertex y.

        Args:
            x (str): The starting vertex.
            y (str): The ending vertex.
        """
        if x in self.vertices and y in self.vertices:
            self.vertices[x]['neighbors'].discard(y)
            del self.edges[(x, y)]

    def get_vertex_value(self, x: str) -> Any | None:
        """
        Returns the value associated with vertex x.

        Args:
            x (str): The vertex for which the value is needed.

        Returns:
            Any: The value associated with the vertex, or None if not found.
        """
        return self.vertices.get(x, {}).get('value')

    def set_vertex_value(self, x: str, v: Any) -> None:
        """
        Sets the value associated with vertex x to v.

        Args:
            x (str): The vertex for which the value needs to be set.
            v (Any): The value to be associated with the vertex.
        """
        if x in self.vertices:
            self.vertices[x]['value'] = v

    def get_edge_value(self, x: str, y: str) -> Any | None:
        """
        Returns: the value associated with the edge from vertex x to vertex y.
        Args:
        x (str): The starting vertex.
        y (str): The ending vertex.
    """
        return self.edges.get((x, y))

    def set_edge_value(self, x: str, y: str, v: Any) -> None:
        """
        Sets the value associated with the edge from vertex x to vertex y to v.

        Args:
            x (str): The starting vertex.
            y (str): The ending vertex.
            v (Any): The value to be associated with the edge.
        """
        if (x, y) in self.edges:
            self.edges[(x, y)] = v


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 10)

    def test_adjacent(self):
        self.assertTrue(self.graph.adjacent('A', 'B'))
        self.assertFalse(self.graph.adjacent('B', 'A'))
        self.assertFalse(self.graph.adjacent('A', 'C'))

    def test_neighbors(self):
        neighbors = self.graph.neighbors('A')
        self.assertEqual(neighbors, ['B'])

    def test_add_vertex(self):
        self.graph.add_vertex('C')
        self.assertIn('C', self.graph.vertices)

    def test_remove_vertex(self):
        self.graph.remove_vertex('B')
        self.assertNotIn('B', self.graph.vertices)

    def test_add_edge(self):
        self.graph.add_edge('B', 'A', 20)
        self.assertTrue(self.graph.adjacent('B', 'A'))
        self.assertEqual(self.graph.get_edge_value('B', 'A'), 20)

    def test_remove_edge(self):
        self.graph.remove_edge('A', 'B')
        self.assertFalse(self.graph.adjacent('A', 'B'))

    def test_get_vertex_value(self):
        value = self.graph.get_vertex_value('A')
        self.assertIsNone(value)

    def test_set_vertex_value(self):
        self.graph.set_vertex_value('A', 100)
        value = self.graph.get_vertex_value('A')
        self.assertEqual(value, 100)

    def test_get_edge_value(self):
        value = self.graph.get_edge_value('A', 'B')
        self.assertEqual(value, 10)

    def test_set_edge_value(self):
        self.graph.set_edge_value('A', 'B', 50)
        value = self.graph.get_edge_value('A', 'B')
        self.assertEqual(value, 50)


if __name__ == '__main__':
    unittest.main()
