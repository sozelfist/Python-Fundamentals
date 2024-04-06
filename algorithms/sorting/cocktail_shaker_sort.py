"""The Cocktail Shaker Sort algorithm, also known as the Cocktail Sort
or the Shaker Sort. It is a variation of the Bubble Sort algorithm
that sorts elements in a list by repeatedly traversing the list in
both directions, swapping adjacent elements if they are in the wrong order.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
Pseudocode:
```
procedure cocktailShakerSort(A : list of sortable items) is
    do
        swapped := false
        for each i in 0 to length(A) − 1 do:
            // test whether the two elements are in the wrong order
            if A[i] > A[i + 1] then
                swap(A[i], A[i + 1]) // let the two elements change places
                swapped := true
            end if
        end for
        if not swapped then
            // we can exit the outer loop here if no swaps occurred.
            break do-while loop
        end if
        swapped := false
        for each i in length(A) − 1 to 0 do:
            if A[i] > A[i + 1] then
                swap(A[i], A[i + 1])
                swapped := true
            end if
        end for
    while swapped
    // if no elements have been swapped, then the list is sorted
end procedure
```
"""

import unittest
from typing import TypeVar

T = TypeVar("T")


def cocktail_shaker_sort(arr: list[T]) -> list[T]:
    left = 0
    right = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        # Traverse from left to right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # Traverse from right to left
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

    return arr


class TestCocktailShakerSort(unittest.TestCase):
    def test_sort_empty_list(self):
        arr: list[int] = []
        sorted_arr = cocktail_shaker_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_sort_already_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = cocktail_shaker_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_sort_reversed_list(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = cocktail_shaker_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_sort_random_list(self):
        arr = [7, 3, 9, 2, 1, 5]
        sorted_arr = cocktail_shaker_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 5, 7, 9])

    def test_sort_duplicate_elements(self):
        arr = [5, 2, 8, 1, 9, 3, 5, 2, 1]
        sorted_arr = cocktail_shaker_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 2, 3, 5, 5, 8, 9])


if __name__ == "__main__":
    unittest.main()
