import heapq
import unittest
from typing import Any

Graph = dict[str, Any]


def beam_search(
    graph: Graph, start: str, goal: str, beam_width: int
) -> list[str] | None:
    """
    Find the shortest path between the `start` and `goal` nodes in a graph
    using beam search.

    Args:
        graph (dict): A dictionary representation of the graph, where the
        keys are the node names and the values are dictionaries that map
        to the connected nodes and their edge weights.
        start (str): The name of the starting node in the graph.
        goal (str): The name of the goal node in the graph.
        beam_width (int): The width of the beam to use in the search.

    Returns:
        A list of node names representing the shortest path from `start`
        to `goal`, or `None` if no path exists.
    """

    if start not in graph:
        raise ValueError(f"Start node {start} is not in the graph")
    if goal not in graph:
        raise ValueError(f"Goal node {goal} is not in the graph")
    if beam_width <= 0:
        raise ValueError("Beam width must be a positive integer")

    visited = set()
    queue = [(0, [start])]

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_cost = cost + graph[node][neighbor]
                heapq.heappush(queue, (new_cost, new_path))
        if len(queue) > beam_width:
            queue = heapq.nsmallest(beam_width, queue)

    return None


class TestBeamSearch(unittest.TestCase):
    def test_basic_path(self):
        graph = {
            "A": {"B": 2, "C": 1},
            "B": {"D": 5, "E": 4},
            "C": {"F": 3},
            "D": {"G": 6},
            "E": {"G": 3},
            "F": {"G": 7},
            "G": {},
        }
        start = "A"
        goal = "G"
        beam_width = 2

        expected_path = ["A", "B", "E", "G"]
        self.assertEqual(beam_search(graph, start, goal, beam_width), expected_path)

    def test_no_path(self):
        graph = {"A": {"B": 1}, "B": {}, "C": {}}
        start = "A"
        goal = "C"
        beam_width = 1
        self.assertIsNone(beam_search(graph, start, goal, beam_width))

    def test_invalid_start_node(self):
        graph = {"A": {"B": 1}, "B": {"C": 1}, "C": {}}
        start = "D"
        goal = "C"
        beam_width = 1
        with self.assertRaises(ValueError):
            beam_search(graph, start, goal, beam_width)

    def test_invalid_goal_node(self):
        graph = {"A": {"B": 1}, "B": {"C": 1}, "C": {}}
        start = "A"
        goal = "D"
        beam_width = 1
        with self.assertRaises(ValueError):
            beam_search(graph, start, goal, beam_width)

    def test_negative_beam_width(self):
        graph = {"A": {"B": 1}, "B": {"C": 1}, "C": {}}
        start = "A"
        goal = "C"
        beam_width = -1
        with self.assertRaises(ValueError):
            beam_search(graph, start, goal, beam_width)

    def test_zero_beam_width(self):
        graph = {"A": {"B": 1}, "B": {"C": 1}, "C": {}}
        start = "A"
        goal = "C"
        beam_width = 0
        with self.assertRaises(ValueError):
            beam_search(graph, start, goal, beam_width)


if __name__ == "__main__":
    unittest.main()
