import unittest
from typing import Any, List, Union


def edmonds_karp(graph: Any, source: int, sink: int) -> Union[int, float]:
    n = len(graph)
    parent = [-1] * n
    max_flow = 0

    while True:
        bfs_result = bfs(graph, source, sink, parent)
        if not bfs_result:
            break
        flow = float("inf")
        s = sink
        while s != source:
            u = parent[s]
            flow = min(flow, graph[u][s][1])
            s = parent[s]
        max_flow += flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] = (graph[u][v][0], graph[u][v][1] - flow)
            graph[v][u] = (graph[v][u][0], graph[v][u][1] + flow)
            v = parent[v]
    return max_flow


def bfs(graph: Any, source: int, sink: int, parent: List[int]) -> bool:
    n = len(graph)
    visited = [False] * n
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v in range(n):
            if not visited[v] and graph[u][v][1] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True
                if v == sink:
                    return True
    return False


class TestEdmondsKarp(unittest.TestCase):
    def test_case_1(self):
        graph = [[(0, 0) for j in range(6)] for i in range(6)]
        graph[0][1] = (1, 16)
        graph[0][2] = (2, 13)
        graph[1][2] = (3, 10)
        graph[1][3] = (4, 12)
        graph[2][4] = (5, 14)
        graph[3][2] = (6, 9)
        graph[3][5] = (7, 20)
        graph[4][3] = (8, 7)
        graph[4][5] = (9, 4)

        source, sink = 0, 5
        max_flow = edmonds_karp(graph, source, sink)

        self.assertEqual(max_flow, 23)

    def test_case_2(self):
        graph = [[(0, 0) for j in range(4)] for i in range(4)]
        graph[0][1] = (1, 3)
        graph[0][2] = (2, 5)
        graph[1][3] = (3, 4)
        graph[2][3] = (4, 2)

        source, sink = 0, 3
        max_flow = edmonds_karp(graph, source, sink)

        self.assertEqual(max_flow, 5)


if __name__ == '__main__':
    unittest.main()
