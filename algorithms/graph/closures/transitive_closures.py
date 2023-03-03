from typing import List
import unittest


def transitive_closure(graph: List[List[int]]) -> List[List[int]]:
    """
    Calculates the transitive closure of a directed graph using Warshall's algorithm.

    Args:
        graph: A list of lists representing the adjacency matrix of the graph. Each
            row i represents the outgoing edges from vertex i, where graph[i][j] is 1
            if there is a directed edge from i to j, and 0 otherwise.

    Returns:
        A list of lists representing the adjacency matrix of the transitive closure of
        the graph. Each row i represents the outgoing edges from vertex i, where the
        value of transitive_closure[i][j] is 1 if there is a directed path from i to j
        in the original graph, and 0 otherwise.

    Raises:
        ValueError: If the input matrix is not square or contains invalid entries.
    """

    # Check that the input is a square matrix
    num_vertices = len(graph)
    if num_vertices != len(graph[0]):
        raise ValueError("Input matrix must be square")

    # Check that the input matrix contains only 0's and 1's
    for row in graph:
        for entry in row:
            if entry not in {0, 1}:
                raise ValueError("Input matrix must contain only 0's and 1's")

    # Create a copy of the original graph to avoid modifying it
    transitive_closure = [row[:] for row in graph]

    # Use Warshall's algorithm to calculate the transitive closure
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                transitive_closure[i][j] = transitive_closure[i][j] \
                    or (transitive_closure[i][k] and transitive_closure[k][j])

    return transitive_closure


class TestTransitiveClosure(unittest.TestCase):

    def test_basic_graph(self):
        graph = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        expected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(transitive_closure(graph), expected)

    def test_disconnected_graph(self):
        graph = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        expected = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
        self.assertEqual(transitive_closure(graph), expected)

    def test_complete_graph(self):
        graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        expected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(transitive_closure(graph), expected)

    def test_self_loop_graph(self):
        graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(transitive_closure(graph), expected)

    def test_non_square_graph(self):
        graph = [[0, 1, 0], [0, 0, 1]]
        with self.assertRaises(ValueError):
            transitive_closure(graph)

    def test_invalid_entry_graph(self):
        graph = [[0, 1, 0], [0, 2, 1], [1, 0, 0]]
        with self.assertRaises(ValueError):
            transitive_closure(graph)


if __name__ == '__main__':
    unittest.main()
