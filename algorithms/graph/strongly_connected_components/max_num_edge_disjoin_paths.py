import unittest


def find_edge_disjoint_paths(
    graph: list[list[int]], source: int, target: int
) -> list[list[int]]:
    """
    Find the maximum number of edge-disjoint paths between
    source and target vertices in a directed graph.

    Args:
        graph (List[List[int]]): The graph represented as an adjacency list.
        source (int): The source vertex.
        target (int): The target vertex.

    Returns:
        List[List[int]]: A list of edge-disjoint paths between
        the source and target vertices.
    """
    def dfs(v: int, path: list[int]) -> list[list[int]]:
        if v == target:
            return [path]
        result = []
        for neighbor in graph[v]:
            if neighbor not in path:
                result.extend(dfs(neighbor, path + [neighbor]))
        return result

    # Initialize the list of edge-disjoint paths
    edge_disjoint_paths = []

    # Find edge-disjoint paths using depth-first search (DFS)
    while True:
        path = dfs(source, [source])
        if not path:
            break
        edge_disjoint_paths.append(path[0])
        # Remove edges of the found path from the graph
        for i in range(len(path[0]) - 1):
            u, v = path[0][i], path[0][i + 1]
            graph[u].remove(v)

    return edge_disjoint_paths


class TestFindEdgeDisjointPaths(unittest.TestCase):
    def test_graph_with_one_edge_disjoint_path(self):
        graph1 = [[1, 2], [], [3], []]
        source1 = 0
        target1 = 3
        expected1 = [[0, 2, 3]]
        self.assertEqual(find_edge_disjoint_paths(
            graph1, source1, target1), expected1)

    def test_graph_with_multiple_edge_disjoint_paths(self):
        graph2 = [[1, 2], [2, 3], [3, 4], [4], []]
        source2 = 0
        target2 = 4
        expected2 = [[0, 1, 2, 3, 4], [0, 2, 4]]
        self.assertEqual(find_edge_disjoint_paths(
            graph2, source2, target2), expected2)

    def test_graph_with_no_edge_disjoint_paths(self):
        graph3 = [[1, 2], [2], [1], []]
        source3 = 0
        target3 = 3
        expected3 = []
        self.assertEqual(find_edge_disjoint_paths(
            graph3, source3, target3), expected3)

    def test_graph_with_multiple_paths_but_not_all_are_edge_disjoint(self):
        graph4 = [[1, 2], [2, 3], [3, 4], [4], [1]]
        source4 = 0
        target4 = 4
        expected4 = [[0, 1, 2, 3, 4], [0, 2, 4]]
        self.assertEqual(find_edge_disjoint_paths(
            graph4, source4, target4), expected4)

    def test_graph_with_disconnected_components(self):
        graph5 = [[1], [0], [3], [2], []]
        source5 = 0
        target5 = 4
        expected5 = []
        self.assertEqual(find_edge_disjoint_paths(
            graph5, source5, target5), expected5)


if __name__ == '__main__':
    unittest.main()
