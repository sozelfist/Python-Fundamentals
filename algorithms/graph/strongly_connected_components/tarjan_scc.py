import unittest
from collections import deque


def create_graph(num_vertices, edges):
    graph = [[] for _ in range(num_vertices)]
    for u, v in edges:
        graph[u].append(v)
    return graph


def strongly_connected_components(graph):
    num_vertices = len(graph)
    stack = deque()
    on_stack = [False] * num_vertices
    indices = [-1] * num_vertices
    low_links = indices[:]
    index = 0
    components = []

    def tarjan_dfs(v):
        nonlocal index
        indices[v] = index
        low_links[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                tarjan_dfs(w)
                low_links[v] = min(low_links[v], low_links[w])
            elif on_stack[w]:
                low_links[v] = min(low_links[v], indices[w])

        if low_links[v] == indices[v]:
            component = []
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            while w != v:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
            components.append(component)

    for v in range(num_vertices):
        if indices[v] == -1:
            tarjan_dfs(v)

    return components


class TestTarjan(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(strongly_connected_components([]), [])

    def test_graph_with_single_node(self):
        self.assertEqual(strongly_connected_components([[]]), [[0]])

    def test_strongly_connected_components_of_size_1(self):
        g = create_graph(5, [(0, 1), (1, 2), (2, 0)])
        self.assertEqual(
            strongly_connected_components(g),
            [[2, 1, 0], [3], [4]]
        )

    def test_strongly_connected_components_of_size_2(self):
        g = create_graph(5, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 3)])
        self.assertEqual(strongly_connected_components(g), [[2, 1, 0], [4, 3]])

    def test_strongly_connected_components_of_size_3(self):
        g = create_graph(7, [(0, 1), (1, 2), (2, 0), (3, 4),
                         (4, 3), (3, 5), (5, 6), (6, 3)])
        self.assertEqual(strongly_connected_components(g),
                         [[2, 1, 0], [6, 5, 4, 3]])


if __name__ == '__main__':
    unittest.main()
