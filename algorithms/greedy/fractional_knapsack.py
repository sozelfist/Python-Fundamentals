import unittest
from typing import List, Tuple


def fractional_knapsack(items: List[Tuple[int, int]], capacity: int) -> float:
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
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
        items = [(5, 30), (8, 120), (7, 10), (0, 20), (4, 50), (5, 80), (2, 10)]
        capacity = 20
        self.assertEqual(fractional_knapsack(items, capacity), 240)

        items = [(5, 20), (8, 100), (7, 10), (0, 20), (4, 50), (5, 80), (2, 10)]
        capacity = 20
        self.assertEqual(fractional_knapsack(items, capacity), 220)

        items = [(5, 20), (8, 100), (7, 10), (0, 20), (4, 50), (5, 80), (2, 10)]
        capacity = 0
        self.assertEqual(fractional_knapsack(items, capacity), 0)


if __name__ == '__main__':
    unittest.main()
