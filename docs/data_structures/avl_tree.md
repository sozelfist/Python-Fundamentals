# AVL Tree

Sure, AVL trees were the first self-balancing trees to be invented. They were invented by Adelson-Velsky and Landis in 1962.

An AVL tree is a binary search tree with a balance condition. The balance condition is that the difference in the heights of the left and right subtrees of any node in the tree cannot be more than 1. This condition is called the AVL property. If the tree becomes unbalanced, then the tree is re-balanced using one of the following tree rotations:

- Left-Left Rotation
- Left-Right Rotation
- Right-Left Rotation
- Right-Right Rotation

AVL trees are widely used in applications that require searching, insertion, and deletion of elements in a data set with a large number of elements. These operations are performed in $O(\log{n})$ time in AVL trees, where n is the number of nodes in the tree. This is because the height of an AVL tree is always $O(\log{n})$.

AVL tree is also commonly used in databases, file systems, and operating systems for efficient memory management. They are also used in many other applications such as IP routers, and real-time systems, etc.

In short, AVL tree is a self-balancing binary search tree that provides an efficient way to maintain a data set with a large number of elements, and it provides a good balance between time and space complexity.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/AVL_Tree_Example.gif/220px-AVL_Tree_Example.gif">
    <p>Animation showing the insertion of several elements into an AVL tree. It includes left, right, left-right and right-left rotations.</p>
</div>

## Complexities in big O notation

### Space complexity

| Space | $\Theta(n)$ |
| ----- | ----------- |

### Time complexity

| **Function** | **Amortized**     | **Worse Case** |
| ------------ | ----------------- | -------------- |
| **Search**   | $\Theta(\log{n})$ | $O(\log{n})$   |
| **Insert**   | $\Theta(\log{n})$ | $O(\log{n})$   |
| **Delete**   | $\Theta(\log{n})$ | $O(\log{n})$   |
## Implementation

The `AVLTree` class is implemented at [avl_tree.py](../../data_structures/avl_tree.py)

## Explanation

The implementation of AVL tree includes the basic operations such as insertion, left and right rotations and it also keeps track of the height of each node, which is used to check the balance of the tree.

- The `insert` method is the main method for inserting a new key into the tree. It calls the `_insert` method which recursively finds the correct position for the new key in the tree and then checks the balance of the tree after the insertion. If the tree is unbalanced, it performs the appropriate rotation to balance the tree.
- The `left_rotate` and `right_rotate` methods are used to rotate the tree when a node becomes unbalanced. The `get_height` and `get_balance` methods are used to calculate the height and balance of a given node.
- `search(key: int) -> Union[Node, None]`: This method can be used to search for a key in the tree and return the corresponding node if it exists. It can be implemented using a similar approach as the `_insert` method, recursively traversing the tree until the key is found or a leaf is reached.
- `delete(key: int) -> None`: This method can be used to delete a key from the tree. It can be implemented by first searching for the key in the tree, then finding the inorder successor or predecessor to replace the key and then balancing the tree if necessary.
- `inorder_traversal() -> List[int]`: This method can be used to return a list of all the keys in the tree in inorder traversal (left subtree -> root -> right subtree) order. It can be implemented using recursion and a list to store the keys.
- `preorder_traversal() -> List[int]`: This method can be used to return a list of all the keys in the tree in preorder traversal (root -> left subtree -> right subtree) order. It can also be implemented using recursion and a list to store the keys.
- `postorder_traversal() -> List[int]`: This method can be used to return a list of all the keys in the tree in postorder traversal (left subtree -> right subtree -> root) order. It can also be implemented using recursion and a list to store the keys.

## Test cases

The test case class includes test methods for the `insert`, `search`, `delete`, `inorder_traversal`, `preorder_traversal`, and `postorder_traversal` functionalities of the `AVLTree` class. Each test method first creates a new `AVLTree` object and inserts some keys into it, then it performs the corresponding operation and compares the output with the expected result using the `assertEqual` method.