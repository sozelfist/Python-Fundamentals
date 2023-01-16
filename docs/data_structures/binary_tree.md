# Binary Tree

## Implementation

The `BinaryTree` class in implemented in [binary_tree.py](../../data_structures/binary_tree.py)

## Explaination

This code is an implementation of a binary tree data structure in Python.

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

The code begins by defining a BinaryTree class which has the following methods:

- `__init__(self, data: int)`: This is the constructor method for the class. It initializes a new binary tree node and assigns the passed data to the node's data attribute. It also sets the `left` and `right` children of the node to `None`.

- `insert(self, data: int)`: This method is used to insert a new node into the binary tree. It compares the value of the `data` passed to the method with the value of the node's `data` attribute. If the `data` passed is less than the node's `data`, it is inserted as the `left` child of the node. If it is greater, it is inserted as the `right` child. If the node already has a `left` or `right` child, the method is called recursively on the `left` or `right` child respectively.

- `lookup(self, data: int, parent: Union[None, 'BinaryTree'] = None) -> Union[None, 'BinaryTree']`: This method is used to search the tree for a node with a specific `data` value. It compares the value of the `data` passed to the method with the value of the node's `data` attribute. If the `data` passed is less than the node's `data`, it recursively calls the method on the `left` child. If it is greater, it recursively calls the method on the `right` child. If the value is equal, it returns the node and its `parent`.

- `children_count(self) -> int`: This method returns the number of children of a node.

- `delete(self, data: int) -> Union[None, 'BinaryTree']`: This method is used to delete a node from the tree. It first calls the lookup method to find the node to be deleted and its parent. Then it checks the number of children of the node. If the node has no children, it simply deletes the node. If it has one child, it replaces the node with its child. If it has two children, it replaces the node with its in-order successor (the leftmost child of its right subtree) and deletes the in-order successor.

- `__str__(self)`: This is a special method that is called when we try to print the tree. It calls another method `_print_tree()` which is used to print the tree in a human-readable format.

The last part of the code defines a `TestBinaryTree` class that inherits from `unittest.TestCase`. This class is used to test the implementation of the `BinaryTree` class by creating an instance of the tree and calling various methods on it, then comparing the results to the expected outcome. The test cases include testing for insertion of new nodes, lookup of nodes, deletion of nodes, and checking the structure of the tree after each operation.