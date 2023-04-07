import unittest


def hamilton_cycle(graph: list[list[int]], start: int) -> list[int] | None:
    def backtrack(curr_node: int, visited: list[bool], path: list[int]) -> list[int] | None:
        # If all vertices have been visited and the last vertex is adjacent to the start vertex,
        # return the path with the start vertex appended to form a cycle
        if len(path) == len(graph) and graph[curr_node][start] == 1:
            return path + [start]

        for next_node in range(len(graph)):
            if graph[curr_node][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                path.append(next_node)
                res = backtrack(next_node, visited, path)
                if res is not None:
                    return res
                visited[next_node] = False
                path.pop()

        return None

    visited = [False] * len(graph)
    visited[start] = True
    path = [start]
    return backtrack(start, visited, path)


class TestHamiltonCycle(unittest.TestCase):
    def test_cycle_exists(self):
        graph = [[0, 1, 1, 0, 0],
                 [1, 0, 1, 1, 0],
                 [1, 1, 0, 1, 1],
                 [0, 1, 1, 0, 1],
                 [0, 0, 1, 1, 0]]
        cycle = hamilton_cycle(graph, 0)
        self.assertEqual(cycle, [0, 1, 3, 4, 2, 0])

    def test_cycle_does_not_exist(self):
        graph = [[0, 1, 1, 0, 0],
                 [1, 0, 1, 1, 0],
                 [1, 1, 0, 1, 1],
                 [0, 1, 1, 0, 0],
                 [0, 0, 1, 0, 0]]
        cycle = hamilton_cycle(graph, 0)
        self.assertIsNone(cycle)

    def test_single_vertex(self):
        graph = [[1]]
        cycle = hamilton_cycle(graph, 0)
        self.assertEqual(cycle, [0, 0])

    def test_two_vertices_cycle(self):
        graph = [[0, 1], [1, 0]]
        cycle = hamilton_cycle(graph, 1)
        self.assertEqual(cycle, [1, 0, 1])


if __name__ == '__main__':
    unittest.main()
