# Dynamic Programming

Dynamic Programming (DP) is a method of solving problems by breaking them down into smaller subproblems, and storing the solutions to these subproblems to avoid redundant work. It is a powerful technique for solving complex problems that can be broken down into smaller overlapping subproblems.

DP problems can be broadly classified into two types:

- **Memoization**: This is also known as "top-down" approach, it starts from the original problem and then breaks it down into smaller subproblems. It stores the solutions of subproblems in a table so that they can be reused later, avoiding the need to recompute them.

- **Tabulation**: This is also known as "bottom-up" approach, it starts by solving all the subproblems first and then uses the solutions to solve the original problem. It stores the solutions of subproblems in a table and uses it to fill the remaining entries in the table to solve the original problem.

Some common examples of problems that can be solved using dynamic programming include:

- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Edit Distance
- Knapsack problem
- Matrix Chain Multiplication
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm
- Fibonacci sequence

1. **Longest Common Subsequence (LCS)**: This problem is to find the longest subsequence common to all sequences in a set of sequences (often just two).

2. **Longest Increasing Subsequence (LIS)**: This problem is to find the length of the longest increasing subsequence in a given array.

3. **Edit Distance**: This problem is to determine the minimum number of operations (insertions, deletions, and substitutions) needed to convert one string into another.

4. **Knapsack problem**: This problem is to find the most valuable set of items that fit in a knapsack of fixed capacity.

5. **Matrix Chain Multiplication**: This problem is to find the most efficient way to multiply a given sequence of matrices.

6. **Bellman-Ford Algorithm**: This algorithm is used to find the shortest path between two nodes in a graph with negative edge weights.

7. **Floyd-Warshall Algorithm**: This algorithm is used to find the shortest path between all pairs of vertices in a graph.

8. **Fibonacci sequence**: This problem is to find the nth Fibonacci number

Dynamic Programming is a powerful technique that can be used to solve a wide variety of problems, but it can also be difficult to implement and debug. It's important to have a good understanding of the problem and the underlying recursive structure in order to develop an efficient DP solution.