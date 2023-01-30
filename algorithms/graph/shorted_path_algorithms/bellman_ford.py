import unittest
from typing import List, Tuple


def bellman_ford(adj_list: List[List[Tuple[int, int]]], start: int) -> List[int]:
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0

    for i in range(n - 1):
        for u in range(n):
            for v, w in adj_list[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(n):
        for v, w in adj_list[u]:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")
    return dist


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford_valid_input(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], []]
        start = 0
        expected_output = [0, 2, 3, 7]
        self.assertEqual(bellman_ford(adj_list, start), expected_output)

    def test_bellman_ford_negative_weights(self):
        adj_list = [[(1, -2), (2, -1)], [(2, -3)], [(0, -4), (1, -4)], [(0, 1)]]
        start = 0
        self.assertRaises(ValueError, bellman_ford, adj_list, start)

    def test_bellman_ford_disconnected_graph(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], [], [(4, 1)]]
        start = 0
        expected_output = [0, 2, 3, 7, float('inf')]
        self.assertEqual(bellman_ford(adj_list, start), expected_output)

    def test_bellman_ford_single_vertex(self):
        adj_list = [[]]
        start = 0
        expected_output = [0]
        self.assertEqual(bellman_ford(adj_list, start), expected_output)


if __name__ == '__main__':
    unittest.main()
