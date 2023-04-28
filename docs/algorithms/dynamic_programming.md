# Dynamic Programming Algorithms

## Introduction

Dynamic programming is a technique used to solve problems by breaking them down into smaller, simpler subproblems and solving each subproblem only once. Dynamic programming algorithms are often used to solve optimization problems, where the goal is to find the best solution among many possible solutions.

## Characteristics of Dynamic Programming Algorithms

Dynamic programming algorithms typically have the following characteristics:

- Optimal Substructure: A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property allows us to solve the problem recursively by breaking it down into smaller subproblems.

- Overlapping Subproblems: A problem has overlapping subproblems if it can be broken down into smaller subproblems that are solved repeatedly. This property allows us to avoid redundant calculations by storing the solutions to subproblems in a table and reusing them as needed.

## Examples of Dynamic Programming Algorithms

The following are some examples of dynamic programming algorithms:

1. Fibonacci Sequence: The Fibonacci sequence is a classic example of a problem that can be solved using dynamic programming. Each number in the sequence is the sum of the two preceding numbers, so we can solve for each number in the sequence recursively by summing the two preceding numbers. However, this approach results in redundant calculations, so we can use dynamic programming to avoid this by storing the solutions to subproblems in a table and reusing them as needed.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Fibonacci_Spiral.svg/300px-Fibonacci_Spiral.svg.png">
        <p>The Fibonacci spiral: an approximation of the golden spiral created by drawing circular arcs connecting the opposite corners of squares in the Fibonacci tiling.</p>
    </div>

2. Knapsack Problem: The knapsack problem is a classic optimization problem that can be solved using dynamic programming. Given a set of items with weights and values, we want to find the subset of items that maximizes the total value while keeping the total weight within a certain limit. We can solve this problem using dynamic programming by breaking it down into smaller subproblems and storing the solutions to each subproblem in a table.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Knapsack.svg/250px-Knapsack.svg.png">
        <p>Example of a one-dimensional (constraint) knapsack problem.</p>
    </div>

## Performance Characteristics

Dynamic programming algorithms can be evaluated based on their time and space complexity. The time complexity of a dynamic programming algorithm depends on the number of subproblems and the time required to solve each subproblem. The space complexity of a dynamic programming algorithm depends on the number of subproblems and the amount of memory required to store the solutions to each subproblem.

## Conclusion

Dynamic programming is a powerful technique used to solve problems by breaking them down into smaller, simpler subproblems and solving each subproblem only once. Dynamic programming algorithms are often used to solve optimization problems, where the goal is to find the best solution among many possible solutions. When evaluating dynamic programming algorithms, it's important to consider their time and space complexity, as well as their optimal substructure and overlapping subproblems properties.