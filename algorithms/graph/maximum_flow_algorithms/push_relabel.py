"""
    The Relabel-to-Front algorithm is an efficient algorithm for solving the maximum
    flow problem in a flow network. The algorithm maintains a list of active nodes and
    repeatedly pushes flow from active nodes to their neighbors until no more flow can
    be pushed. If a node has excess flow that it cannot push to any neighbor, it is
    relabeled to a new height to allow it to push flow again in the future.

    The algorithm uses a height labeling scheme to determine the order in which nodes
    are processed. Each node is assigned a height, which represents the distance from
    the node to the sink node in the residual graph. Nodes are processed in order of
    decreasing height, and each node is processed repeatedly until it has no more excess
    flow to push.

    This implementation uses a matrix to represent the flow and capacity, and assumes
    that the flow network is represented as an adjacency matrix. The matrix C represents
    the capacity of the edges, and the function returns the maximum flow from the source
    node to the sink node.
"""

import unittest


def relabel_to_front(C, source: int, sink: int) -> int:
    """
    Finds the maximum flow in a directed graph using the Relabel-to-Front algorithm.

    Args:
        C (List[List[int]]): The capacity matrix of the graph. C[u][v] is the capacity of the edge (u, v).
        source (int): The source node of the graph.
        sink (int): The sink node of the graph.

    Returns:
        int: The maximum flow in the graph from the source to the sink.

    """
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for _ in range(n)]
    # residual capacity from u to v is C[u][v] - F[u][v]

    height = [0] * n  # height of node
    excess = [0] * n  # flow into node minus flow from node
    seen = [0] * n  # neighbours seen since last relabel
    # node "queue"
    nodelist = [i for i in range(n) if i != source and i != sink]

    def push(u, v):
        """Pushes flow from node u to node v."""
        send = min(excess[u], C[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        """Relabels the height of node u to the smallest height that would allow a push from u to its neighbours."""
        min_height = float("inf")
        for v in range(n):
            if C[u][v] - F[u][v] > 0:
                min_height = min(min_height, height[v])
        height[u] = min_height + 1  # type: ignore

    def discharge(u):
        """Discharges the excess flow at node u to its neighbours."""
        while excess[u] > 0:
            if seen[u] < n:  # check next neighbour
                v = seen[u]
                if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:  # we have checked all neighbours. must relabel
                relabel(u)
                seen[u] = 0

    height[source] = n  # longest path from source to sink is less than n long
    excess[source] = float("inf")  # type: ignore # send as much flow as possible to neighbours of source
    for v in range(n):
        push(source, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))  # move to front of list
            p = 0  # start from front of list
        else:
            p += 1

    return sum(F[source])


class TestMaxFlow(unittest.TestCase):

    def test_small_network(self):
        C = [[0, 3, 4],
             [0, 0, 1],
             [0, 0, 0]]
        source = 0
        sink = 2
        self.assertEqual(relabel_to_front(C, source, sink), 5)

    def test_disconnected_network(self):
        C = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        source = 0
        sink = 2
        self.assertEqual(relabel_to_front(C, source, sink), 0)

    def test_medium_network(self):
        C = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]
        source = 0
        sink = 5
        self.assertEqual(relabel_to_front(C, source, sink), 23)


if __name__ == '__main__':
    unittest.main()
