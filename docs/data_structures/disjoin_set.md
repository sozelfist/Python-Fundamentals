# Disjoint Set

A `Disjoint Set`, also known as Union-Find or Merge-Find, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides two main operations:

1. `Union(x, y)`: Merges the set containing element x with the set containing element y.

2. `Find(x)`: Returns the representative element of the set containing element x.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Dsu_disjoint_sets_init.svg/360px-Dsu_disjoint_sets_init.svg.png">
    <p><code>MakeSet</code> creates 8 singletons.</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Dsu_disjoint_sets_final.svg/360px-Dsu_disjoint_sets_final.svg.png">
    <p>After some operations of <code>Union</code>, some sets are grouped together.</p>
</div>

## Representation

The representative element of a set is one of its elements that is chosen to represent the set. The `Disjoint Set` data structure can be implemented using an array, where each element of the array represents a single element, and the value of the element points to the parent of the set to which it belongs. The representative element of a set is the root element of its corresponding tree.

Initially, each element is in its own set, and the value of the parent is set to itself. When two sets are merged, the root of one set is made the parent of the root of the other set. This ensures that all elements in the merged set share the same root.

## Applications

The Disjoint Set data structure is used in many algorithms, including Kruskal's algorithm for finding the minimum spanning tree of a graph and in image processing for connected component labeling. It has a time complexity of O(alpha(n)) for each operation, where alpha(n) is the inverse Ackermann function and grows very slowly, making the data structure very efficient in practice.

## Implementation

The `DisjointSet` is implemented here [disjoint_set.py](../../data_structures/disjoint_set.py)

## Explanation

This is an implementation of the disjoint-set data structure, also known as a union-find data structure. It is used to keep track of a partition of a set into disjoint subsets.

The `DisjointSet` class has three methods: `make_set`, `find_set`, and `union`.

- `make_set(x)` creates a new set whose only member (and thus representative) is `x`. It also initializes the rank of `x` to 0. The `parent` and `rank` dictionaries are used to keep track of the parent and rank of each element.

- `find_set(x)` returns the representative of the set containing `x`. It uses path compression which flattens the tree structure of the disjoint-set in order to improve the performance.

- `union(x, y)` joins the two sets containing x and y into a single set. It uses union by rank in order to make sure that the resulting tree structure is balanced.

The class also includes several test cases that check the functionality of the implemented methods. The `setUp()` method initializes an instance of the `DisjointSet` class, and the test methods use this instance to test the functionality of the class.
