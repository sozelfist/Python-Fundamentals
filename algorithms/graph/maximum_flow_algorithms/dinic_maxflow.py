import unittest

INF = float("inf")


class Edge:
    def __init__(self, to: int, cap: int, rev: int) -> None:
        self.to = to
        self.cap = cap
        self.rev = rev


def add_edge(graph: list[list[Edge]], u: int, v: int, cap: int) -> None:
    if u < 0 or u >= len(graph) or v < 0 or v >= len(graph):
        raise ValueError("Invalid vertex index")
    if cap < 0:
        raise ValueError("Capacity must be non-negative")
    graph[u].append(Edge(v, cap, len(graph[v])))
    graph[v].append(Edge(u, 0, len(graph[u]) - 1))


def bfs(graph: list[list[Edge]], level: list[int], s: int, t: int) -> bool:
    if s < 0 or s >= len(graph) or t < 0 or t >= len(graph):
        raise ValueError("Invalid vertex index")
    level[:] = [-1] * len(graph)
    level[s] = 0
    queue = [s]

    while queue:
        u = queue.pop(0)
        for e in graph[u]:
            if e.cap > 0 and level[e.to] < 0:
                level[e.to] = level[u] + 1
                queue.append(e.to)

    return level[t] >= 0


def dfs(
    graph: list[list[Edge]], level: list[int], iter: list[int],
    u: int, t: int, f: int
) -> int:
    if u < 0 or u >= len(graph) or t < 0 or t >= len(graph):
        raise ValueError("Invalid vertex index")
    if u == t:
        return f

    for i in range(iter[u], len(graph[u])):
        e = graph[u][i]
        if e.cap > 0 and level[u] < level[e.to]:
            d = dfs(graph, level, iter, e.to, t, min(f, e.cap))
            if d > 0:
                e.cap -= d
                graph[e.to][e.rev].cap += d
                return d

    return 0


def max_flow(graph: list[list[Edge]], s: int, t: int) -> int:
    if s < 0 or s >= len(graph) or t < 0 or t >= len(graph):
        raise ValueError("Invalid vertex index")
    level = [0] * len(graph)
    flow = 0

    while bfs(graph, level, s, t):
        iter = [0] * len(graph)
        while True:
            f = dfs(graph, level, iter, s, t, INF)  # type: ignore
            if f == 0:
                break
            flow += f

    return flow


class TestDinicMaxFlow(unittest.TestCase):
    def test_basic(self):
        n = 6
        s = 0
        t = 5
        graph = [[] for _ in range(n)]
        add_edge(graph, 0, 1, 16)
        add_edge(graph, 0, 2, 13)
        add_edge(graph, 1, 2, 10)
        add_edge(graph, 1, 3, 12)
        add_edge(graph, 2, 1, 4)
        add_edge(graph, 2, 4, 14)
        add_edge(graph, 3, 2, 9)
        add_edge(graph, 3, 5, 20)
        add_edge(graph, 4, 3, 7)
        add_edge(graph, 4, 5, 4)
        max_flow_val = max_flow(graph, s, t)
        self.assertEqual(max_flow_val, 23)

    def test_invalid_vertex_index(self):
        n = 6
        s = 0
        graph = [[] for _ in range(n)]
        with self.assertRaises(ValueError):
            add_edge(graph, -1, 2, 5)
        with self.assertRaises(ValueError):
            add_edge(graph, 0, n, 10)
        with self.assertRaises(ValueError):
            bfs(graph, [0] * n, s, n)
        with self.assertRaises(ValueError):
            dfs(graph, [0] * n, [0] * n, s, n, 5)
        with self.assertRaises(ValueError):
            max_flow(graph, s, n)

    def test_negative_capacity(self):
        n = 3
        graph = [[] for _ in range(n)]
        with self.assertRaises(ValueError):
            add_edge(graph, 0, 1, -1)
        with self.assertRaises(ValueError):
            add_edge(graph, 1, 2, -10)


if __name__ == '__main__':
    unittest.main()
