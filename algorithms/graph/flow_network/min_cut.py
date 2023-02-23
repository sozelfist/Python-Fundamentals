from typing import List, Tuple
import unittest


def bfs(graph: List[List[int]], source: int, sink: int, parent: List[int]) -> bool:
    """
    Breadth-first search algorithm to find a path from source to sink in the residual graph.
    Returns True if there is a path from source to sink, and updates the parent list with the path.
    """
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[sink]


def min_cut(graph: List[List[int]], source: int, sink: int) -> List[Tuple[int, int]]:
    """
    Implementation of the minimum cut algorithm using the Ford-Fulkerson algorithm.
    Returns a list of tuples representing the edges in the minimum cut.
    """
    parent = [-1] * len(graph)
    max_flow = 0
    res = []
    temp = [i[:] for i in graph]  # Record original graph, make a copy.

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0 and temp[i][j] > 0:
                res.append((i, j))

    return res


class TestMinCut(unittest.TestCase):
    def setUp(self):
        self.test_graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0],
        ]

    def test_min_cut(self):
        expected_result = [(1, 3), (4, 3), (4, 5)]
        result = min_cut(self.test_graph, source=0, sink=5)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
