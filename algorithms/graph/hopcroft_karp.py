import unittest

# Type hint for graph represented as adjacency list
Graph = dict[int, list[int]]


def hopcroft_karp(graph: Graph) -> dict[int, int]:
    """
    Hopcroft-Karp algorithm for finding maximum cardinality
    matching in a bipartite graph.

    Args:
        graph (Dict[int, List[int]]): The bipartite graph
        represented as an adjacency list, where the keys
        represent the vertices on the left side of the
        bipartition and the values represent the vertices
        on the right side of the bipartition.

    Returns:
        Dict[int, int]: A dictionary representing the maximum
        cardinality matching, where the keys are the
        vertices on the left side of the bipartition and
        the values are the vertices on the right side
        of the bipartition. If a vertex on the left side
        does not have a matching, its value is set to -1.
    """

    def dfs(u: int) -> bool:
        """Depth-first search to find augmenting paths."""
        if u == -1:
            return True

        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                if match_r[v] == -1 or dfs(match_r[v]):
                    match_r[v] = u
                    match_l[u] = v
                    return True
        return False

    # Initialize matching
    match_l: dict[int, int] = {}  # Left-side matching
    match_r: dict[int, int] = {}  # Right-side matching

    for u in graph.keys():
        match_l[u] = -1
    for v in {v for vertices in graph.values() for v in vertices}:
        match_r[v] = -1

    # Augmenting path search
    match_count = 0
    while True:
        seen: set[int] = set()
        for u in graph.keys():
            if match_l[u] == -1 and dfs(u):
                match_count += 1
        if match_count == len(graph):
            break

    return match_l


class TestHopcroftKarp(unittest.TestCase):

    def test_empty_graph(self):
        graph = {}
        self.assertEqual(hopcroft_karp(graph), {})

    def test_graph_with_one_vertex_on_each_side(self):
        graph = {1: [4], 2: [5], 3: [6]}
        expected_matching = {1: 4, 2: 5, 3: 6}
        self.assertEqual(hopcroft_karp(graph), expected_matching)

    def test_graph_with_multiple_edges_between_vertices(self):
        graph = {1: [4, 5], 2: [4, 6], 3: [5]}
        expected_matching = {1: 4, 2: 6, 3: 5}
        self.assertEqual(hopcroft_karp(graph), expected_matching)


if __name__ == '__main__':
    unittest.main()
