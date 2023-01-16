# Disjoint Set

## Implementation

The `DisjointSet` is implemented here [disjoint_set.py](../../data_structures/disjoint_set.py)

## Explaination

This is an implementation of the disjoint-set data structure, also known as a union-find data structure. It is used to keep track of a partition of a set into disjoint subsets.

The `DisjointSet` class has three methods: `make_set`, `find_set`, and `union`.

- `make_set(x)` creates a new set whose only member (and thus representative) is `x`. It also initializes the rank of `x` to 0. The `parent` and `rank` dictionaries are used to keep track of the parent and rank of each element.

- `find_set(x)` returns the representative of the set containing `x`. It uses path compression which flattens the tree structure of the disjoint-set in order to improve the performance.

- `union(x, y)` joins the two sets containing x and y into a single set. It uses union by rank in order to make sure that the resulting tree structure is balanced.

The class also includes several test cases that check the functionality of the implemented methods. The `setUp()` method initializes an instance of the `DisjointSet` class, and the test methods use this instance to test the functionality of the class.
