import unittest

import numpy as np


def viterbi_shortest_path(graph, source):
    """
    Viterbi algorithm for finding the shortest path in a weighted graph.

    Args:
        graph (dict): Weighted graph represented as an adjacency list,
                      where keys are the vertices and values are dictionaries
                      of neighboring vertices and their corresponding
                      edge weights.
        source (int): Source vertex to start the shortest path from.

    Returns:
        dict: Dictionary containing the shortest path distances from
              the source vertex to all other vertices in the graph,
              where keys are the vertices and values are the corresponding
              shortest path distances.
    """
    # Initialize the shortest path distances with infinity for
    # all vertices except the source vertex
    dist = {v: np.inf for v in graph.keys()}
    dist[source] = 0

    # Initialize the backpointers for the shortest path
    backpointers = {}

    # Iterate over the vertices in the graph
    for v in graph.keys():
        # Update the shortest path distances for each neighboring vertex of v
        for neighbor, weight in graph[v].items():
            if dist[v] + weight < dist[neighbor]:
                dist[neighbor] = dist[v] + weight
                backpointers[neighbor] = v

    return dist, backpointers


def get_shortest_path(backpointers, target):
    """
    Helper function to reconstruct the shortest path from the backpointers.

    Args:
        backpointers (dict): Dictionary containing the backpointers for the
                             shortest path, where keys are the vertices
                             and values are the corresponding backpointers.
        target (int): Target vertex to find the shortest path to.

    Returns:
        list: Shortest path from the source vertex to the target vertex,
              represented as a list of vertices in the path.
    """
    path = [target]
    while target in backpointers:
        target = backpointers[target]
        path.append(target)
    return path[::-1]


class TestViterbiShortestPath(unittest.TestCase):
    def setUp(self):
        """Example weighted graph represented as an adjacency list."""
        self.graph = {0: {1: 2, 2: 4}, 1: {3: 1}, 2: {3: 3}, 3: {4: 1}, 4: {}}
        self.source = 0
        self.target = 4

    def test_viterbi_shortest_path(self):
        shortest_distances, backpointers = viterbi_shortest_path(
            self.graph, self.source
        )
        self.assertEqual(shortest_distances, {0: 0, 1: 2, 2: 4, 3: 3, 4: 4})
        self.assertEqual(backpointers, {1: 0, 2: 0, 3: 1, 4: 3})

    def test_get_shortest_path(self):
        backpointers = {1: 0, 2: 0, 3: 1, 4: 3}
        shortest_path = get_shortest_path(backpointers, self.target)
        self.assertEqual(shortest_path, [0, 1, 3, 4])


if __name__ == "__main__":
    unittest.main()
