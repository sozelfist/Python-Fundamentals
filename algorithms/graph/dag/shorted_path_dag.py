import unittest

Graph = dict[str, list[tuple[str, int]]]


def shortest_path_dag(graph: Graph, start: str) -> dict[str, float]:
    """
    Function to find the shortest path in a directed acyclic graph
    (DAG) using topological sorting.

    Args:
    graph (dict): A dictionary representing the DAG with nodes as
    keys and a list of (node, weight) pairs as values.
    start (str): The starting node.

    Returns:
    dict: A dictionary with the shortest distances from the start
    node to all other nodes in the DAG.
    """
    # Step 1: Topologically sort the nodes in the DAG
    def topological_sort(graph):
        visited = set()
        stack = []

        def visit(node):
            if node not in visited:
                visited.add(node)
                for neighbor, _ in graph[node]:
                    visit(neighbor)
                stack.append(node)

        for node in graph:
            visit(node)

        return stack[::-1]

    # Step 2: Perform the shortest path algorithm
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    sorted_nodes = topological_sort(graph)

    for node in sorted_nodes:
        for neighbor, weight in graph[node]:
            dist[neighbor] = min(dist[neighbor], dist[node] + weight)

    return dist


class TestShortestPathDAG(unittest.TestCase):
    def test_shortest_path_dag(self):
        graph = {
            'A': [('B', 3), ('C', 2)],
            'B': [('C', 1), ('D', 4)],
            'C': [('D', 2), ('E', 1)],
            'D': [('E', 3)],
            'E': []
        }
        start = 'A'

        expected_distances = {'A': 0, 'B': 3, 'C': 2, 'D': 4, 'E': 3}

        actual_distances = shortest_path_dag(graph, start)

        self.assertEqual(actual_distances, expected_distances)

    def test_shortest_path_dag_empty_graph(self):
        graph = {}
        start = 'A'

        expected_distances = {'A': 0}

        actual_distances = shortest_path_dag(graph, start)

        self.assertEqual(actual_distances, expected_distances)

    def test_shortest_path_dag_unreachable_node(self):
        graph = {
            'A': [('B', 3), ('C', 2)],
            'B': [('C', 1), ('D', 4)],
            'C': [('D', 2), ('E', 1)],
            'D': [('E', 3)],
            'E': [],
            'F': []
        }
        start = 'F'

        expected_distances = {'A': float('inf'), 'B': float('inf'), 'C': float(
            'inf'), 'D': float('inf'), 'E': float('inf'), 'F': 0}

        actual_distances = shortest_path_dag(graph, start)

        self.assertEqual(actual_distances, expected_distances)


if __name__ == '__main__':
    unittest.main()
