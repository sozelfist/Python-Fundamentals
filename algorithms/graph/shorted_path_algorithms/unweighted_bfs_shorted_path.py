import unittest
from collections import deque


def shortest_path_bfs(
    graph: dict[int, list[int]], start: int, end: int
) -> list[int] | None:
    """
    Find the shortest path between two vertices in an unweighted
    graph using Breadth-First Search (BFS).

    Args:
        graph (Dict[int, List[int]]): The adjacency list representation
        of the graph.
        start (int): The starting vertex.
        end (int): The target vertex.

    Returns:
        Optional[List[int]]: The shortest path as a list of vertices,
        including start and end vertices. Returns None if there is no
        path between the start and end vertices.
    """
    # Create a queue for BFS traversal
    queue = deque([(start, [])])

    # Create a set to keep track of visited vertices
    visited = set()

    while queue:
        # Get the next vertex and its path from the queue
        vertex, path = queue.popleft()

        if vertex == end:
            # Found the target vertex, return the path
            return path + [vertex]

        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    # Add unvisited neighbors to the queue with updated path
                    queue.append((neighbor, path + [vertex]))

    return None  # No path found


class ShortestPathBFSTest(unittest.TestCase):
    def setUp(self):
        self.graph = {1: [2, 3],
                      2: [1, 3, 4],
                      3: [1, 2, 4, 5],
                      4: [2, 3, 5],
                      5: [3, 4]}

    def test_shortest_path_exists(self):
        start_vertex = 1
        end_vertex = 5
        expected_path = [1, 3, 5]
        result = shortest_path_bfs(self.graph, start_vertex, end_vertex)
        self.assertEqual(
            result, expected_path,
            f"Failed for start={start_vertex} and end={end_vertex}"
        )

    def test_shortest_path_not_exists(self):
        start_vertex = 1
        end_vertex = 6
        expected_path = None
        result = shortest_path_bfs(self.graph, start_vertex, end_vertex)
        self.assertEqual(
            result, expected_path,
            f"Failed for start={start_vertex} and end={end_vertex}"
        )

    def test_start_end_same_vertex(self):
        start_vertex = 1
        end_vertex = 1
        expected_path = [1]
        result = shortest_path_bfs(self.graph, start_vertex, end_vertex)
        self.assertEqual(
            result, expected_path,
            f"Failed for start={start_vertex} and end={end_vertex}"
        )

    def test_single_vertex_graph(self):
        graph = {1: []}
        start_vertex = 1
        end_vertex = 1
        expected_path = [1]
        result = shortest_path_bfs(graph, start_vertex, end_vertex)
        self.assertEqual(
            result, expected_path,
            f"Failed for start={start_vertex} and end={end_vertex}"
        )


if __name__ == '__main__':
    unittest.main()
