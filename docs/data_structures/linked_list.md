# Linked List

## Implementation

The implementation of `LinkedList` class is at [linked_list.py](../../data_structures/linked_list.py)

## Explaination

The code above is an implementation of a singly linked list data structure in Python using object-oriented programming (OOP) and type hints. The implementation includes a Node class and a `LinkedList` class.

The `Node` class has a constructor that takes in a single argument, `data`, which represents the value stored in the node. The class also has an instance variable, `next`, which is a reference to the next node in the list and is initialized to `None`.

The `LinkedList` class has a constructor that initializes an empty list, with the instance variable `head` set to `None`.

The class has several methods that allows the user to manipulate the linked list:

- The `append()` method takes in a `data` value, creates a new node with that value, and adds it to the end of the list. 
- The `insert()` method takes in a `prev_node` and a `data` value, creates a new node with that `value`, and adds it after the `prev_node`. 
- The `delete()` method takes in a `data` value and removes the first node with that value from the list. 
- The `search()` method takes in a `data` value and returns the first node with that `value`.

The class also has methods that allow the user to access the linked list using an `index`, using the `__getitem__` method and `__len__` method. The `__str__` and `__repr__` methods return the string representation of the linked list in the form of `"1->2->3->..."`

There is also a `TestLinkedList` class which uses `unittest` module to test the implemented functionalities of the `LinkedList` class by creating instances of it and calling the methods on it and checking the output against the expected output.