# Queue

## Implementation

The implementation of the `Queue` class are placed in [queue.py](../../data_structures/queue.py)

## Explanation

This code defines a `Queue` class using a Python list as the underlying data structure. The class has several methods:

- `enqueue(item)`: adds an item to the back of the queue
- `dequeue()`: removes and returns the front item from the queue
- `peek()`: returns the front item from the queue without removing it
- `is_empty()`: returns `True` if the queue is empty, `False` otherwise
- `size()`: returns the number of items in the queue

In addition, the class overloads the `__str__` and `__repr__` methods to display the contents of the queue.

The code also includes a `TestQueue` class which inherits from `unittest.TestCase` and defines several test methods to test the functionality of the `Queue` class. These test methods use the `unittest.TestCase` methods such as `assertEqual` to check if the output of the methods of the `Queue` class match the expected output