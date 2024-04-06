import unittest


class DAG:
    def __init__(self, v):
        """Initialize DAG with v vertices."""
        self.v = v
        self.adj = [[] for i in range(v)]
        self.indegree = [0 for i in range(v)]

    def add_edge(self, v, w):
        """Utility function to add edge"""
        self.adj[v].append(w)
        self.indegree[w] += 1

    def topological_sort(self):
        """Perform topological sort on the DAG."""
        topological = []
        q = []

        for i in range(self.v):
            if self.indegree[i] == 0:
                q.append(i)

        while len(q) != 0:
            t = q[0]
            q.pop(0)

            topological.append(t)

            for j in self.adj[t]:
                self.indegree[j] -= 1

                if self.indegree[j] == 0:
                    q.append(j)

        return topological

    def maximum_edge_addition(self):
        """Returns a list of edges that can be added without
        creating any cycle."""
        visited = [False for i in range(self.v)]
        topo = self.topological_sort()
        edges = []

        for i in range(len(topo)):
            t = topo[i]

            for j in self.adj[t]:
                visited[j] = True

            for j in range(i + 1, len(topo)):
                if not visited[topo[j]]:
                    edges.append((t, topo[j]))

                visited[topo[j]] = False

        return edges, len(edges)


class TestDAG(unittest.TestCase):
    def test_on_DAG_with_no_edges(self):
        g1 = DAG(3)
        g1.add_edge(0, 1)
        g1.add_edge(1, 2)
        g1.add_edge(0, 2)
        edges1, num_edges1 = g1.maximum_edge_addition()
        self.assertEqual(edges1, [])
        self.assertEqual(num_edges1, 0)

    def test_on_DAG_with_one_edge(self):
        g2 = DAG(4)
        g2.add_edge(0, 1)
        edges2, num_edges2 = g2.maximum_edge_addition()
        self.assertEqual(edges2, [(0, 2), (0, 3), (2, 3), (2, 1), (3, 1)])
        self.assertEqual(num_edges2, 5)

    def test_on_DAG_with_multiple_edges(self):
        g3 = DAG(6)
        g3.add_edge(5, 2)
        g3.add_edge(5, 0)
        g3.add_edge(4, 0)
        g3.add_edge(4, 1)
        g3.add_edge(2, 3)
        g3.add_edge(3, 1)
        edges3, num_edges3 = g3.maximum_edge_addition()
        self.assertEqual(
            edges3,
            [(4, 5), (4, 2), (4, 3), (5, 3), (5, 1), (2, 0), (2, 1), (0, 3), (0, 1)],
        )
        self.assertEqual(num_edges3, 9)


if __name__ == "__main__":
    unittest.main()
