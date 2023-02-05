from typing import List, Tuple
import unittest


def boruvka(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    mst = []
    rep = [i for i in range(n)]
    weight = [float('inf')] * n

    while len(mst) < n - 1:
        connected_components = n
        for i in range(n):
            rep[i] = i

        for u, v, w in edges:
            ru, rv = rep[u], rep[v]

            if ru != rv:
                if w < min(weight[ru], weight[rv]):
                    if weight[ru] < weight[rv]:
                        weight[rv] = w
                        mst.append((u, v))
                        rep = [rv if r == ru else r for r in rep]
                        connected_components -= 1
                    else:
                        weight[ru] = w
                        mst.append((u, v))
                        rep = [ru if r == rv else r for r in rep]
                        connected_components -= 1

        if connected_components == n:
            break

    return mst


class TestBoruvka(unittest.TestCase):
    def test_boruvka_empty_graph(self):
        n = 0
        edges = []
        result = boruvka(n, edges)
        self.assertEqual(result, [])

    def test_boruvka_complete_graph(self):
        n = 4
        edges = [(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 2, 4), (1, 3, 5), (2, 3, 6)]
        result = boruvka(n, edges)
        self.assertEqual(len(result), n - 1)

    def test_boruvka_disconnected_graph(self):
        n = 4
        edges = [(0, 1, 1), (2, 3, 2)]
        result = boruvka(n, edges)
        self.assertEqual(result, [(0, 1), (2, 3)])


if __name__ == '__main__':
    unittest.main()
