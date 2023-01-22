# Sorting Algorithms

Sorting algorithms are a set of instructions that take an array of data as input and rearrange it into a certain order. There are many different sorting algorithms, each with their own strengths and weaknesses. Some of the most commonly used sorting algorithms include:

- **Bubble sort**: Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
- **Insertion sort**: This algorithm builds the final sorted list one item at a time. It starts with an empty left hand side and the item on the list is inserted back into the sorted sub-list (left side)
- **Selection sort**: This algorithm divides the input list into two parts: the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire input list. The smallest element is selected from the unsorted array and swapped with the leftmost unsorted element, moving the boundary of the sorted sublist one step to the right.
- **Merge sort**: This algorithm divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted). Then repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
- **Quick sort**: This algorithm selects a 'pivot' element from the list and partitions the other elements into two sub-lists, according to whether they are less than or greater than the pivot. The sub-lists are then sorted recursively.
- **Heap sort**: This algorithm first builds a heap from the input list and then repeatedly extracts the maximum element from the heap and places it at the end of the sorted list.
- **Radix sort**: This algorithm sorts the elements by first grouping the individual elements of the same radix(i.e. digits in a number if the elements are numbers) together and then sorting the elements according to their radix.

There are other sorting algorithms too but these are some of the most popular and widely used. Each algorithm has its own time and space complexity and is suitable for different types of data and problem.