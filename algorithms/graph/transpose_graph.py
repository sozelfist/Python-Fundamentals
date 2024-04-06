import unittest


def transpose_graph(graph: dict[int, list[int]]):
    # Create a dictionary to store the transposed
    # graph as an adjacency list
    transposed_graph = {v: [] for v in graph}

    # Iterate over each vertex in the original graph
    for v in graph:
        # Iterate over each neighbor of the vertex
        for neighbor in graph[v]:
            # Add the vertex as a neighbor of the neighbor
            # in the transposed graph
            transposed_graph[neighbor].append(v)

    return transposed_graph


class TestTransposeGraph(unittest.TestCase):
    def test_empty_graph(self):
        graph1 = {}
        expected1 = {}
        self.assertEqual(transpose_graph(graph1), expected1)

    def test_graph_with_single_vertex(self):
        graph2 = {1: []}
        expected2 = {1: []}
        self.assertEqual(transpose_graph(graph2), expected2)

    def test_graph_with_disconnected_vertices(self):
        graph3 = {1: [], 2: [], 3: []}
        expected3 = {1: [], 2: [], 3: []}
        self.assertEqual(transpose_graph(graph3), expected3)

    def test_graph_with_directed_edges(self):
        graph4 = {1: [2, 3], 2: [3, 4], 3: [4], 4: [1]}
        expected4 = {1: [4], 2: [1], 3: [1, 2], 4: [2, 3]}
        self.assertEqual(transpose_graph(graph4), expected4)

    def test_graph_with_self_loops(self):
        graph5 = {1: [1], 2: [2, 3], 3: [], 4: [1, 2, 3]}
        expected5 = {1: [1, 4], 2: [2, 4], 3: [2, 4], 4: []}
        self.assertEqual(transpose_graph(graph5), expected5)


if __name__ == "__main__":
    unittest.main()
