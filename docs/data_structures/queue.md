# Queue

In computer science, a _queue_ is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence. By convention, the end of the sequence at which elements are added is called the back, tail, or rear of the queue, and the end at which elements are removed is called the head or front of the queue, analogously to the words used when people line up to wait for goods or services.

The operation of adding an element to the rear of the queue is known as _enqueue_, and the operation of removing an element from the front is known as _dequeue_. Other operations may also be allowed, often including a _peek_ or _front_ operation that returns the value of the next element to be dequeued without dequeuing it.

The operations of a queue make it a first-in-first-out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed. This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed. A queue is an example of a linear data structure, or more abstractly a sequential collection. Queues are common in computer programs, where they are implemented as data structures coupled with access routines, as an abstract data structure or in object-oriented languages as classes. Common implementations are circular buffers and linked lists.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/220px-Data_Queue.svg.png">
    <p>
        Representation of a FIFO (first in, first out) queue
    </p>
</div>

## Time complexity in big O notation


| **Algorithm** | **Average** | **Worst case** |
| ------------- | ----------- | -------------- |
| **Space**     | $O(n)$      | $O(n)$         |
| **Search**    | $O(n)$      | $O(n)$         |
| **Insert**    | $O(1)$      | $O(1)$         |
| **Delete**    | $O(1)$      | $O(1)$         |

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