import unittest

Tree = dict[int, set[int]]


def prufer_code(tree: Tree) -> list[int]:
    """
    Returns the Prufer code for a given tree represented as an adjacency list.
    """
    n = len(tree)
    degree = [len(tree[i]) for i in range(n)]
    code = []

    for _ in range(n - 2):
        # Find the smallest leaf node
        leaf = min(i for i in range(n) if degree[i] == 1)

        # Find its parent
        parent = next(iter(tree[leaf]))

        # Add parent's label to the code
        code.append(parent)

        # Remove the leaf node and decrement the degrees of its neighbors
        degree[parent] -= 1
        degree[leaf] -= 1
        tree[parent].remove(leaf)

    return code


class TestPruferCode(unittest.TestCase):
    def test_single_node(self):
        tree = {0: set()}
        code = prufer_code(tree)
        self.assertEqual(code, [])

    def test_two_nodes(self):
        tree = {0: {1}, 1: {0}}
        code = prufer_code(tree)
        self.assertEqual(code, [])

    def test_three_nodes(self):
        tree = {0: {1, 2}, 1: {0}, 2: {0}}
        code = prufer_code(tree)
        self.assertEqual(code, [0])

    def test_four_nodes(self):
        tree = {0: {1, 2}, 1: {0, 3}, 2: {0, 4}, 3: {1}, 4: {2}}
        code = prufer_code(tree)
        self.assertEqual(code, [1, 0, 2])

    def test_five_nodes(self):
        tree = {0: {1, 2}, 1: {0, 3}, 2: {0, 4}, 3: {1}, 4: {2, 5}, 5: {4}}
        code = prufer_code(tree)
        self.assertEqual(code, [1, 0, 2, 4])

    def test_six_nodes(self):
        tree = {0: {3}, 1: {3}, 2: {3}, 3: {0, 1, 2, 4}, 4: {3, 5}, 5: {4}}
        code = prufer_code(tree)
        self.assertEqual(code, [3, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()
