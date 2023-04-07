import unittest


def binary_lifting(adj_list: list[list[int]], root: int) -> tuple[list[list[int]], list[int]]:
    num_nodes = len(adj_list)
    log_num_nodes = (num_nodes - 1).bit_length()

    parents = [-1] * num_nodes
    depths = [-1] * num_nodes
    depths[root] = 0
    stack = [(root, -1)]
    while stack:
        node, parent = stack.pop()
        parents[node] = parent
        for neighbor in adj_list[node]:
            if neighbor != parent:
                depths[neighbor] = depths[node] + 1
                stack.append((neighbor, node))

    ancestors = [[-1] * num_nodes for _ in range(log_num_nodes)]
    ancestors[0] = parents
    for i in range(1, log_num_nodes):
        for node in range(num_nodes):
            ancestor = ancestors[i - 1][node]
            if ancestor != -1:
                ancestor = ancestors[i - 1][ancestor]
            ancestors[i][node] = ancestor

    return ancestors, depths


def find_kth_ancestor(node: int, k: int, ancestors: list[list[int]]) -> int:
    log_num_nodes = len(ancestors)
    for i in range(log_num_nodes):
        if k & (1 << i):
            node = ancestors[i][node]
            if node == -1:
                break
    return node


class TestBinaryLifting(unittest.TestCase):
    def setUp(self):
        self.adj = [[1, 2], [3, 4], [], [5, 6], [], [], []]
        self.root = 0
        self.ancestors, self.depths = binary_lifting(self.adj, self.root)

    def test_binary_lifting_on_tree(self):
        expected_ancestors = [
            [-1, 0, 0, 1, 1, 3, 3],
            [-1, -1, -1, 0, 0, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1]
        ]
        self.assertEqual(self.ancestors, expected_ancestors)

        expected_depths = [0, 1, 1, 2, 2, 3, 3]
        self.assertEqual(self.depths, expected_depths)

    def test_find_kth_ancestor_on_tree(self):
        # Find the 2nd ancestor of node 3
        node = 3
        k = 2
        ancestor = find_kth_ancestor(node, k, self.ancestors)
        self.assertEqual(ancestor, 0)

        # Find the LCA of nodes 2 and 4
        node1 = 2
        node2 = 4
        depth1 = self.depths[node1]
        depth2 = self.depths[node2]
        if depth1 > depth2:
            node1, node2 = node2, node1
            depth1, depth2 = depth2, depth1
        delta = depth2 - depth1
        for i in range(len(self.ancestors)):
            if delta & (1 << i):
                node2 = self.ancestors[i][node2]
        if node1 == node2:
            lca = node1
        else:
            for i in range(len(self.ancestors) - 1, -1, -1):
                if self.ancestors[i][node1] != self.ancestors[i][node2]:
                    node1 = self.ancestors[i][node1]
                    node2 = self.ancestors[i][node2]
            lca = self.ancestors[0][node1]
        self.assertEqual(lca, 0)


if __name__ == '__main__':
    unittest.main()
