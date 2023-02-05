from typing import List
import unittest


class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v1: int, v2: int):
        self.adj_list[v1].append(v2)

    def get_adj_list(self) -> List[List[int]]:
        return self.adj_list


class TestGraph(unittest.TestCase):
    def test_add_edge(self):
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        self.assertEqual(g.get_adj_list(), [[1, 2], [2], [0, 3], []])


if __name__ == '__main__':
    unittest.main()
