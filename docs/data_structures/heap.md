## Heap

A Heap is a specialized tree-based data structure in which the parent node is either greater than or less than its children nodes, depending on whether it is a _Max Heap_ or a _Min Heap_, respectively.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Max-Heap-new.svg/220px-Max-Heap-new.svg.png">
    <p>Example of a binary max-heap with node keys being integers between 1 and 100</p>
</div>

## Types of Heap

A Max Heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. The node at the root of the tree has the largest value.

A Min Heap is also a complete binary tree where the value of each node is less than or equal to the values of its children. The node at the root of the tree has the smallest value.

## Applications

Heaps are commonly used to implement priority queues, which are used in a variety of applications, such as task scheduling, Dijkstra's algorithm, and Huffman coding.


## Operations

The two main operations supported by heaps are:

1. Insertion: A new element is added to the heap by inserting it at the next available position in the bottom level of the tree, and then bubbling it up to its proper position by comparing it with its parent node.

2. Deletion: The root node is removed from the heap, and the last element in the bottom level of the tree is moved to the root position. The element is then bubbled down to its proper position by comparing it with its children nodes.

## Complexities

Heaps have a time complexity of O(log n) for both insertion and deletion operations, where n is the number of elements in the heap. However, building a heap from an unsorted array takes O(n) time, and the complexity of finding the kth smallest or largest element in a heap is O(k log n), which is less efficient than other algorithms such as quickselect.

## Implementation

The implementation of the `Heap` class is placed in [heap.py](../../data_structures/heap.py)

## Explanation

This code defines a class called `Heap` which is a simple implementation of a min or max heap data structure. The heap can be initialized as a min heap or a max heap, and it can be initialized with an array of values.

The class has several methods:

- `build_heap()`: This method is called when the heap is initialized and it creates the heap by maintaining the min or max heap property.

- `heapify()`: This method is used to maintain the min or max heap property after an element is added or removed from the heap. It takes an index of an element and compares it to its children and if necessary, it swaps the element with one of its children to maintain the min or max heap property.

- `push()`: This method is used to add an element to the heap. It first appends the element to the end of the heap, then it compares the element with its parent and if necessary, it swaps the element with its parent to maintain the min or max heap property.

- `pop()`: This method is used to remove the minimum (in case of min heap) or maximum element (in case of max heap) from the heap. It swaps the first and last element of the heap, then it removes the last element and calls the `heapify()` method to maintain the min or max heap property.

- `poll()`: This method is similar to the `pop()` method, but it only returns the minimum (in case of min heap) or maximum element (in case of max heap) without removing it.

- `top()`: This method returns the minimum (in case of min heap) or maximum element (in case of max heap) without removing it.

The class also has `__len__` and `__repr__` methods to return the length of the heap and a string representation of the heap, respectively. Additionally, the class has `__iter__` method which allow you to iterate over the heap.

The class also has test cases defined using `unittest` to test the heap implementation.