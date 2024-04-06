import unittest


def is_safe(vertex, graph, colors, color):
    """
    Check if the given color is safe for the vertex.

    Parameters:
    - vertex (int): the index of the vertex to be colored
    - graph (List[List[int]]): the graph represented as a 2D matrix
    - colors (List[int]): a list of colors assigned to each vertex
    - color (int): the color to be assigned to the vertex

    Returns:
    - True if the color is safe, False otherwise
    """
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True


def m_coloring_util(vertex, m, graph, colors):
    """
    A recursive function to color the vertices of the graph.

    Parameters:
    - vertex (int): the index of the current vertex to be colored
    - m (int): the maximum number of colors allowed
    - graph (List[List[int]]): the graph represented as a 2D matrix
    - colors (List[int]): a list of colors assigned to each vertex

    Returns:
    - True if a valid coloring exists, False otherwise
    """
    # Base case: all vertices are colored
    if vertex == len(graph):
        return True

    # Try different colors for the current vertex
    for color in range(1, m + 1):
        if is_safe(vertex, graph, colors, color):
            colors[vertex] = color
            if m_coloring_util(vertex + 1, m, graph, colors):
                return True
            colors[vertex] = 0

    return False


def m_coloring(graph, m):
    """
    A function to color the vertices of the graph using at most m colors.

    Parameters:
    - graph (List[List[int]]): the graph represented as a 2D matrix
    - m (int): the maximum number of colors allowed

    Returns:
    - A list of colors assigned to each vertex if a valid coloring exists,
    - None otherwise.
    """
    # Initialize colors of all vertices as 0
    colors = [0] * len(graph)

    # Try to color the graph
    if m_coloring_util(0, m, graph, colors) is False:
        return None

    # Return the list of colors
    return colors


class TestMColoring(unittest.TestCase):
    def test_m_coloring_with_solution(self):
        graph1 = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
        m1 = 3
        expected_colors1 = [1, 2, 3, 2]
        self.assertEqual(m_coloring(graph1, m1), expected_colors1)

    def test_m_coloring_with_no_solution(self):
        graph2 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0]]
        m2 = 2
        self.assertIsNone(m_coloring(graph2, m2))


if __name__ == "__main__":
    unittest.main()
