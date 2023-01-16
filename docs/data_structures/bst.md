# Binary Search Tree

## Implementation

The implementation of the `BinarySearchTree` class is placed in [binary_search_tree.py](../../data_structures/binary_search_tree.py)

## Explaination

This code defines a class called `BST` which stands for Binary Search Tree. This class has several methods that can be used to manipulate the tree data structure.

- The `__init__` method initializes a new node with a given data and two pointers (`left` and `right`) set to None.

- The `insert` method takes in a `data` as an argument and it compares the data with the current node's data, if the data is less than the current node's data it goes to the left of the tree otherwise it goes to the right of the tree. If the left or right pointer is `None`, it creates a new node with that data, otherwise, it continues to recursively call the `insert` method on the left or right child node.

- The `find` method takes in a data as an argument and it compares the data with the current node's data. If the data is equal to the current node's data, it returns `True`, otherwise, it continues to recursively call the `find` method on the left or right child node depending on if the data is less than or greater than the current node's data. If the data is not found, it returns `False`.

- The `min_value` method returns the smallest value in the tree by traversing down the left side of the tree until it reaches a node that has no left child.

- The `max_value` method returns the largest value in the tree by traversing down the right side of the tree until it reaches a node that has no right child.

- The `delete` method takes in a data as an argument and it uses the find method to locate the node to be deleted. If the node has no children, it simply sets the left or right pointer of the parent node to `None`. If the node has one child, it replaces the current node with its child. If the node has two children, it finds the minimum value in the right subtree, replaces the current node's data with that value and then recursively calls the delete method on the right subtree to remove the duplicate value.

- The `preorder`, `inorder`, and `postorder` methods are used to traverse the tree and return a list of the data of each node visited in the tree.

- The `height` method returns the height of the tree, it is calculated by taking the maximum height of the left subtree and the right subtree and adding one.

- The `size` method returns the size of the tree, it is calculated by adding the size of the left subtree and the size of the right subtree and adding one.

- The `is_balanced` method returns a Boolean value indicating if the tree is balanced or not. It first checks if the difference in height of the left subtree and the right subtree is greater than 1 and returns `False` if it is. Then it recursively checks if the left and right subtrees are balanced and returns true if they are.

The class also includes a test case `TestBST` that uses the `unittest` framework to test the implementation of the class by creating an instance of the BST class, inserting some values and calling the methods on it to check if the results are correct.