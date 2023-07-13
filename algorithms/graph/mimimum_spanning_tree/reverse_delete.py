import unittest

Graph = list[list[int]]


def reverse_delete_algorithm(adj_matrix: Graph) -> Graph:
    """
    Given a weighted graph represented as an adjacency matrix, returns
    the minimum spanning tree using the reverse delete algorithm.

    Args:
        adj_matrix (list[list[int]]): The adjacency matrix representing
        the weighted graph.

    Returns:
        list[list[int]]: The adjacency matrix representing the minimum
        spanning tree.

    """
    # Create list of edges of the input graph
    edges = []
    for i in range(len(adj_matrix)):
        for j in range(i + 1, len(adj_matrix)):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))

    # Sort the edges in decreasing order of weight
    edges.sort(key=lambda edge: edge[2], reverse=True)

    # Create a set of vertices that are currently connected
    connected = set(range(len(adj_matrix)))

    # Iterate over the edges in decreasing order of weight
    for edge in edges:
        # Check if removing the edge would disconnect the graph
        if len(connected) > 1:
            if edge[0] in connected and edge[1] in connected:
                # Remove the edge from the graph
                adj_matrix[edge[0]][edge[1]] = 0
                adj_matrix[edge[1]][edge[0]] = 0
                # Check if the removal of the edge has disconnected the graph
                if not is_connected(adj_matrix, connected):
                    # Add the edge back to the graph
                    adj_matrix[edge[0]][edge[1]] = edge[2]
                    adj_matrix[edge[1]][edge[0]] = edge[2]
                else:
                    # Update the set of connected vertices
                    connected = set(get_connected_vertices(adj_matrix))
        else:
            break

    # Return the modified adjacency matrix
    return adj_matrix


def is_connected(adj_matrix: Graph, connected: set[int]) -> bool:
    """ Helper function to check if a graph is connected. """
    visited = [False] * len(adj_matrix)
    stack = [next(iter(connected))]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for i in range(len(adj_matrix)):
                if adj_matrix[v][i] != 0 and i in connected:
                    stack.append(i)
    return all(visited)


def get_connected_vertices(adj_matrix: Graph) -> set[int]:
    """ Helper function to get the set of connected vertices in a graph. """
    visited = [False] * len(adj_matrix)
    stack = [0]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for i in range(len(adj_matrix)):
                if adj_matrix[v][i] != 0 and not visited[i]:
                    stack.append(i)
    return {i for i in range(len(adj_matrix)) if visited[i]}


class TestReverseDeleteAlgorithm(unittest.TestCase):

    def test_reverse_delete_algorithm(self):
        graph = [
            [0, 2, 3, 0],
            [2, 0, 1, 3],
            [3, 1, 0, 4],
            [0, 3, 4, 0]
        ]
        mst = reverse_delete_algorithm(graph)
        self.assertEqual(mst, [
            [0, 2, 0, 0],
            [2, 0, 1, 3],
            [0, 1, 0, 0],
            [0, 3, 0, 0]
        ])
        self.assertEqual(sum(sum(row) for row in mst) / 2, 6)

    def test_reverse_delete_algorithm_empty_graph(self):
        graph = []
        mst = reverse_delete_algorithm(graph)
        self.assertEqual(mst, [])

    def test_reverse_delete_algorithm_singleton_graph(self):
        graph = [[0]]
        mst = reverse_delete_algorithm(graph)
        self.assertEqual(mst, [[0]])

    def test_reverse_delete_algorithm_complete_graph(self):
        graph = [
            [0, 2, 3],
            [2, 0, 1],
            [3, 1, 0]
        ]
        mst = reverse_delete_algorithm(graph)
        self.assertEqual(mst, [
            [0, 2, 0],
            [2, 0, 1],
            [0, 1, 0]
        ])
        self.assertEqual(sum(sum(row) for row in mst) / 2, 3)


if __name__ == '__main__':
    unittest.main()
