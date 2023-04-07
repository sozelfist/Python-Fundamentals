import unittest


def kosaraju(graph: list[list[int]]) -> list[list[int]]:
    def dfs_first_pass(node: int, visited: list[bool], stack: list[int]) -> None:
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_first_pass(neighbor, visited, stack)
        stack.append(node)

    def dfs_second_pass(node: int, visited: list[bool], component: list[int]) -> None:
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_second_pass(neighbor, visited, component)

    n = len(graph)
    visited = [False for _ in range(n)]
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs_first_pass(i, visited, stack)

    reversed_graph = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            reversed_graph[j].append(i)

    visited = [False for _ in range(n)]
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_second_pass(node, visited, component)
            result.append(component)

    return result


class TestKosaraju(unittest.TestCase):
    def test_kosaraju(self):
        graph = [
            [1],
            [2],
            [0, 3],
            [2]
        ]
        expected = [[0, 1, 2, 3]]
        result = kosaraju(graph)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
