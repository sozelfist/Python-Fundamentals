import unittest
from collections import defaultdict


def bfs(graph, U, match, dist):
    """
    Function to perform Breadth-First Search (BFS) in the Hopcroft-Karp
    algorithm.

    Args:
    graph: Dictionary representing the bipartite graph in adjacency
    list format.
    U: List of vertices in the first set (U).
    match: Dictionary representing the current matching.
    dist: Dictionary representing the distance from the source vertex.

    Returns:
    bool: True if an augmenting path is found, False otherwise.
    """
    queue = []
    for u in U:
        if match[u] is None:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float("inf")
    dist[None] = float("inf")

    while queue:
        u = queue.pop(0)
        if u is not None:
            for v in graph[u]:
                if dist[match[v]] == float("inf"):
                    dist[match[v]] = dist[u] + 1
                    queue.append(match[v])
    return dist[None] != float("inf")


def dfs(u, graph, match, dist):
    """
    Function to perform Depth-First Search (DFS) in the Hopcroft-Karp
    algorithm.

    Args:
    u: Vertex in the first set (U).
    graph: Dictionary representing the bipartite graph in adjacency
    list format.
    match: Dictionary representing the current matching.
    dist: Dictionary representing the distance from the source vertex.

    Returns:
    bool: True if an augmenting path is found, False otherwise.
    """
    if u is not None:
        for v in graph[u]:
            if dist[match[v]] == dist[u] + 1 and dfs(match[v], graph, match, dist):
                match[v] = u
                match[u] = v
                return True
        dist[u] = float("inf")
        return False
    return True


def max_bipartite_matching(graph):
    """
    Function to find the maximum bipartite matching in a given bipartite
    graph using Hopcroft-Karp algorithm.

    Args:
    graph: Dictionary representing the bipartite graph in adjacency list
           format. The keys represent vertices in the first set (U),
           and the values represent vertices in the second set (V).

    Returns:
    matching: Dictionary representing the maximum matching in the
              bipartite graph. The keys represent vertices in the
              first set (U), and the values represent vertices in
              the second set (V).
    """
    U = list(graph.keys())  # Vertices in the first set (U)
    # V = list(set(vertex for vertices in graph.values()
    #          for vertex in vertices))  # Vertices in the second set (V)

    match = defaultdict(lambda: None)  # Dictionary to store the matching
    dist = {}  # Dictionary to store the distance from the source vertex

    matching = 0  # Number of edges in the matching

    while bfs(graph, U, match, dist):
        for u in U:
            if match[u] is None and dfs(u, graph, match, dist):
                matching += 1

    # Construct the maximum matching in dictionary format
    max_matching = {}
    for u in U:
        if match[u] is not None:
            max_matching[u] = match[u]

    return max_matching


class BipartiteMatchingTestCase(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        expected = {}
        result = max_bipartite_matching(graph)
        self.assertEqual(result, expected)

    def test_graph_with_no_edges(self):
        graph = {"U1": [], "U2": [], "U3": []}
        expected = {}
        result = max_bipartite_matching(graph)
        self.assertEqual(result, expected)

    def test_graph_with_single_matching(self):
        graph = {"U1": ["V1"], "U2": ["V2"], "U3": ["V3"]}
        expected = {"U1": "V1", "U2": "V2", "U3": "V3"}
        result = max_bipartite_matching(graph)
        self.assertEqual(result, expected)

    def test_graph_with_multiple_matchings(self):
        graph = {"U1": ["V1", "V2"], "U2": ["V1", "V2"], "U3": ["V2", "V3"]}
        expected1 = {"U1": "V1", "U2": "V2", "U3": "V3"}
        expected2 = {"U1": "V2", "U2": "V1", "U3": "V3"}
        result = max_bipartite_matching(graph)
        self.assertTrue(result in [expected1, expected2])


if __name__ == "__main__":
    unittest.main()
