import unittest
from typing import List


def floyd_warshall(adj_matrix: List[List[int]], start: int, goal: int) -> List[int]:
    n = len(adj_matrix)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = adj_matrix[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    if dist[start][goal] == float('inf'):
        return []
    path = [goal]
    current = goal
    while current != start:
        for i in range(n):
            if dist[start][i] + dist[i][current] == dist[start][current]:
                current = i
                path.append(current)
                break
    return path[::-1]


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_valid_input(self):
        adj_matrix = [
            [0, 3, 8, float('inf'), -4],
            [float('inf'), 0, float('inf'), 1, 7],
            [float('inf'), 4, 0, float('inf'), float('inf')],
            [2, float('inf'), -5, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), 6, 0]
        ]
        start = 0
        goal = 4
        expected_output = [0, 4]
        self.assertEqual(floyd_warshall(adj_matrix, start, goal), expected_output)

    def test_floyd_warshall_no_path(self):
        adj_matrix = [
            [0, 3, 8, float('inf'), -4],
            [float('inf'), 0, float('inf'), 1, 7],
            [float('inf'), 4, 0, float('inf'), float('inf')],
            [2, float('inf'), -5, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), 6, 0]
        ]
        start = 0
        goal = 2
        expected_output = []
        self.assertEqual(floyd_warshall(adj_matrix, start, goal), expected_output)

    def test_floyd_warshall_disconnected_graph(self):
        adj_matrix = [
            [0, 3, 8, float('inf'), -4],
            [float('inf'), 0, float('inf'), 1, 7],
            [float('inf'), 4, 0, float('inf'), float('inf')],
            [2, float('inf'), -5, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), 6, 0]
        ]
        start = 0
        goal = 5
        expected_output = []
        self.assertEqual(floyd_warshall(adj_matrix, start, goal), expected_output)

    def test_floyd_warshall_single_vertex(self):
        adj_matrix = [[0]]
        start = 0
        goal = 0
        expected_output = [0]
        self.assertEqual(floyd_warshall(adj_matrix, start, goal), expected_output)


if __name__ == '__main__':
    unittest.main()
