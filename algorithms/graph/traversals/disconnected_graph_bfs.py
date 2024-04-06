import unittest
from collections import deque

# Graph represented as an adjacency list
Graph = dict[int, list[int]]


def bfs_disconnected(graph: Graph) -> list[list[int]]:
    """
    Perform BFS on a disconnected graph and return a list of
    connected components.

    Args:
        graph: The graph represented as an adjacency list.

    Returns:
        A list of connected components, where each connected
        component is a list of nodes.
    """
    visited: set[int] = set()  # to keep track of visited nodes
    connected_components: list[list[int]] = []  # to store connected components

    for node in graph.keys():
        if node not in visited:
            connected_component: list[int] = []
            queue: deque[int] = deque([node])
            visited.add(node)

            while queue:
                current_node = queue.popleft()
                connected_component.append(current_node)

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            connected_components.append(connected_component)

    return connected_components


class TestBFSDisconnected(unittest.TestCase):
    def test_on_empty_graph(self):
        graph: Graph = {}
        expected: list[list[int]] = []
        self.assertEqual(bfs_disconnected(graph), expected)

    def test_on_graph_with_a_single_connected_component(self):
        graph: Graph = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: []}
        expected: list[list[int]] = [[1, 2, 3], [4]]
        self.assertEqual(bfs_disconnected(graph), expected)

    def test_on_graph_with_multiple_disconnected_components(self):
        graph: Graph = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [], 5: [], 6: [7], 7: [6]}
        expected: list[list[int]] = [[1, 2, 3], [4], [5], [6, 7]]
        self.assertEqual(bfs_disconnected(graph), expected)

    def test_on_graph_with_isolated_nodes(self):
        graph: Graph = {1: [], 2: [], 3: [], 4: []}
        expected: list[list[int]] = [[1], [2], [3], [4]]
        self.assertEqual(bfs_disconnected(graph), expected)


if __name__ == "__main__":
    unittest.main()
