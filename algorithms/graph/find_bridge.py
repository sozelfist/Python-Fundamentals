import unittest


def find_bridges(
    n: int, edges: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    bridges = []
    discovery_time = [-1] * n
    lowest_reachable = [-1] * n
    visited = [False] * n
    time = 0

    def dfs(u: int, parent: int) -> None:
        nonlocal time
        visited[u] = True
        discovery_time[u] = lowest_reachable[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                dfs(v, u)
                lowest_reachable[u] = min(
                    lowest_reachable[u], lowest_reachable[v])
                if lowest_reachable[v] > discovery_time[u]:
                    bridges.append((u, v))
            elif v != parent:
                lowest_reachable[u] = min(
                    lowest_reachable[u], discovery_time[v])

    for u in range(n):
        if not visited[u]:
            dfs(u, -1)

    return bridges


class TestFindBridges(unittest.TestCase):
    def test_simple_graph(self):
        n = 3
        edges = [(0, 1), (1, 2)]
        bridges = find_bridges(n, edges)
        self.assertEqual(bridges, [(1, 2), (0, 1)])

    def test_graph_with_bridge(self):
        n = 5
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 2)]
        bridges = find_bridges(n, edges)
        self.assertEqual(bridges, [(1, 2), (0, 1)])

    def test_disconnected_graph(self):
        n = 6
        edges = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)]
        bridges = find_bridges(n, edges)
        self.assertEqual(bridges, [])

    def test_complex_graph(self):
        n = 7
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4),
                 (3, 4), (3, 5), (4, 5), (5, 6)]
        bridges = find_bridges(n, edges)
        self.assertEqual(bridges, [(5, 6)])


if __name__ == '__main__':
    unittest.main()
