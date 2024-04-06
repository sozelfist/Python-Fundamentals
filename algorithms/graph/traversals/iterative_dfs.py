import unittest


class Graph:
    def __init__(self, vertices: int):
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int) -> None:
        self.adj_list[u].append(v)

    def idfs(self, start: int, target: int, max_depth: int) -> list[int] | None:
        if (
            start < 0
            or start >= len(self.adj_list)
            or target < 0
            or target >= len(self.adj_list)
        ):
            return None

        visited = [False] * len(self.adj_list)
        return self._idfs(start, target, max_depth, visited)

    def _idfs(
        self,
        node: int,
        target: int,
        max_depth: int,
        visited: list[bool],
        depth: int = 0,
    ) -> list[int] | None:
        if node == target:
            return [node]

        if depth == max_depth:
            return None

        visited[node] = True
        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:
                path = self._idfs(neighbor, target, max_depth, visited, depth + 1)
                if path is not None:
                    return [node] + path

        return None


class TestIDFS(unittest.TestCase):
    def test_idfs_path_exists(self):
        # Test case where a path exists within the max depth limit
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 5)

        start_node = 0
        target_node = 4
        max_depth_limit = 3

        result = g.idfs(start_node, target_node, max_depth_limit)

        expected_path = [0, 1, 4]  # Expected path from 0 to 4: [0, 1, 4]
        self.assertEqual(result, expected_path)

    def test_idfs_path_not_exists(self):
        # Test case where no path exists within the max depth limit
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)

        start_node = 0
        target_node = 3
        max_depth_limit = 1

        result = g.idfs(start_node, target_node, max_depth_limit)

        self.assertIsNone(result)  # Expected result is None

    def test_idfs_start_node_equals_target_node(self):
        # Test case where start node equals target node
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)

        start_node = 1
        target_node = 1
        max_depth_limit = 2

        result = g.idfs(start_node, target_node, max_depth_limit)

        expected_path = [1]  # Expected path from 1 to 1: [1]
        self.assertEqual(result, expected_path)

    def test_idfs_invalid_start_node(self):
        # Test case where an invalid start node is given
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)

        start_node = 5
        target_node = 3
        max_depth_limit = 2

        result = g.idfs(start_node, target_node, max_depth_limit)

        self.assertIsNone(result)  # Expected result is None

    def test_idfs_invalid_target_node(self):
        # Test case where an invalid target node is given
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)

        start_node = 0
        target_node = 5
        max_depth_limit = 2

        result = g.idfs(start_node, target_node, max_depth_limit)

        self.assertIsNone(result)  # Expected result is None


if __name__ == "__main__":
    unittest.main()
