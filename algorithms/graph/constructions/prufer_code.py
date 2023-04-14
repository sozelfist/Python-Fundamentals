import unittest


def prufer_code(leaf_nodes: list[int]) -> list[tuple[int, int]]:
    """
    Generate the Prufer code for a tree given a list of leaf node indices.

    Args:
        leaf_nodes (List[int]): A list of indices representing the leaf
        nodes of the tree.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing the edges
        of the tree encoded using Prufer code.
    """
    leaf_nodes = list(leaf_nodes)
    vertices = set(range(len(leaf_nodes) + 2))
    edges = []
    while leaf_nodes:
        v = min(vertices - set(leaf_nodes))
        vertices.remove(v)
        u = leaf_nodes.pop(0)
        edges.append((u, v))
    edges.append(tuple(vertices))
    return edges


class TestPruferCode(unittest.TestCase):
    def test_small_tree(self):
        leaf_nodes = [3, 4]
        expected_edges = [(3, 0), (4, 1), (2, 3)]
        self.assertEqual(prufer_code(leaf_nodes), expected_edges)

    def test_medium_tree(self):
        leaf_nodes = [3, 1, 0, 0, 3, 2, 9, 9, 2, 3]
        expected_edges = [(3, 4), (1, 5), (0, 1), (0, 6), (3, 0),
                          (2, 7), (9, 8), (9, 10), (2, 9), (3, 2), (3, 11)]
        self.assertEqual(prufer_code(leaf_nodes), expected_edges)

    def test_empty_input(self):
        leaf_nodes = []
        expected_edges = [(0, 1)]
        self.assertEqual(prufer_code(leaf_nodes), expected_edges)

    def test_duplicate_nodes(self):
        leaf_nodes = [1, 1, 2, 3, 3, 3]
        expected_edges = [(1, 0), (1, 4), (2, 1), (3, 2),
                          (3, 5), (3, 6), (3, 7)]
        self.assertEqual(prufer_code(leaf_nodes), expected_edges)


if __name__ == '__main__':
    unittest.main()
