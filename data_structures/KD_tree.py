import heapq
import unittest


class KDNode:
    def __init__(self, point: tuple[float, ...], left_child=None, right_child=None, axis=None):
        self.point = point
        self.left_child = left_child
        self.right_child = right_child
        self.axis = axis


class KDTree:
    def __init__(self, points: list[tuple[float, ...]]):
        def build_tree(points, depth):
            if not points:
                return None
            axis = depth % len(points[0])
            points.sort(key=lambda point: point[axis])
            median_idx = len(points) // 2
            return KDNode(
                points[median_idx],
                left_child=build_tree(points[:median_idx], depth + 1),
                right_child=build_tree(points[median_idx + 1:], depth + 1),
                axis=axis
            )
        self.root = build_tree(points, depth=0)

    def search_knn(self, query: tuple[float, ...], k: int) -> list[tuple[float, ...]]:
        def search_node(node, query, k, heap):
            if not node:
                return
            distance = sum((p - q)**2 for p, q in zip(node.point, query))
            if len(heap) < k:
                heap.append((-distance, node.point))
            else:
                heapq.heappushpop(heap, (-distance, node.point))
            if node.left_child and node.right_child:
                if query[node.axis] < node.point[node.axis]:
                    search_node(node.left_child, query, k, heap)
                    if node.point[node.axis] - query[node.axis] < -heap[0][0]:
                        search_node(node.right_child, query, k, heap)
                else:
                    search_node(node.right_child, query, k, heap)
                    if query[node.axis] - node.point[node.axis] < -heap[0][0]:
                        search_node(node.left_child, query, k, heap)
            elif node.left_child:
                search_node(node.left_child, query, k, heap)
            else:
                search_node(node.right_child, query, k, heap)
        heap = []
        search_node(self.root, query, k, heap)
        return [point for _, point in sorted(heap, reverse=True)]


class KDTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
        self.tree = KDTree(self.points)

    def test_search_knn_with_point_in_tree(self):
        query_point = (3, 5)
        expected_neighbors = [(5, 4), (4, 7)]
        actual_neighbors = self.tree.search_knn(query_point, k=2)
        self.assertEqual(actual_neighbors, expected_neighbors)

    def test_search_knn_with_point_not_in_tree(self):
        query_point = (1, 1)
        expected_neighbors = [(2, 3), (5, 4)]
        actual_neighbors = self.tree.search_knn(query_point, k=2)
        self.assertEqual(actual_neighbors, expected_neighbors)

    def test_search_knn_with_ties(self):
        query_point = (7, 3)
        expected_neighbors = [(7, 2), (9, 6)]
        actual_neighbors = self.tree.search_knn(query_point, k=2)
        self.assertEqual(actual_neighbors, expected_neighbors)


if __name__ == '__main__':
    unittest.main()
