import unittest


# Creating a directed graph using an adjacency matrix
class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.matrix: list[list[int]] = [
            [0 for _ in range(num_vertices)] for _ in range(num_vertices)
        ]

    def add_edge(self, v1: int, v2: int):
        self.matrix[v1][v2] = 1

    def get_graph(self) -> list[list[int]]:
        return self.matrix


class TestGraph(unittest.TestCase):
    def test_add_edge(self):
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        self.assertEqual(g.get_graph(), [[0, 1, 1, 0], [
                         0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
