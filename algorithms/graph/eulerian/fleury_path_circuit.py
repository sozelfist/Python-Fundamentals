import unittest


def fleury(graph: list[list[int]]) -> list[int]:
    """
    Find and print an Eulerian path or circuit in an undirected graph
    using Fleury's Algorithm.

    Args:
        graph (List[List[int]]): The adjacency list representation
        of the undirected graph.

    Returns:
        List[int]: The list of vertices in the Eulerian path or circuit.
    """

    def is_bridge(u: int, v: int) -> bool:
        """Check if an edge (u, v) is a bridge in the graph."""
        if len(graph[u]) == 1:
            return True
        visited = [False] * len(graph)
        visited[u] = True
        stack = [v]
        while stack:
            node = stack.pop()
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        return not all(visited)

    def dfs(u: int) -> None:
        """Perform depth-first search from vertex u."""
        for v in graph[u]:
            if not visited[u][v] and (not is_bridge(u, v) or len(graph[u]) == 1):
                visited[u][v] = visited[v][u] = True
                dfs(v)
        path.append(u)

    # Check if the graph is empty
    if not graph:
        return []

    n = len(graph)
    visited = [[False] * n for _ in range(n)]
    start_vertex = 0  # Choose an arbitrary starting vertex
    for u in range(n):
        if len(graph[u]) % 2 != 0:
            start_vertex = u
            break
    path = []
    dfs(start_vertex)
    return path[::-1]  # Reverse the path to get the correct order


class FleuryTestCase(unittest.TestCase):
    def test_fleury_eulerian_path(self):
        graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]
        expected = [1, 0, 2, 1, 3, 2]
        self.assertEqual(fleury(graph), expected)

    def test_fleury_eulerian_circuit(self):
        graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
        expected = [0, 1, 3, 2, 0]
        self.assertEqual(fleury(graph), expected)

    def test_fleury_isolated_vertex(self):
        graph = [[], [3], [], [1]]
        expected = [1, 3]
        self.assertEqual(fleury(graph), expected)

    def test_fleury_single_vertex(self):
        graph = [[]]
        expected = [0]
        self.assertEqual(fleury(graph), expected)

    def test_fleury_empty_graph(self):
        graph = []
        expected = []
        self.assertEqual(fleury(graph), expected)


if __name__ == "__main__":
    unittest.main()
