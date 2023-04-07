import unittest


def bellman_ford(adj_list: list[list[tuple[int, int]]], start: int) -> list[int | float]:
    n = len(adj_list)
    distances = [float('inf')] * n
    distances[start] = 0

    for _i in range(n - 1):
        for u, neighbors in enumerate(adj_list):
            for v, w in neighbors:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    for u, neighbors in enumerate(adj_list):
        for v, w in neighbors:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford_negative_cycle(self):
        adj_list = [[(1, -1), (2, -1)], [(2, -1)], [(0, 1)]]
        with self.assertRaises(ValueError) as context:
            bellman_ford(adj_list, 0)
        self.assertEqual(str(context.exception), "Graph contains a negative-weight cycle")

    def test_bellman_ford_shortest_paths(self):
        adj_list = [[(1, 2), (2, -1)], [(2, 2)], [(0, 3)]]
        result = bellman_ford(adj_list, 0)
        expected = [0, 2, -1]
        self.assertEqual(result, expected)

    def test_bellman_ford_single_node(self):
        adj_list = [[]]
        result = bellman_ford(adj_list, 0)
        expected = [0]
        self.assertEqual(result, expected)

    def test_bellman_ford_disconnected_graph(self):
        adj_list = [[(1, 2)], [(2, 1)], [], [], []]
        result = bellman_ford(adj_list, 0)
        expected = [0, 2, 3, float('inf'), float('inf')]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
