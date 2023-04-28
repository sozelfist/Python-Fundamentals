# Red Black Tree

A red-black tree is a type of self-balancing binary search tree that is used to maintain a sort of a balance between the height of the tree. The balance is achieved by assigning a color to each node of the tree, either red or black.

1. Each node is either red or black: This is the first property of the tree, and it ensures that the tree is well-formed.

2. The root is always black: This is the second property of the tree, and it ensures that the tree is well-formed.

3. All leaves (NIL) are black: This is the third property of the tree, and it ensures that the tree is well-formed.

4. If a node is red, then both its children are black: This is the fourth property of the tree, and it ensures that the tree is well-formed.

5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes: This is the fifth and most important property of the tree, and it ensures that the tree is balanced. The number of black nodes on any given path is called the black-height of the node. The black-height of the root is the black-height of the entire tree.

The first, second, third and fourth properties ensure that the tree is well-formed, and the fifth property ensures that the tree is balanced.

During the insertion and deletion, if the tree is not following the properties, then the tree is re-balanced using different rotations such as left-rotation, right-rotation, left-right-rotation, and right-left-rotation.

Red-black trees have an average time complexity of $O(\log{n})$ for most operations like searching, inserting and deleting. This makes it a good choice when the number of elements in the tree is large, and the elements need to be frequently added or removed.

<div align="center">
    <p><b>Example of a red–black tree</b></p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Red-black_tree_example_with_NIL.svg/316px-Red-black_tree_example_with_NIL.svg.png">
    <p>
        A directed graph with three vertices (blue circles) and three edges (black arrows).
    </p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Red-black_tree_example_with_sockets.svg/316px-Red-black_tree_example_with_sockets.svg.png">
    <p>
        A directed graph with three vertices (blue circles) and three edges (black arrows).
    </p>
</div>

For more information, see :heart: [Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

## Implementation

The `RedBlackTree` class is implemented at [red_black_tree.py](../../data_structures/red_black_tree.py)

## Explanation

The implementation is clean and optimized, it uses sentinel nodes to simplify the implementation and it doesn't use unnecessary rebalancing when it's not needed after deletion. It also uses helper methods such as `transplant`, `left_rotate`, `right_rotate`, `insert_fixup` and `delete_fixup` to maintain the red-black tree's properties.