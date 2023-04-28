# Recursion Algorithms

## Introduction

Recursion is a technique used in programming to solve problems by breaking them down into smaller subproblems. Recursion involves calling a function within itself to solve a problem, and the function continues to call itself until it reaches a base case, which is the smallest possible subproblem that can be solved. Recursion can be used to solve a wide range of problems, from calculating factorial numbers to traversing tree structures.

## Characteristics of Recursion Algorithms

Recursion algorithms typically have the following characteristics:

1. Base case: The recursion algorithm must have a base case, which is the smallest possible subproblem that can be solved. When the base case is reached, the recursion stops and the solution is returned.

2. Recursive case: The recursive case is the step where the function calls itself to solve a smaller subproblem. The recursive case must move towards the base case, otherwise the recursion will continue indefinitely and cause a stack overflow error.

## Examples of Recursion Algorithms

The following are some examples of recursion algorithms:

1. Factorial Function: The factorial function is a classic example of a recursion algorithm. To calculate the factorial of a number, we recursively multiply the number by the factorial of the number minus one, until we reach the base case of one.

2. Binary Search: Binary search is a search algorithm used to find a specific value in a sorted array. The algorithm recursively divides the array in half, discarding the half that does not contain the value being searched for, until it reaches the base case of a single element array.
    <div align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Binary-search-work.gif/220px-Binary-search-work.gif">
        <p>Visualization of the binary search algorithm where 9 is the target value</p>
    </div>

## Performance Characteristics

Recursion algorithms can be evaluated based on their time complexity and space complexity. The time complexity of a recursion algorithm depends on the number of recursive calls and the time required to solve each subproblem. The space complexity of a recursion algorithm depends on the maximum depth of the call stack and the amount of memory required to store the solutions to each subproblem.

## Conclusion

Recursion is a powerful technique used in programming to solve problems by breaking them down into smaller subproblems. Recursion algorithms typically have a base case and a recursive case, and can be used to solve a wide range of problems. When evaluating recursion algorithms, it's important to consider their time and space complexity, as well as their base case and recursive case.