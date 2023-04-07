import unittest


def floyd_warshall(graph: list[list[int]], nodes: int) -> list[list[int]]:
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_1(self):
        nodes = 4
        inf = float("inf")
        graph = [[0, 3, inf, 5],
                 [2, 0, inf, 4],
                 [inf, 1, 0, inf],
                 [inf, inf, 2, 0]]
        result = floyd_warshall(graph, nodes)
        expected = [[0, 3, 7, 5],
                    [2, 0, 6, 4],
                    [3, 1, 0, 5],
                    [5, 3, 2, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_2(self):
        nodes = 3
        inf = float("inf")
        graph = [[0, 1, inf],
                 [1, 0, 2],
                 [inf, 2, 0]]
        result = floyd_warshall(graph, nodes)
        expected = [[0, 1, 3],
                    [1, 0, 2],
                    [3, 2, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_3(self):
        nodes = 2
        float("inf")
        graph = [[0, 5],
                 [3, 0]]
        result = floyd_warshall(graph, nodes)
        expected = [[0, 5],
                    [3, 0]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
