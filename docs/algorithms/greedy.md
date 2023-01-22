# Greedy Algorithms

Greedy algorithms are a type of algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. The local optimal choices made by a greedy algorithm are used to construct a global solution that is also optimal.

A greedy algorithm always makes the choice that looks best at the moment. That is, it makes a locally optimal choice in the hope that this choice will lead to a globally optimal solution.

Some common examples of problems that can be solved using greedy algorithms include:

- Huffman Encoding
- Dijkstra's Algorithm for finding the shortest path
- Prim's Algorithm for finding the minimum spanning tree
- Kruskal's Algorithm for finding the minimum spanning tree
- Coin Change problem
- Fractional Knapsack problem

1. **Huffman Encoding**: This algorithm is used for compressing data by assigning variable-length codes to characters, such that more frequent characters have shorter codes. It is based on the idea of a greedy algorithm that builds a prefix tree from the bottom up, always adding the least frequent item as a child of the two most frequent items.

2. **Dijkstra's Algorithm**: This algorithm is used to find the shortest path between two nodes in a graph. It works by maintaining a priority queue of unvisited nodes and always visiting the node with the smallest distance first.

3. **Prim's Algorithm**: This algorithm is used to find the minimum spanning tree of a graph. It starts with an arbitrary node, and at each step, adds the edge with the smallest weight that connects the current tree to a new node.

4. **Kruskal's Algorithm**: This algorithm is used to find the minimum spanning tree of a graph. It starts with an empty tree and at each step, adds the edge with the smallest weight that connects two different connected components.

5. **Coin Change problem**: Given a set of coins and amount, Write an algorithm to find out how many ways we can make the change of the amount using the coins given.

6. **Fractional Knapsack problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

It is important to note that not all problems have globally optimal solutions that can be constructed by making locally optimal choices, and greedy algorithms are not always able to find the optimal solution for a given problem. In some cases, a greedy algorithm may produce a suboptimal solution, and it is important to consider other algorithmic approaches when solving a problem.