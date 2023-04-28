# Binary Tree

A binary tree is a data structure made up of nodes that are connected by edges or branches. A binary tree has at most two children, referred to as the left and right children. If there are no nodes in the tree, it is considered to be empty.

The root node is the initial node in a binary tree. All other nodes are either the left or right child of another node. Nodes with no children are known as leaf nodes, while nodes with at least one child are known as interior nodes.

According to a stated ordering of the tree's elements, the relationship between nodes in a binary tree is such that for each node, its left child (if it exists) is less than or equal to the node, and its right child (if it exists) is greater than or equal to the node.

In computer science and programming, binary trees are frequently used to build efficient searching, sorting, and indexing algorithms. They can also be used to represent hierarchical structures like family trees, decision trees, and syntax trees.


<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Binary_tree_v2.svg/220px-Binary_tree_v2.svg.png">
    <p>A labeled binary tree of size 9 and height 3, with a root node whose value is 1. The above tree is unbalanced and not sorted.</p>
</div>

## Types of Binary Tree

There are several types of binary trees, including:

1. Full binary tree: A binary tree in which each node has either two children or no children (i.e., it is a leaf node).

2. Complete binary tree: A binary tree in which all levels are completely filled, except possibly for the last level, which is filled from left to right.

3. Balanced binary tree: A binary tree in which the height of the left and right subtrees of any node differ by at most 1.

4. Perfect binary tree: A binary tree in which all internal nodes have two children and all leaf nodes are at the same level.

5. Degenerate (or pathological) tree: A binary tree in which each parent node has only one associated child node, creating a long chain-like structure.

6. Threaded binary tree: A binary tree in which some nodes have extra pointers that allow for faster traversal of the tree.

7. Binary search tree: A binary tree in which for each node, its left child is less than or equal to the node, and its right child is greater than or equal to the node, according to a specified ordering of the elements in the tree.



8. AVL tree: A binary search tree that is balanced, meaning that the height of the left and right subtrees of any node differ by at most 1.

9. Red-black tree: A binary search tree that is self-balancing and maintains a balance by coloring nodes with one of two colors, typically red and black.

10. 2-3 tree: A tree in which each node can have either two or three children, and which is used for storing sorted data.

11. B-tree: A tree that is used for indexing data in a database, in which each node can have many children (usually between two and several hundred), and which allows for efficient searching and insertion of data.

The type of binary tree used in a particular application will depend on the specific requirements of that application, such as the desired level of balance, the type of data being stored, and the efficiency requirements for searching and insertion.

## Implementation

The `BinaryTree` class in implemented in [binary_tree.py](../../data_structures/binary_tree.py)

## Explanation

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