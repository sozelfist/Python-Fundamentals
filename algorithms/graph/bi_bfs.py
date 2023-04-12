import unittest


def bidirectional_bfs(
    graph: dict[int, list[int]], source: int, target: int
) -> list[int] | None:
    """
    Bidirectional Breadth-First Search (BiBFS) algorithm to find the shortest
    path between source and target nodes
    in an undirected graph represented as an adjacency list.

    Args:
        graph (Dict[int, List[int]]): The graph represented as an adjacency
        list where keys are node identifiers
        and values are lists of neighboring node identifiers.
        source (int): The source node.
        target (int): The target node.

    Returns:
        Optional[List[int]]: The shortest path from source to target if found,
        or None if no path exists.
    """

    # Create two frontiers, one from source and one from target
    source_frontier = [source]
    target_frontier = [target]

    # Create two sets to keep track of visited nodes in both frontiers
    source_visited: set[int] = {source}
    target_visited: set[int] = {target}

    # Create two dictionaries to store parent nodes
    # for each visited node in both frontiers
    source_parent: dict[int, int | None] = {source: None}
    target_parent: dict[int, int | None] = {target: None}

    # Bidirectional BFS loop
    while source_frontier and target_frontier:
        # Explore neighbors of nodes in the source frontier
        next_source_frontier: list[int] = []
        for node in source_frontier:
            for neighbor in graph[node]:
                if neighbor not in source_visited:
                    source_visited.add(neighbor)
                    source_parent[neighbor] = node
                    next_source_frontier.append(neighbor)

                    # If the neighbor is already visited by target frontier,
                    # we have found a common node
                    if neighbor in target_visited:
                        # Construct the shortest path by combining partial
                        # paths from source and target
                        path = _construct_path(
                            source_parent, target_parent, neighbor)
                        return path

        source_frontier = next_source_frontier

        # Explore neighbors of nodes in the target frontier
        next_target_frontier: list[int] = []
        for node in target_frontier:
            for neighbor in graph[node]:
                if neighbor not in target_visited:
                    target_visited.add(neighbor)
                    target_parent[neighbor] = node
                    next_target_frontier.append(neighbor)

                    # If the neighbor is already visited by source frontier,
                    # we have found a common node
                    if neighbor in source_visited:
                        # Construct the shortest path by combining partial
                        # paths from source and target
                        path = _construct_path(
                            source_parent, target_parent, neighbor)
                        return path

        target_frontier = next_target_frontier

    # No path found
    return None


def _construct_path(
        source_parent: dict[int, int | None],
        target_parent: dict[int, int | None], common_node: int
) -> list[int]:
    """
    Helper function to construct the shortest path
    from source to target by combining partial paths
    from source and target, given a common node.

    Args:
        source_parent (Dict[int, Optional[int]]): Dictionary of parent nodes
        for each visited node in the source frontier.
        target_parent (Dict[int, Optional[int]]): Dictionary of parent nodes
        for each visited node in the target frontier.
        common_node (int): The common node where the source and target
        frontiers intersect.

    Returns:
        List[int]: The shortest path from source to target
    """
    # Construct the shortest path by combining partial
    # paths from source and target
    source_path: list[int] = []
    node = common_node
    while node is not None:
        source_path.append(node)
        node = source_parent[node]
    source_path.reverse()  # Reverse the path to get correct order

    target_path: list[int] = []
    node = common_node
    while node is not None:
        target_path.append(node)
        node = target_parent[node]

    # Combine source and target paths, excluding the common node
    path = source_path + target_path[1:]

    return path


class BidirectionalBFSTestCase(unittest.TestCase):
    def setUp(self):
        # Example graph represented as an adjacency list
        self.graph = {1: [2, 3],
                      2: [1, 4, 5],
                      3: [1, 6],
                      4: [2, 7],
                      5: [2, 8],
                      6: [3],
                      7: [4],
                      8: [5, 9],
                      9: [8]}

    def test_bidirectional_bfs_shortest_path(self):
        # Test case for finding shortest path
        source_node = 1
        target_node = 9
        expected_path = [1, 2, 5, 8, 9]
        shortest_path = bidirectional_bfs(self.graph, source_node, target_node)
        self.assertEqual(shortest_path, expected_path)

    def test_bidirectional_bfs_disconnected_graph(self):
        # Test case for disconnected graph
        graph = {1: [2],
                 2: [1],
                 3: [4],
                 4: [3]}
        source_node = 1
        target_node = 3
        expected_path = None
        shortest_path = bidirectional_bfs(graph, source_node, target_node)
        self.assertEqual(shortest_path, expected_path)


if __name__ == '__main__':
    unittest.main()
