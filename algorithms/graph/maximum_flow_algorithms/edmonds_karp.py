import unittest
from typing import List, Tuple
from collections import deque


def edmonds_karp(n: int, edges: List[Tuple[int, int, int]], s: int, t: int) -> int:
    # Initialize the residual graph
    residual = [[0 for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        residual[u][v] += w

    # Initialize the parent array
    parent = [-1 for _ in range(n)]

    # Initialize the maximum flow
    max_flow = 0

    # Perform the Edmonds-Karp algorithm
    while True:
        # Use BFS to find an augmenting path
        queue = deque([s])
        parent[s] = -2
        while queue:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        break

        # If no augmenting path was found, break out of the loop
        if parent[t] == -1:
            break

        # Find the bottleneck capacity
        bottleneck = float('inf')
        v = t
        while v != s:
            u = parent[v]
            bottleneck = min(bottleneck, residual[u][v])
            v = u

        # Update the residual graph
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck
            v = u

        # Add the bottleneck capacity to the maximum flow
        max_flow += bottleneck

    # Return the maximum flow
    return max_flow


class TestEdmondsKarp(unittest.TestCase):
    def test_simple(self):
        n = 6
        edges = [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4),
                 (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]
        s = 0
        t = 5
        self.assertEqual(edmonds_karp(n, edges, s, t), 23)

    def test_complex(self):
        n = 5
        edges = [(0, 1, 9), (0, 3, 5), (1, 2, 2), (1, 3, 4), (2, 4, 4), (3, 2, 1), (3, 4, 6)]
        s = 0
        t = 4
        self.assertEqual(edmonds_karp(n, edges, s, t), 8)

    def test_no_path(self):
        n = 5
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 0, 1)]
        s = 0
        t = 4
        self.assertEqual(edmonds_karp(n, edges, s, t), 0)


if __name__ == '__main__':
    unittest.main()
