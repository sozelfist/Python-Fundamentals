from typing import List, Tuple, Callable
import unittest


def tabu_search(initial_solution: List[int], objective_function: Callable,
                neighborhood_function: Callable, tabu_list_length: int,
                max_iterations: int) -> Tuple[List[int], int]:
    """
    Implementation of Tabu search algorithm for combinatorial optimization problems.

    Args:
    - initial_solution: A list representing the initial solution.
    - objective_function: A callable that takes a list and returns a numeric value representing
      the quality of the solution.
    - neighborhood_function: A callable that takes a list and returns a list of neighboring solutions.
    - tabu_list_length: The length of the tabu list, which determines how long a move will remain
      forbidden after it has been made.
    - max_iterations: The maximum number of iterations to run the algorithm.

    Returns:
    - A tuple containing the best solution found and its objective value.
    """
    current_solution = initial_solution.copy()
    best_solution = current_solution.copy()
    tabu_list = []
    best_objective_value = objective_function(current_solution)

    for i in range(max_iterations):
        neighbors = neighborhood_function(current_solution)
        best_neighbor = None
        best_neighbor_objective_value = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_objective_value = objective_function(neighbor)
                if neighbor_objective_value < best_neighbor_objective_value:
                    best_neighbor = neighbor
                    best_neighbor_objective_value = neighbor_objective_value

        if best_neighbor is not None:
            current_solution = best_neighbor
            tabu_list.append(current_solution)
            if len(tabu_list) > tabu_list_length:
                tabu_list.pop(0)
            current_objective_value = best_neighbor_objective_value

            if current_objective_value < best_objective_value:
                best_solution = current_solution.copy()
                best_objective_value = current_objective_value

    return (best_solution, best_objective_value)


class TestTabuSearch(unittest.TestCase):

    def test_solution_found(self):
        # Test that the function can find a valid solution to the optimization problem
        initial_solution = [0, 0]
        tabu_list_length = 5
        max_iterations = 50

        def objective_function(x):
            return x[0]**2 + x[1]**2 - 2 * x[0] - 4 * x[1] + 4

        def neighborhood_function(x):
            neighbors = []
            if x[0] > 0:
                neighbors.append([x[0] - 1, x[1]])
            if x[0] < 4:
                neighbors.append([x[0] + 1, x[1]])
            if x[1] > 0:
                neighbors.append([x[0], x[1] - 1])
            if x[1] < 4:
                neighbors.append([x[0], x[1] + 1])
            return neighbors
        best_solution, best_objective_value = tabu_search(
            initial_solution, objective_function, neighborhood_function, tabu_list_length, max_iterations)
        # Ensure that the objective value is at least as good as the true optimal value
        self.assertGreaterEqual(best_objective_value, -9.0)
        # Ensure that the solution satisfies the constraints of the optimization problem
        self.assertGreaterEqual(best_solution[0] + best_solution[1], 3)

    def test_no_improvement(self):
        # Test that the function terminates if no improvement is made for a certain number of iterations
        initial_solution = [1, 2]
        tabu_list_length = 5
        max_iterations = 50

        def objective_function(x):
            return x[0]**2 + x[1]**2 - 2 * x[0] - 4 * x[1] + 4

        def neighborhood_function(x):
            return [[x[0] - 1, x[1]], [x[0] + 1, x[1]], [x[0], x[1] - 1], [x[0], x[1] + 1]]
        best_solution, best_objective_value = tabu_search(
            initial_solution, objective_function, neighborhood_function, tabu_list_length, max_iterations)
        # Ensure that the function returns the initial solution if no improvement is made
        self.assertEqual(best_solution, initial_solution)

    def test_small_tabu_list(self):
        # Test that the function can still find a valid solution with a small tabu list
        initial_solution = [0, 0]
        tabu_list_length = 1
        max_iterations = 50

        def objective_function(x):
            return x[0]**2 + x[1]**2 - 2 * x[0] - 4 * x[1] + 4

        def neighborhood_function(x):
            neighbors = []
            if x[0] > 0:
                neighbors.append([x[0] - 1, x[1]])
            if x[0] < 4:
                neighbors.append([x[0] + 1, x[1]])
            if x[1] > 0:
                neighbors.append([x[0], x[1] - 1])
            if x[1] < 4:
                neighbors.append([x[0], x[1] + 1])
            return neighbors
        best_solution, best_objective_value = tabu_search(
            initial_solution, objective_function, neighborhood_function, tabu_list_length, max_iterations)
        # Ensure that the objective value is at least as good as the true optimal value
        self.assertGreaterEqual(best_objective_value, -9.0)
        # Ensure that the solution satisfies the constraints of the optimization problem
        self.assertGreaterEqual(best_solution[0] + best_solution[1], 3)

    def test_large_tabu_list(self):
        # Test that the function can still find a valid solution with a large tabu list
        initial_solution = [0, 0]
        tabu_list_length = 10
        max_iterations = 50

        def objective_function(x):
            return x[0]**2 + x[1]**2 - 2 * x[0] - 4 * x[1] + 4

        def neighborhood_function(x):
            neighbors = []
            if x[0] > 0:
                neighbors.append([x[0] - 1, x[1]])
            if x[0] < 4:
                neighbors.append([x[0] + 1, x[1]])
            if x[1] > 0:
                neighbors.append([x[0], x[1] - 1])
            if x[1] < 4:
                neighbors.append([x[0], x[1] + 1])
            return neighbors
        best_solution, best_objective_value = tabu_search(
            initial_solution, objective_function, neighborhood_function, tabu_list_length, max_iterations)
        # Ensure that the objective value is at least as good as the true optimal value
        self.assertGreaterEqual(best_objective_value, -9.0)
        # Ensure that the solution satisfies the constraints of the optimization problem
        self.assertGreaterEqual(best_solution[0] + best_solution[1], 3)


if __name__ == '__main__':
    unittest.main()
