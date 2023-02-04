import unittest
from typing import List, Tuple


def fractional_knapsack(items: List[Tuple[int, int]], capacity: int) -> float:
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break
    return total_value


class TestFractionalKnapsack(unittest.TestCase):
    def test_fractional_knapsack(self):
        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(result, 240.0, delta=1e-9)

        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 20
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(result, 110.0, delta=1e-9)

        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 70
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(result, 280.0, delta=1e-9)

        items = [(10, 60), (20, 100), (30, 120)]
        capacity = 0
        result = fractional_knapsack(items, capacity)
        self.assertAlmostEqual(result, 0.0, delta=1e-9)


if __name__ == '__main__':
    unittest.main()
