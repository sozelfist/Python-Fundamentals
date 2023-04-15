import heapq
import unittest

Graph = dict[str, dict[str, int]]


def bidirectional_dijkstra(graph: Graph, start: str, end: str):
    # Initialize the forward and backward search
    forward_dist = {start: 0}
    backward_dist = {end: 0}
    forward_prev = {}
    backward_prev = {}
    forward_heap = [(0, start)]
    backward_heap = [(0, end)]
    visited_forward = set()
    visited_backward = set()

    # While there are still vertices to explore in either direction
    while forward_heap and backward_heap:
        # Explore a vertex in the forward direction
        _, curr_forward = heapq.heappop(forward_heap)
        visited_forward.add(curr_forward)
        for neighbor, weight in graph[curr_forward].items():
            if neighbor not in visited_forward:
                new_dist = forward_dist[curr_forward] + weight
                if neighbor not in forward_dist or new_dist \
                        < forward_dist[neighbor]:
                    forward_dist[neighbor] = new_dist
                    forward_prev[neighbor] = curr_forward
                    heapq.heappush(forward_heap, (new_dist, neighbor))

        # Explore a vertex in the backward direction
        _, curr_backward = heapq.heappop(backward_heap)
        visited_backward.add(curr_backward)
        for neighbor, weight in graph[curr_backward].items():
            if neighbor not in visited_backward:
                new_dist = backward_dist[curr_backward] + weight
                if neighbor not in backward_dist \
                        or new_dist < backward_dist[neighbor]:
                    backward_dist[neighbor] = new_dist
                    backward_prev[neighbor] = curr_backward
                    heapq.heappush(backward_heap, (new_dist, neighbor))

        # Check if we have found a shortest path
        intersect = visited_forward.intersection(visited_backward)
        if intersect:
            shortest = None
            midpoint = None
            for vertex in intersect:
                dist = forward_dist[vertex] + backward_dist[vertex]
                if shortest is None or dist < shortest:
                    shortest = dist
                    midpoint = vertex

            # Build the path from start to midpoint and from end to midpoint
            path = [midpoint]
            curr = midpoint
            while curr != start:
                curr = forward_prev[curr]
                path.append(curr)
            path.reverse()
            curr = midpoint
            while curr != end:
                curr = backward_prev[curr]
                path.append(curr)

            return shortest, path

    # If no path was found, return None
    return None, None


class TestBidirectionalDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1, 'D': 5},
            'C': {'A': 2, 'B': 1, 'D': 8},
            'D': {'B': 5, 'C': 8, 'E': 6},
            'E': {'D': 6}
        }

    def test_shortest_distance(self):
        distance, _ = bidirectional_dijkstra(self.graph, 'A', 'E')
        self.assertEqual(distance, 14)

    def test_path(self):
        _, path = bidirectional_dijkstra(self.graph, 'A', 'E')
        self.assertEqual(path, ['A', 'C', 'B', 'D', 'E'])

    def test_distinct_vertices(self):
        _, path = bidirectional_dijkstra(self.graph, 'A', 'E')
        distinct_vertices = set(path)
        self.assertEqual(distinct_vertices, {'A', 'C', 'B', 'D', 'E'})


if __name__ == '__main__':
    unittest.main()
