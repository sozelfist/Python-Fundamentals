## Heap

## Implementation

The implementation of the `Heap` class is placed in [heap.py](../../data_structures/heap.py)

## Explaination

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