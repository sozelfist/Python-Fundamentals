import unittest


def bron_kerbosch(graph: dict[int, list[int]]) -> list[set[int]]:
    def recursive_bron_kerbosch(R: set[int], P: set[int], X: set[int]) -> list[set[int]]:
        """
        Find all maximal cliques in an undirected graph using the Bron-Kerbosch algorithm.

        Parameters:
            graph (dict[int, list[int]]): An adjacency list representation of the undirected graph,
                                        where keys are vertices, and values are lists containing
                                        adjacent vertices.

        Returns:
            list[set[int]]: A list of sets, each representing a maximal clique in the graph.
                            Each set contains vertex indices belonging to the respective clique.

        Example:
            graph = {
                1: [2, 3, 4],
                2: [1, 3],
                3: [1, 2, 4],
                4: [1, 3]
            }
            result = bron_kerbosch(graph)
            # Output: [set([1, 2, 3]), set([1, 3, 4])]

        Note:
            - The input graph should be an undirected graph represented as an adjacency list.
            - This implementation is suitable for small to medium-sized graphs.
            - For large graphs, additional optimizations may be required for improved performance.
        """
        # Base case: If both P and X are empty, R is a maximal clique
        if not P and not X:
            return [R]

        cliques = []
        for v in P.copy():
            neighbors = set(graph[v])
            recursive_cliques = recursive_bron_kerbosch(
                R | {v}, P & neighbors, X & neighbors)
            cliques.extend(recursive_cliques)
            P.remove(v)
            X.add(v)

        return cliques

    # Start the algorithm with empty R, all vertices as P, and an empty set X
    vertices = set(graph.keys())
    return recursive_bron_kerbosch(set(), vertices, set())


class TestBronKerbosch(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        result = bron_kerbosch(graph)
        self.assertEqual(result, [set()])

    def test_single_vertex(self):
        graph = {1: []}
        result = bron_kerbosch(graph)
        self.assertEqual(result, [{1}])

    def test_disconnected_vertices(self):
        graph = {
            1: [],
            2: [],
            3: [],
        }
        result = bron_kerbosch(graph)
        self.assertEqual(result, [{1}, {2}, {3}])

    def test_simple_graph(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 3],
            3: [1, 2, 4],
            4: [1, 3],
        }
        result = bron_kerbosch(graph)
        expected = [{1, 2, 3}, {1, 3, 4}]
        self.assertEqual(result, expected)

    def test_complex_graph(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2, 4],
            4: [3, 5],
            5: [4, 6],
            6: [5],
        }
        result = bron_kerbosch(graph)
        expected = [{1, 2, 3}, {3, 4}, {4, 5}, {5, 6}]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
