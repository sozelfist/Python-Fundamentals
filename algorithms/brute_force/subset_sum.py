import unittest


def subset_sum_brute_force(numbers: list[int], target: int) -> list[list[int]]:
    """
    Brute-force subset sum algorithm that tries all possible subsets
    of a given set to find all subsets whose sum is equal to a given
    target value.

    Args:
        numbers: A list of integers.
        target: The target value to be achieved by summing a subset of numbers.

    Returns:
        A list of lists of integers representing all possible subsets
        of the input list that sum to the target value, or an empty
        list if no such subsets were found.
    """

    n = len(numbers)
    subsets = []
    for i in range(2 ** n):
        subset = [numbers[j] for j in range(n) if (i & (1 << j)) > 0]
        if sum(subset) == target:
            subsets.append(subset)

    # Sort the subsets by length, then by their elements
    subsets.sort(key=lambda x: (len(x), x))

    return subsets


class TestSubsetSumBruteForce(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        numbers: list[int] = []
        target: int = 0
        expected_subsets: list[list[int]] = [[]]
        self.assertEqual(subset_sum_brute_force(
            numbers, target), expected_subsets)

    def test_no_subsets(self):
        # Test when there are no subsets that sum to the target value
        numbers: list[int] = [1, 2, 3, 4, 5]
        target: int = 100
        expected_subsets: list[list[int]] = []
        self.assertEqual(subset_sum_brute_force(
            numbers, target), expected_subsets)

    def test_single_element(self):
        # Test with a list containing a single element
        numbers: list[int] = [42]
        target: int = 42
        expected_subsets: list[list[int]] = [[42]]
        self.assertEqual(subset_sum_brute_force(
            numbers, target), expected_subsets)

    def test_multiple_subsets(self):
        # Test when there are multiple subsets that sum to the target value
        numbers: list[int] = [1, 2, 3, 4, 5]
        target: int = 9
        expected_subsets: list[list[int]] = [[4, 5], [1, 3, 5], [2, 3, 4]]
        self.assertEqual(subset_sum_brute_force(
            numbers, target), expected_subsets)

    def test_all_elements(self):
        # Test when all elements of the list sum to the target value
        numbers: list[int] = [1, 2, 3, 4, 5]
        target: int = 15
        expected_subsets: list[list[int]] = [[1, 2, 3, 4, 5]]
        self.assertEqual(subset_sum_brute_force(
            numbers, target), expected_subsets)


if __name__ == '__main__':
    unittest.main()
