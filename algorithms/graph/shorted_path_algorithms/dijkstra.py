import heapq
import unittest


def dijkstra(adj_list: list[list[tuple[int, int]]], start: int) -> list[int]:
    n = len(adj_list)
    dist = [float("inf")] * n
    dist[start] = 0
    visited = [False] * n
    queue = [(0, start)]
    while queue:
        (curr_dist, curr) = heapq.heappop(queue)
        if visited[curr]:
            continue
        visited[curr] = True
        for neighbor, weight in adj_list[curr]:
            if neighbor >= n:
                continue
            if dist[curr] + weight < dist[neighbor]:
                dist[neighbor] = dist[curr] + weight
                heapq.heappush(queue, (dist[neighbor], neighbor))
    return dist


class TestDijkstra(unittest.TestCase):
    def test_dijkstra_simple(self):
        adj_list = [[(1, 2), (2, 3)], [(2, 1)], []]
        result = dijkstra(adj_list, 0)
        expected = [0, 2, 3]
        self.assertEqual(result, expected)

    def test_dijkstra_disconnected(self):
        adj_list = [[(1, 2)], [(2, 1)], [], [], []]
        result = dijkstra(adj_list, 0)
        expected = [0, 2, 3, float("inf"), float("inf")]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
