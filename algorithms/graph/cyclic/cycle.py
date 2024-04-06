import unittest


def find_cycle(graph: dict[int, list[int]]) -> set[int] | None:
    """
    Given an undirected graph, returns a list of nodes that form a cycle in
    the graph, if one exists. Returns None if no cycle is found.
    """
    if not graph:
        return None

    visited = set()

    def dfs(node: int, parent: int | None) -> tuple[bool, list[int]] | None:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, node)
                if result is not None and result[0]:
                    return True, result[1] + [node]
            elif neighbor != parent:
                return True, [node, neighbor]
        return False, []

    for node in graph:
        if node not in visited:
            result = dfs(node, None)
            if result is not None and result[0]:
                # Reverse the list to get the correct order
                return set(result[1][::-1])
    return None


class TestFindCycle(unittest.TestCase):
    def test_cycle_exists(self):
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        expected_cycle = {0, 1, 2}
        self.assertEqual(find_cycle(graph), expected_cycle)

    def test_cycle_does_not_exist(self):
        graph = {1: [2], 2: [3], 3: [4], 4: [5], 5: []}
        self.assertIsNone(find_cycle(graph))

    def test_empty_graph(self):
        graph = {}
        self.assertIsNone(find_cycle(graph))


if __name__ == "__main__":
    unittest.main()
