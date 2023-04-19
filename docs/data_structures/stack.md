# Stack

## Implementation

The `Stack` class implementation is at [stack.py](../../data_structures/stack.py)

## Explanation

This code defines a class called `Stack` which implements a basic stack data structure. A stack is a Last In, First Out (LIFO) data structure where elements are added and removed from the top of the stack. The code uses a list to store the elements in the stack.

The class has several methods:

- `push(item: int)`: This method takes an integer as input and adds it to the top of the stack by appending it to the list.

- `pop()`: This method removes the top element from the stack and returns it. If the stack is empty, it raises an exception with the message `"Stack is empty"`.

- `peek()`: This method returns the top element of the stack without removing it. If the stack is empty, it raises an exception with the message `"Stack is empty"`.

- `is_empty()`: This method returns a boolean indicating whether the stack is empty or not.

- `size()`: This method returns the number of elements in the stack.

The code also includes a test class called `TestStack` which uses the `unittest` library to define several test cases for the Stack class. These test cases include: testing the `push` method, testing the `pop` method, testing the `peek` method, testing if stack is empty, testing the `size` of stack. The test cases are executed by the last line of the code which calls the `unittest.main()` method.