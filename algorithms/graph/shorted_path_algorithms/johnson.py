from typing import List
import unittest


def johnson(graph: List[List[int]], nodes: int) -> List[List[float]]:
    dist = [[float("inf") for j in range(nodes)] for i in range(nodes)]
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float("inf"):
                dist[i][j] = graph[i][j]

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


class TestFloydWarshall(unittest.TestCase):
    def test_johnson_1(self):
        nodes = 4
        inf = float("inf")
        graph = [[0, 3, inf, 5],
                 [2, 0, inf, 4],
                 [inf, 1, 0, inf],
                 [inf, inf, 2, 0]]
        result = johnson(graph, nodes)
        expected = [[0, 3, 7, 5],
                    [2, 0, 6, 4],
                    [3, 1, 0, 5],
                    [5, 3, 2, 0]]
        self.assertEqual(result, expected)

    def test_johnson_2(self):
        nodes = 3
        inf = float("inf")
        graph = [[0, 1, inf],
                 [1, 0, 2],
                 [inf, 2, 0]]
        result = johnson(graph, nodes)
        expected = [[0, 1, 3],
                    [1, 0, 2],
                    [3, 2, 0]]
        self.assertEqual(result, expected)

    def test_johnson_3(self):
        nodes = 2
        inf = float("inf")
        graph = [[0, 5],
                 [3, 0]]
        result = johnson(graph, nodes)
        expected = [[0, 5],
                    [3, 0]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
