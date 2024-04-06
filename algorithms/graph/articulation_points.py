import unittest


def articulation_points(graph: dict[int, list[int]]) -> set[int]:
    """
    Returns a set of articulation points in an undirected graph.
    """

    def dfs(
        u: int,
        parent: int,
        visited: set[int],
        disc: list[int],
        low: list[int],
        ap: set[int],
    ):
        """
        Depth-first search to find articulation points.
        """
        # Count the number of children in the DFS tree.
        children = 0

        # Mark the current node as visited.
        visited.add(u)

        # Initialize discovery time and low value.
        disc[u] = dfs.time
        low[u] = dfs.time
        dfs.time += 1

        # Visit all neighbors of the current node.
        for v in graph[u]:
            if v not in visited:
                children += 1
                dfs(v, u, visited, disc, low, ap)

                # Update low value of u for parent function calls.
                low[u] = min(low[u], low[v])

                # Case 1: u is the root of the DFS tree
                # and has two or more children.
                if parent is None and children > 1:
                    ap.add(u)

                # Case 2: u is not the root of the DFS tree and has a child v
                # such that no backedge from a descendant of v to u
                # can be found.
                elif parent is not None and low[v] >= disc[u]:
                    ap.add(u)

            # Update low value of u for backedge function calls.
            elif v != parent:
                low[u] = min(low[u], disc[v])

    # Initialize variables.
    visited = set()
    disc = [-1] * (len(graph))
    low = [-1] * (len(graph))
    ap = set()
    dfs.time = 0

    # Call DFS for every unvisited vertex.
    for u in graph.keys():
        if u not in visited:
            dfs(u, None, visited, disc, low, ap)

    return ap


class TestArticulationPoints(unittest.TestCase):
    def test_empty_graph(self):
        # Test an empty graph.
        graph = {}
        self.assertEqual(articulation_points(graph), set())

    def test_single_node(self):
        # Test a graph with a single node.
        graph = {0: []}
        self.assertEqual(articulation_points(graph), set())

    def test_two_nodes(self):
        # Test a graph with two nodes and one edge.
        graph = {0: [1], 1: [0]}
        self.assertEqual(articulation_points(graph), set())

    def test_two_nodes_disconnected(self):
        # Test a graph with two nodes and no edges.
        graph = {0: [], 1: []}
        self.assertEqual(articulation_points(graph), set())

    def test_five_nodes(self):
        # Test a graph with five nodes and multiple articulation points.
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
        self.assertEqual(articulation_points(graph), {2, 3})

    def test_four_nodes(self):
        # Test a graph with four nodes and one articulation point.
        graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
        self.assertEqual(articulation_points(graph), set())

    def test_four_nodes_disconnected(self):
        # Test a graph with four nodes and a disconnected component.
        graph = {0: [1], 1: [0], 2: [3], 3: [2]}
        self.assertEqual(articulation_points(graph), set())


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
