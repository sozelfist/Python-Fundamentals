# Sorting Algorithms

## Introduction

Sorting algorithms are a class of algorithms that arrange a collection of items into a specific order, typically from smallest to largest or vice versa. Sorting is a fundamental problem in computer science and is used in many applications, including databases, search algorithms, and data analysis.

There are many different sorting algorithms, each with their own strengths and weaknesses. The choice of sorting algorithm depends on the size of the data set, the distribution of the data, and the performance requirements of the application.

## Types of Sorting Algorithms

The following are some of the most commonly used sorting algorithms:

1. Bubble Sort: Bubble sort is a simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.

    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/220px-Bubblesort-edited-color.svg.png">
        <p>Static visualization of bubble sort</p>
    </div>

    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif">
        <p>An example of bubble sort. Starting from the beginning of the list, compare every adjacent pair, swap their position if they are not in the right order (the latter one is smaller than the former one). After each iteration, one less element (the last one) is needed to be compared until there are no more elements left to be compared.</p>
    </div>

2. Selection Sort: Selection sort is a simple sorting algorithm that repeatedly selects the smallest element from the unsorted portion of the list and places it at the beginning of the sorted portion.
    | Sorted sublist       | Unsorted sublist     | Least element in unsorted list |
    | -------------------- | -------------------- | ------------------------------ |
    | ()                   | (11, 25, 12, 22, 64) | 11                             |
    | (11)                 | (25, 12, 22, 64)     | 12                             |
    | (11, 12)             | (25, 22, 64)         | 22                             |
    | (11, 12, 22)         | (25, 64)             | 25                             |
    | (11, 12, 22, 25)     | (64)                 | 64                             |
    | (11, 12, 22, 25, 64) | ()                   |

3. Insertion Sort: Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif">
        <p>A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list. With each iteration one element (red) is removed from the "not yet checked for order" input data and inserted in-place into the sorted list.</p>
    </div>

4. Merge Sort: Merge sort is a divide-and-conquer sorting algorithm that works by splitting the array into smaller subarrays, sorting them, and then merging them back together.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif">
        <p>An example of merge sort. First, divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally, all the elements are sorted and merged.</p>
    </div>

5. Quick Sort: Quick sort is a divide-and-conquer sorting algorithm that works by selecting a pivot element and partitioning the array into two subarrays, one with elements smaller than the pivot and one with elements larger than the pivot.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Quicksort-diagram.svg/200px-Quicksort-diagram.svg.png">
        <p>Full example of quicksort on a random set of numbers. The shaded element is the pivot. It is always chosen as the last element of the partition.</p>
    </div>


| **Algorithm**  | **Best Case Time Complexity** | **Average Case Time Complexity** | **Worst Case Time Complexity** | **Space Complexity** |
| -------------- | ----------------------------- | -------------------------------- | ------------------------------ | -------------------- |
| Bubble Sort    | $O(n)$                        | $O(n^2)$                         | $O(n^2)$                       | $O(1)$               |
| Selection Sort | $O(n^2)$                      | $O(n^2)$                         | $O(n^2)$                       | $O(1)$               |
| Insertion Sort | $O(n)$                        | $O(n^2)$                         | $O(n^2)$                       | $O(1)$               |
| Merge Sort     | $O(n\log n)$                  | $O(n\log n)$                     | $O(n\log n)$                   | $O(n)$               |
| Quick Sort     | $O(n\log n)$                  | $O(n\log n)$                     | $O(n^2)$                       | $O(log n)$           |

## Performance Characteristics

Sorting algorithms can be evaluated based on their performance characteristics, including time complexity and space complexity.

Time complexity is a measure of the number of operations required to sort an array of n elements. The best-case, average-case, and worst-case time complexity of a sorting algorithm can be expressed using Big O notation.

Space complexity is a measure of the amount of memory required by the algorithm. In-place sorting algorithms use only a constant amount of additional memory, while out-of-place algorithms require additional memory proportional to the size of the input.

## Conclusion

Sorting algorithms are a fundamental problem in computer science and are used in many applications. There are many different sorting algorithms, each with their own strengths and weaknesses. The choice of sorting algorithm depends on the size of the data set, the distribution of the data, and the performance requirements of the application. When evaluating sorting algorithms, it's important to consider their time and space complexity, as well as their ease of implementation and debugging.