import unittest
from collections import defaultdict

MAX_NODES = 1025

tree: defaultdict[int, list[int]] = defaultdict(list)
centroid_tree: defaultdict[int, list[int]] = defaultdict(list)
centroid_marked: list[bool] = [False] * MAX_NODES


def add_edge(u: int, v: int) -> None:
    """Add edge between two nodes of the undirected tree."""
    tree[u].append(v)
    tree[v].append(u)


def dfs(
    src: int, visited: list[bool], subtree_size: list[int],
    num_nodes: list[int]
) -> None:
    """Setup subtree sizes and nodes in current tree."""
    visited[src] = True
    num_nodes[0] += 1
    subtree_size[src] = 1
    for neighbor in tree[src]:
        if not visited[neighbor] and not centroid_marked[neighbor]:
            dfs(neighbor, visited, subtree_size, num_nodes)
            subtree_size[src] += subtree_size[neighbor]


def get_centroid(
    src: int, visited: list[bool], subtree_size: list[int],
    num_nodes: int
) -> int:
    """Get the centroid of tree rooted at src."""
    is_centroid = True
    visited[src] = True
    heaviest_child = 0
    for neighbor in tree[src]:
        if not visited[neighbor] and not centroid_marked[neighbor]:
            if subtree_size[neighbor] > num_nodes / 2:
                is_centroid = False
            if heaviest_child == 0 or \
                    subtree_size[neighbor] > subtree_size[heaviest_child]:
                heaviest_child = neighbor
    if is_centroid and num_nodes - subtree_size[src] <= num_nodes / 2:
        return src
    return get_centroid(heaviest_child, visited, subtree_size, num_nodes)


def get_centroid_tree(src: int) -> int:
    """Get the centroid of tree rooted at src."""
    visited = [False] * MAX_NODES
    subtree_size = [0] * MAX_NODES
    num_nodes = [0]
    dfs(src, visited, subtree_size, num_nodes)
    visited = [False] * MAX_NODES
    centroid = get_centroid(src, visited, subtree_size, num_nodes[0])
    centroid_marked[centroid] = True
    return centroid


def decompose_tree(root: int) -> list[int]:
    """Function to generate centroid tree of tree rooted at src."""
    centroid_list = []
    cend_tree = get_centroid_tree(root)
    centroid_list.append(cend_tree)
    for it in tree[cend_tree]:
        if not centroid_marked[it]:
            centroid_list.extend(decompose_tree(it))
    return centroid_list


class TestCentroidDecomposition(unittest.TestCase):

    def setUp(self):
        add_edge(1, 4)
        add_edge(2, 4)
        add_edge(3, 4)
        add_edge(4, 5)
        add_edge(5, 6)
        add_edge(6, 7)
        add_edge(7, 8)
        add_edge(7, 9)
        add_edge(6, 10)
        add_edge(10, 11)
        add_edge(11, 12)
        add_edge(11, 13)
        add_edge(12, 14)
        add_edge(13, 15)
        add_edge(13, 16)

    def test_add_edge(self):
        add_edge(4, 7)
        self.assertEqual(tree[4], [1, 2, 3, 5, 7])
        self.assertEqual(tree[7], [6, 8, 9, 4])

    def test_decompose_tree(self):
        result = decompose_tree(1)
        self.assertEqual(
            result, [6, 4, 1, 2, 3, 5, 7, 8, 9, 11, 10, 12, 14, 13, 15, 16]
        )

    def test_get_centroid_tree(self):
        result = get_centroid_tree(1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
