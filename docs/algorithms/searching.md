# Searching Algorithms

## Introduction

Searching algorithms are used to find the location of a specific value or element within a collection of data. There are many different searching algorithms, each with their own strengths and weaknesses. The choice of searching algorithm depends on the size of the data set, the distribution of the data, and the performance requirements of the application.

# Searching Algorithms

Like sorting algorithms, there are many different searching algorithms, each with their own strengths and weaknesses. Some of the most commonly used searching algorithms include:

- Linear Search: This algorithm checks every element of the array sequentially, until it finds the desired element or determines that the element is not present. It has a time complexity of $O(n)$, where $n$ is the number of elements in the array.

- Binary Search: This algorithm finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. The time complexity of binary search is $O(\log{n})$

- Jump Search: This algorithm searches for a particular value by jumping through the list by a fixed step size. It is similar to Linear Search but with the added advantage of jumping. It has a time complexity of $O(\sqrt{n})$.

- Interpolation Search: This algorithm improves on the binary search algorithm by using the value of the element being searched for to estimate the position of the element in the array. It has a average time complexity of $O(\log{(\log{n}}))$

- Exponential Search: This algorithm improves on the binary search algorithm by first finding the range where the element is likely to be present and then applying binary search on that range. It has a average time complexity of $O(\log{n})$

- Sublist Search (*not implemented yet*): This algorithm searches for a list (the sublist) within another list (the superlist). It has a time complexity of $O(n\times m)$ where n and m are the lengths of the superlist and sublist respectively

- Breadth-First Search: This algorithm explores all the vertices of a graph or all the nodes of a tree in breadth-first order. It starts at the tree root (or some arbitrary node of a graph) and explores the neighbor nodes first, before moving to the next level neighbours.

- Depth-First Search: This algorithm explores all the vertices of a graph or all the nodes of a tree in depth-first order. It starts at the tree root (or some arbitrary node of a graph) and explores as far as possible along each branch before backtracking.

## Performance Characteristics

Searching algorithms can be evaluated based on their performance characteristics, including time complexity and space complexity.

Time complexity is a measure of the number of operations required to search for a specific element in a collection of n elements. The best-case, average-case, and worst-case time complexity of a searching algorithm can be expressed using Big O notation.

Space complexity is a measure of the amount of memory required by the algorithm. Hash tables have a higher space complexity than linear and binary search algorithms, but provide constant-time searching on average.

## Conclusion

Searching algorithms are used to find the location of a specific value or element within a collection of data. There are many different searching algorithms, each with their own strengths and weaknesses. The choice of searching algorithm depends on the size of the data set, the distribution of the data, and the performance requirements of the application. When evaluating searching algorithms, it's important to consider their time and space complexity, as well as their ease of implementation and debugging.