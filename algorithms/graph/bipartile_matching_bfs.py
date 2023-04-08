import unittest
from collections import deque


def is_bipartite(graph: dict[int, list[int]]):
    num_vertices = len(graph)
    vertex_colors = [-1] * num_vertices
    bfs_queue = deque()

    for start_vertex in range(num_vertices):
        if vertex_colors[start_vertex] == -1:
            bfs_queue.append(start_vertex)
            vertex_colors[start_vertex] = 1

            while bfs_queue:
                curr_vertex = bfs_queue.popleft()

                for neighbor_vertex in graph[curr_vertex]:
                    if vertex_colors[neighbor_vertex] == -1:
                        vertex_colors[neighbor_vertex] = 1 - \
                            vertex_colors[curr_vertex]
                        bfs_queue.append(neighbor_vertex)
                    elif vertex_colors[neighbor_vertex] \
                            == vertex_colors[curr_vertex]:
                        return False

    return True


def find_bipartite_matching(graph: dict[int, list[int]]):
    if not is_bipartite(graph):
        return None

    num_vertices = len(graph)
    vertex_colors = [-1] * num_vertices
    bfs_queue = deque()
    matching = {}

    for start_vertex in range(num_vertices):
        if vertex_colors[start_vertex] == -1:
            bfs_queue.append(start_vertex)
            vertex_colors[start_vertex] = 1

            while bfs_queue:
                curr_vertex = bfs_queue.popleft()

                for neighbor_vertex in graph[curr_vertex]:
                    if vertex_colors[neighbor_vertex] == -1:
                        vertex_colors[neighbor_vertex] = 1 - \
                            vertex_colors[curr_vertex]
                        bfs_queue.append(neighbor_vertex)
                        matching[neighbor_vertex] = curr_vertex
                    elif vertex_colors[neighbor_vertex] \
                            == vertex_colors[curr_vertex]:
                        continue

    return [(v, u) for v, u in matching.items()]


class TestBipartiteMatching(unittest.TestCase):
    def test_bipartite_graph(self):
        bipartite_graph = {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
        self.assertTrue(is_bipartite(bipartite_graph))

    def test_non_bipartile_graph(self):
        non_bipartite_graph = {
            0: [1, 2, 3],
            1: [0, 2],
            2: [1, 0, 3],
            3: [0, 2]
        }
        self.assertFalse(is_bipartite(non_bipartite_graph))

    def test_find_bipartite_matching(self):
        bipartite_graph = {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
        matching = find_bipartite_matching(bipartite_graph)
        self.assertEqual(matching, [(1, 0), (3, 0), (2, 1)])

    def test_find_non_bipartite_graph(self):
        non_bipartite_graph = {
            0: [1, 2, 3],
            1: [0, 2],
            2: [1, 0, 3],
            3: [0, 2]
        }
        matching = find_bipartite_matching(non_bipartite_graph)
        self.assertIsNone(matching)


if __name__ == '__main__':
    unittest.main()
