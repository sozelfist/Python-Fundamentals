import unittest

import numpy as np


def markov_chain(
    transitions: list[list[float]], initial_state: int, num_steps: int
) -> list[int]:
    """
    Simulate a discrete-time Markov chain with a given transition matrix,
    starting state, and number of steps.

    Args:
    - transitions: a list of lists representing the transition probabilities
    between states, where transitions[i][j] is the probability of
    transitioning from state i to state j.
    - initial_state: an integer representing the starting state of the Markov
    chain.
    - num_steps: an integer representing the number of steps to simulate the
    Markov chain.

    Returns:
    - A list of integers representing the sequence of states visited by the
    Markov chain, starting with the initial state.
    """
    # Convert the transition matrix to a numpy array for faster computations
    transitions = np.array(transitions)

    # Create an empty list to store the sequence of states
    states = [initial_state]

    # Simulate the Markov chain for the specified number of steps
    for _ in range(num_steps):
        # Get the transition probabilities for the current state
        probs = transitions[states[-1]]

        # Sample the next state from the transition probabilities
        next_state = np.random.choice(len(probs), p=probs)

        # Add the next state to the sequence of states
        states.append(next_state)

    return states


class TestMarkovChain(unittest.TestCase):
    def test_simple_chain(self):
        # Define a transition matrix for a simple 2-state Markov chain
        transitions = [[0.7, 0.3],
                       [0.4, 0.6]]
        initial_state = 0
        num_steps = 10

        # Call the markov_chain function to simulate the Markov chain
        states = markov_chain(transitions, initial_state, num_steps)

        # Check that the length of the output
        # sequence is equal to num_steps + 1 (accounting for the initial state)
        self.assertEqual(len(states), num_steps + 1)

        # Check that all elements in the output sequence are either 0 or 1
        self.assertTrue(all(state in [0, 1] for state in states))

    def test_irreducible_chain(self):
        # Define a transition matrix for an irreducible Markov chain
        transitions = [[0.5, 0.5],
                       [0.5, 0.5]]
        initial_state = 0
        num_steps = 1000

        # Call the markov_chain function to simulate the Markov chain
        states = markov_chain(transitions, initial_state, num_steps)

        # Check that the length of the output sequence
        # is equal to num_steps + 1 (accounting for the initial state)
        self.assertEqual(len(states), num_steps + 1)

        # Check that the proportion of time spent in
        # each state converges to the stationary distribution
        # (0.5 for each state)
        self.assertAlmostEqual(states.count(0) / len(states), 0.5, places=1)
        self.assertAlmostEqual(states.count(1) / len(states), 0.5, places=1)


if __name__ == '__main__':
    unittest.main()
