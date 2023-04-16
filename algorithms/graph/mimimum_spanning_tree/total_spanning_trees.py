import unittest


def count_spanning_trees(adj_matrix: list[list[int]]) -> int:
    """
    Counts the total number of spanning trees in an undirected
    graph using Kirchhoff's matrix tree theorem.

    Args:
        adj_matrix (List[List[int]]): The adjacency matrix of the graph.

    Returns:
        int: The total number of spanning trees in the graph.
    """
    # Get the number of vertices in the graph
    n = len(adj_matrix)

    # Initialize the Laplacian matrix
    laplacian = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the Laplacian matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                # Diagonal element is the degree of vertex i
                laplacian[i][j] = sum(adj_matrix[i])
            else:
                # Off-diagonal element is the negative of the adjacency matrix
                laplacian[i][j] = -adj_matrix[i][j]

    # Compute the determinant of the Laplacian matrix
    det = determinant(laplacian)

    # According to Kirchhoff's matrix tree theorem, the total
    # number of spanning trees is the determinant of any cofactor
    # of the Laplacian matrix
    return det


def determinant(matrix: list[list[int]]) -> int:
    """
    Computes the determinant of a square matrix using recursion.

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        int: The determinant of the matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        det = 0
        for j in range(n):
            # Compute the cofactor of the first row and j-th column
            cofactor = [[matrix[i][j]
                         for j in range(1, n)] for i in range(1, n)]
            det += ((-1) ** j) * matrix[0][j] * determinant(cofactor)
        return det


class TestSpanningTrees(unittest.TestCase):

    def test_count_spanning_trees_nonempty_graph(self):
        # Test case for a non-empty graph
        adj_matrix = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        expected_count = 144
        self.assertEqual(count_spanning_trees(adj_matrix), expected_count)

    def test_count_spanning_trees_single_vertex(self):
        # Test case for a graph with only one vertex
        adj_matrix = [
            [0]
        ]
        expected_count = 0
        self.assertEqual(count_spanning_trees(adj_matrix), expected_count)

    def test_count_spanning_trees_empty_graph(self):
        # Test case for an empty graph (all zero adjacency matrix)
        adj_matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_count = 0
        self.assertEqual(count_spanning_trees(adj_matrix), expected_count)

    def test_count_spanning_trees_disconnected_graph(self):
        # Test case for a disconnected graph (adjacency matrix
        # with disconnected components)
        adj_matrix = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_count = 0
        self.assertEqual(count_spanning_trees(adj_matrix), expected_count)


if __name__ == '__main__':
    unittest.main()
