import unittest
from typing import List, Tuple
import heapq


def a_star(adj_list: List[List[Tuple[int, int]]], heuristics: List[int], start: int, goal: int) -> List[int]:
    n = len(adj_list)
    dist = {v: float('inf') for v in range(n)}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {v: None for v in range(n)}

    while queue:
        current = heapq.heappop(queue)[1]

        if current == goal:
            break

        for neighbor, weight in adj_list[current]:
            cost = dist[current] + weight + heuristics[neighbor] - heuristics[current]
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                came_from[neighbor] = current
                heapq.heappush(queue, (dist[neighbor], neighbor))

    if goal not in came_from:
        return []

    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]


class TestAStar(unittest.TestCase):
    def test_a_star_valid_input(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], []]
        heuristics = [0, 2, 3, 7]
        start = 0
        goal = 3
        expected_output = [0, 1, 2, 3]
        self.assertEqual(a_star(adj_list, heuristics, start, goal), expected_output)

    def test_a_star_no_path(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], []]
        heuristics = [0, 2, 3, 7]
        start = 0
        goal = 4
        expected_output = []
        self.assertEqual(a_star(adj_list, heuristics, start, goal), expected_output)

    def test_a_star_disconnected_graph(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], [], [(4, 1)]]
        heuristics = [0, 2, 3, 7, 1]
        start = 0
        goal = 4
        expected_output = []
        self.assertEqual(a_star(adj_list, heuristics, start, goal), expected_output)

    def test_a_star_single_vertex(self):
        adj_list = [[]]
        heuristics = [0]
        start = 0
        goal = 0
        expected_output = [0]
        self.assertEqual(a_star(adj_list, heuristics, start, goal), expected_output)

    def test_a_star_large_graph(self):
        adj_list = [[(i + 1, i) for i in range(1000)], *[[(i + 2, i + 1) for i in range(999)], []]]
        heuristics = list(range(1001))
        start = 0
        goal = 1000
        expected_output = list(range(1001))
        self.assertEqual(a_star(adj_list, heuristics, start, goal), expected_output)


if __name__ == '__main__':
    unittest.main()
