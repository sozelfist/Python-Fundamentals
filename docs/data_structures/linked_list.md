# Linked List

In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

The principal benefit of a linked list over a conventional array is that the list elements can be easily inserted or removed without reallocation or reorganization of the entire structure because the data items do not need to be stored contiguously in memory or on disk, while restructuring an array at run-time is a much more expensive operation. Linked lists allow insertion and removal of nodes at any point in the list, and allow doing so with a constant number of operations by keeping the link previous to the link being added or removed in memory during list traversal.

## Types of Linked List

### Singly linked list

Singly linked lists contain nodes which have a `value` field as well as `next` field, which points to the next node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and traversal.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png">
    <p>
        A singly linked list whose nodes contain two fields: an integer value and a link to the next node
    </p>
</div>

### Doubly linked list

In a doubly linked list, each node contains, besides the next-node link, a second link field pointing to the `previous` node in the sequence. The two links may be called `forward` and `backwards`, or `next` and `prev`(`previous`).

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png">
    <p>
        A doubly linked list whose nodes contain three fields: an integer value, the link forward to the next node, and the link backward to the previous node
    </p>
</div>

### Circular linked list

In the last node of a list, the link field often contains a null reference, a special value is used to indicate the lack of further nodes. A less common convention is to make it point to the first node of the list; in that case, the list is said to be _circular_ or _circularly linked_; otherwise, it is said to be _open_ or _linear_. It is a list where the last pointer points to the first node.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/350px-Circularly-linked-list.svg.png">
    <p>
        A circular linked list
    </p>
</div>

## Implementation

The implementation of `LinkedList` class is at [linked_list.py](../../data_structures/linked_list.py)

## Explanation

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