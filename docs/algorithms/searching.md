# Searching Algorithms

Searching algorithms are a set of instructions that take a collection of data as input and find a specific element or a group of elements that match a certain condition. Like sorting algorithms, there are many different searching algorithms, each with their own strengths and weaknesses. Some of the most commonly used searching algorithms include:

- Linear Search: This algorithm checks every element of the array sequentially, until it finds the desired element or determines that the element is not present. It has a time complexity of $O(n)$, where $n$ is the number of elements in the array.

- Binary Search: This algorithm finds the position of a target value within a sorted array. It compares the target value to the middle element of the array; if they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. The time complexity of binary search is $O(\log{n})$

- Jump Search: This algorithm searches for a particular value by jumping through the list by a fixed step size. It is similar to Linear Search but with the added advantage of jumping. It has a time complexity of $O(\sqrt{n})$.

- Interpolation Search: This algorithm improves on the binary search algorithm by using the value of the element being searched for to estimate the position of the element in the array. It has a average time complexity of $O(\log{(\log{n}}))$

- Exponential Search: This algorithm improves on the binary search algorithm by first finding the range where the element is likely to be present and then applying binary search on that range. It has a average time complexity of $O(\log{n})$

- Sublist Search (*not implemented yet*): This algorithm searches for a list (the sublist) within another list (the superlist). It has a time complexity of $O(n\times m)$ where n and m are the lengths of the superlist and sublist respectively

- Breadth-First Search: This algorithm explores all the vertices of a graph or all the nodes of a tree in breadth-first order. It starts at the tree root (or some arbitrary node of a graph) and explores the neighbor nodes first, before moving to the next level neighbours.

- Depth-First Search: This algorithm explores all the vertices of a graph or all the nodes of a tree in depth-first order. It starts at the tree root (or some arbitrary node of a graph) and explores as far as possible along each branch before backtracking.

There are other searching algorithms too, but these are some of the most popular and widely used. Each algorithm has its own time and space complexity and is suitable for different types of data and problem.