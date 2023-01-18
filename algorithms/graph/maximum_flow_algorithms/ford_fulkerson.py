from collections import deque
import unittest
from typing import List, Tuple


def ford_fulkerson(n: int, edges: List[Tuple[int, int, int]], s: int, t: int) -> int:
    # Initialize the residual graph
    residual = [[0 for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        residual[u][v] = w

    # Initialize the flow and the parent arrays
    flow = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    # Find an augmenting path from the source to the sink
    while bfs(residual, s, t, parent):
        # Find the minimum capacity along the path
        path_flow = float("Inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Update the flow and the residual graph
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        # Add the path flow to the overall flow
        flow[s] += path_flow

    # Return the maximum flow
    return flow[s]


def bfs(residual: List[List[int]], s: int, t: int, parent: List[int]) -> bool:
    # Initialize the visited array
    visited = [False for _ in range(len(residual))]

    # Create a deque and add the source node
    queue = deque([s])
    visited[s] = True

    # Perform the BFS
    while queue:
        u = queue.popleft()
        for v in range(len(residual)):
            if not visited[v] and residual[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

    # Return True if a path was found, otherwise False
    return visited[t]


class TestFordFulkerson(unittest.TestCase):
    def test_simple(self):
        n = 6
        edges = [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4),
                 (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]
        s = 0
        t = 5
        self.assertEqual(ford_fulkerson(n, edges, s, t), 23)

    def test_complex(self):
        n = 5
        edges = [(0, 1, 9), (0, 3, 5), (1, 2, 2), (1, 3, 4), (2, 4, 4), (3, 2, 1), (3, 4, 6)]
        s = 0
        t = 4
        self.assertEqual(ford_fulkerson(n, edges, s, t), 9)

    def test_no_path(self):
        n = 5
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 0, 1)]
        s = 0
        t = 4
        self.assertEqual(ford_fulkerson(n, edges, s, t), 1)


if __name__ == '__main__':
    unittest.main()
