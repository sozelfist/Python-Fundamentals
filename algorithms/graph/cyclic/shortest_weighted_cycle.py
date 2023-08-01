# Assuming the refactored code is in a module called "graph"
import unittest
from sys import maxsize

INF = 0x3f3f3f3f


class Edge:
    def __init__(self, u: int, v: int, weight: int) -> None:
        self.u = u
        self.v = v
        self.weight = weight


class Graph:
    def __init__(self, V: int) -> None:
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.edge = []

    def add_edge(self, u: int, v: int, w: int) -> None:
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        e = Edge(u, v, w)
        self.edge.append(e)

    def remove_edge(self, u: int, v: int, w: int) -> None:
        self.adj[u].remove((v, w))
        self.adj[v].remove((u, w))

    def get_shorted_path(self, u: int, v: int) -> int:
        setds = set()
        dist = [INF] * self.V
        setds.add((0, u))
        dist[u] = 0

        while setds:
            tmp = setds.pop()
            uu = tmp[1]

            for i in self.adj[uu]:
                vv = i[0]
                weight = i[1]

                if dist[vv] > dist[uu] + weight:
                    if dist[vv] != INF:
                        if (dist[vv], vv) in setds:
                            setds.remove((dist[vv], vv))
                    dist[vv] = dist[uu] + weight
                    setds.add((dist[vv], vv))

        return dist[v]

    def find_minimum_cycle(self) -> int:
        min_cycle = maxsize
        E = len(self.edge)

        for i in range(E):
            e = self.edge[i]
            self.remove_edge(e.u, e.v, e.weight)
            distance = self.get_shorted_path(e.u, e.v)
            min_cycle = min(min_cycle, distance + e.weight)
            self.add_edge(e.u, e.v, e.weight)

        return min_cycle


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.V = 9
        self.g = Graph(self.V)
        self.g.add_edge(0, 1, 4)
        self.g.add_edge(0, 7, 8)
        self.g.add_edge(1, 2, 8)
        self.g.add_edge(1, 7, 11)
        self.g.add_edge(2, 3, 7)
        self.g.add_edge(2, 8, 2)
        self.g.add_edge(2, 5, 4)
        self.g.add_edge(3, 4, 9)
        self.g.add_edge(3, 5, 14)
        self.g.add_edge(4, 5, 10)
        self.g.add_edge(5, 6, 2)
        self.g.add_edge(6, 7, 1)
        self.g.add_edge(6, 8, 6)
        self.g.add_edge(7, 8, 7)

    def test_shortest_path(self):
        self.assertEqual(self.g.get_shorted_path(0, 5), 11)
        self.assertEqual(self.g.get_shorted_path(2, 6), 6)
        self.assertEqual(self.g.get_shorted_path(3, 7), 14)

    def test_find_minimum_cycle(self):
        self.assertEqual(self.g.find_minimum_cycle(), 14)

    def test_remove_edge(self):
        self.g.remove_edge(2, 5, 4)
        self.assertNotIn((5, 4), self.g.adj[2])
        self.assertNotIn((2, 4), self.g.adj[5])

    def test_add_edge(self):
        self.g.add_edge(2, 5, 4)
        self.assertIn((5, 4), self.g.adj[2])
        self.assertIn((2, 4), self.g.adj[5])


if __name__ == '__main__':
    unittest.main()
