import unittest
from typing import List, Tuple
import heapq


def dijkstra(adj_list: List[List[Tuple[int, int]]], start: int) -> List[int]:
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        (curr_dist, curr) = heapq.heappop(queue)
        if curr_dist > dist[curr]:
            continue
        for neighbor, weight in adj_list[curr]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(queue, (dist[neighbor], neighbor))
    return dist


class TestDijkstra(unittest.TestCase):
    def test_dijkstra_valid_input(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], []]
        start = 0
        expected_output = [0, 2, 3, 7]
        self.assertEqual(dijkstra(adj_list, start), expected_output)

    def test_dijkstra_negative_weights(self):
        adj_list = [[(1, -2), (2, 1)], [(2, -3)], [(0, -4), (1, 4)], []]
        start = 0
        expected_output = [0, -2, -1, 3]
        self.assertEqual(dijkstra(adj_list, start), expected_output)

    def test_dijkstra_disconnected_graph(self):
        adj_list = [[(1, 2), (2, 1)], [(2, 3)], [(0, 4), (1, 4)], [], [(4, 1)]]
        start = 0
        expected_output = [0, 2, 3, 7, float('inf')]
        self.assertEqual(dijkstra(adj_list, start), expected_output)

    def test_dijkstra_single_vertex(self):
        adj_list = [[]]
        start = 0
        expected_output = [0]
        self.assertEqual(dijkstra(adj_list, start), expected_output)

    def test_dijkstra_large_graph(self):
        adj_list = [[(i + 1, i) for i in range(1000)], *[[(i + 2, i + 1) for i in range(999)], []]]
        start = 0
        expected_output = [0, *range(1000)]
        self.assertEqual(dijkstra(adj_list, start), expected_output)


if __name__ == '__main__':
    unittest.main()
