import unittest
from collections import defaultdict
from typing import Any


def count_walks_with_k_edges(
    graph: dict[int, list[int]], src: int, dest: int, k: int
) -> tuple[list, Any]:
    # Create a memoization table to store intermediate results
    memo = defaultdict(dict)

    def dfs(u, v, e):
        # Base case: if source and destination are same, and k is 0, return 1
        if u == v and e == 0:
            return 1

        # If k becomes 0, we can't move further, so return 0
        if e == 0:
            return 0

        # If the result is already computed, return it
        if e in memo[u] and v in memo[u][e]:
            return memo[u][e][v]

        # Initialize the count of walks to 0
        count = 0

        # Iterate over all adjacent vertices of u
        for nei in graph[u]:
            # Recursively count walks with k-1 edges from nei to v
            count += dfs(nei, v, e - 1)

        # Store the result in the memoization table and return the count
        memo[u][e] = {v: count}
        return count

    # Call the DFS function to count walks from src to dest with k edges
    count = dfs(src, dest, k)

    # Initialize a list to store the walks
    walks = []

    def find_walks(u, v, e, path):
        # Base case: if source and destination are same, and k is 0,
        # add the path to walks
        if u == v and e == 0:
            walks.append(path)
            return

        # If k becomes 0, we can't move further, so return
        if e == 0:
            return

        # Iterate over all adjacent vertices of u
        for nei in graph[u]:
            # Recursively find walks with k-1 edges from nei to v
            find_walks(nei, v, e - 1, path + [nei])

    # Call the DFS function to find the walks from src to dest with k edges
    find_walks(src, dest, k, [src])

    return walks, count


class TestCountWalksWithKEdges(unittest.TestCase):
    def test_count_walks_with_k_edges_example_graph(self):
        graph = {0: [1, 2], 1: [2], 2: [3], 3: [4], 4: [1]}
        src = 0
        dest = 3
        k = 3
        walks, count = count_walks_with_k_edges(graph, src, dest, k)
        expected_walks = [[0, 1, 2, 3]]
        expected_count = 1
        self.assertEqual(walks, expected_walks)
        self.assertEqual(count, expected_count)

    def test_count_walks_with_k_edges_no_walks(self):
        graph = {0: [1, 2], 1: [2], 2: [3], 3: [4], 4: [1]}
        src = 0
        dest = 3
        k = 5
        walks, count = count_walks_with_k_edges(graph, src, dest, k)
        expected_walks = []
        expected_count = 0
        self.assertEqual(walks, expected_walks)
        self.assertEqual(count, expected_count)

    def test_count_walks_with_k_edges_multiple_walks(self):
        graph = {0: [1, 2], 1: [2], 2: [3, 4], 3: [4], 4: []}
        src = 0
        dest = 4
        k = 2
        walks, count = count_walks_with_k_edges(graph, src, dest, k)
        expected_walks = [[0, 2, 4]]
        expected_count = 1
        self.assertEqual(walks, expected_walks)
        self.assertEqual(count, expected_count)

    def test_count_walks_with_k_edges_self_loop(self):
        graph = {0: [1, 2], 1: [2], 2: [3, 4], 3: [4], 4: [4]}
        src = 0
        dest = 4
        k = 2
        walks, count = count_walks_with_k_edges(graph, src, dest, k)
        expected_walks = [[0, 2, 4]]
        expected_count = 1
        self.assertEqual(walks, expected_walks)
        self.assertEqual(count, expected_count)


if __name__ == "__main__":
    unittest.main()
