import unittest

# Define a type alias for a maze, which is represented as a 2D grid of characters.
Maze = list[list[str]]

# Define a type alias for a point in the maze, which is represented as a tuple of x and y coordinates.
Point = tuple[int, int]


def find_path(maze: Maze, start: Point, end: Point) -> list[Point]:
    """Finds a path through a maze from a starting point to an end point.

    Args:
        maze: A 2D grid of characters representing the maze.
        start: A tuple of x and y coordinates representing the starting point.
        end: A tuple of x and y coordinates representing the end point.

    Returns:
        A list of tuples representing the path from the starting point to the end point,
        or an empty list if no path is found.
    """
    # Define a recursive helper function to explore all possible paths.
    def explore_path(path: list[Point], current: Point) -> list[Point]:
        # Add the current point to the path.
        path.append(current)

        # If we've reached the end point, return the path.
        if current == end:
            return path

        # Try moving in each of the four possible directions (up, down, left, right).
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x, y = current[0] + dx, current[1] + dy

            # Check that the new position is within the maze and not a wall.
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':

                # Check that we haven't already visited this position.
                if (x, y) not in path:

                    # Explore the path recursively from the new position.
                    new_path = explore_path(path, (x, y))

                    # If we've found a path, return it.
                    if new_path:
                        return new_path

        # If we've explored all possible paths from this position and haven't found a solution, backtrack.
        path.pop()
        return []

    # Start exploring paths from the starting point.
    return explore_path([], start)


class TestFindPath(unittest.TestCase):

    def test_simple_maze(self):
        maze = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        start = (1, 1)
        end = (2, 2)
        expected_path = [(1, 1), (1, 2), (2, 2)]
        path = find_path(maze, start, end)
        self.assertEqual(path, expected_path)

    def test_complex_maze(self):
        maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        start = (1, 1)
        end = (5, 7)
        expected_path = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (2, 5),
                         (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7)]
        path = find_path(maze, start, end)
        self.assertEqual(path, expected_path)

    def test_no_path(self):
        maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        start = (1, 1)
        end = (5, 8)
        path = find_path(maze, start, end)
        self.assertEqual(path, [])


if __name__ == '__main__':
    unittest.main()
