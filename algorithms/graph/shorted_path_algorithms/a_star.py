import heapq
import unittest


def a_star(adj_list: list[list[tuple[int, int]]], heuristics: list[int], start: int, goal: int) -> list[int]:
    n = len(adj_list)
    dist = {v: float('inf') for v in range(n)}
    dist[start] = 0
    queue = [(0, start)]
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
                heapq.heappush(queue, (cost + heuristics[neighbor], neighbor))

    if goal not in came_from:
        return []

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]

    return path[::-1]


class TestAStar(unittest.TestCase):
    def test_case_1(self):
        adj_list = [[(1, 1), (2, 2)], [(0, 1), (3, 3)], [(0, 2)], [(1, 3)]]
        heuristics = [0, 1, 2, 3]
        start = 0
        goal = 3
        expected = [0, 1, 3]
        result = a_star(adj_list, heuristics, start, goal)
        self.assertEqual(result, expected)

    def test_case_2(self):
        adj_list = [[(1, 1), (2, 2)], [(0, 1), (3, 3)], [(0, 2)], [(1, 3)]]
        heuristics = [0, 1, 2, 3]
        start = 3
        goal = 0
        expected = [3, 1, 0]
        result = a_star(adj_list, heuristics, start, goal)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
