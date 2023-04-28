# Priority Queue

In computer science, a _priority queue_ is an abstract data-type similar to a regular queue or stack data structure. Each element in a priority queue has an associated priority. In a priority queue, elements with high priority are served before elements with low priority. In some implementations, if two elements have the same priority, they are served in the same order that they were enqueued in. In other implementations, the order of elements with the same priority is undefined.

While priority queues are often implemented using heaps, they are conceptually distinct from heaps. A priority queue is an abstract data structure like a list or a map; just as a list can be implemented with a linked list or with an array, a priority queue can be implemented with a heap or another method such as an unordered array.

## Implementation

The implementation of the `PriorityQueue` class is at [priority_queue.py](../../data_structures/priority_queue.py)

## Explanation

This code defines a `PriorityQueue` class that is based on a binary heap data structure. A priority queue is a data structure that stores elements in a specific order, so that the element with the highest or lowest priority can be retrieved quickly. In this case, the `PriorityQueue` class can be initialized with either a min heap or a max heap. The `PriorityQueue` class has the following methods:

- `insert(value)`: adds a value to the priority queue
- `peek()`: returns the element with the highest or lowest priority without removing it from the queue
- `poll()`: returns the element with the highest or lowest priority and removes it from the queue
- `heapify_up(index)`: restores the heap property when an element is inserted
- `heapify_down(index)`: restores the heap property when an element is removed
- `build_heap()`: creates a valid heap from an unordered list

The class also has a `should_swap` method, which compares the priorities of two elements and returns `true` or `false` depending on whether they should be swapped in the heap or not.

Additionally, there is a `TestPriorityQueue` class that tests the implementation of the `PriorityQueue` class. It creates a priority queue, inserts elements into it and check their order and if it is correct.