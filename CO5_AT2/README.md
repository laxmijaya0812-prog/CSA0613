# CO5_AT2 – Design and Analysis of Algorithms

## Student Information

* **Course:** Design and Analysis of Algorithms
* **Assessment:** CO5_AT2
* **Question:** Graph Partition Problem Using Backtracking

## Overview

This repository contains the implementation and analysis of the Graph Partition Problem using the Backtracking algorithm.

The objective is to partition the vertices of a graph into two equal-sized subsets. The algorithm systematically assigns vertices to either partition and uses pruning to eliminate invalid assignments.

## Problem Description

Given a graph with an even number of vertices, divide its vertices into two subsets such that:

* Every vertex belongs to exactly one subset.
* Both subsets contain an equal number of vertices.
* Invalid partitions are eliminated using pruning.
* All valid possibilities can be explored using Backtracking.

## Algorithm Used

**Backtracking with Pruning**

The algorithm:

1. Assigns each vertex to one of two sets.
2. Maintains equal-size constraints.
3. Recursively explores possible assignments.
4. Backtracks when an assignment cannot lead to a valid solution.
5. Uses pruning to reduce unnecessary computation.

## Input

The graph is represented using an adjacency matrix.

Example:

```text
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
```

## Output

Example partition:

```text
Set A: [0, 1]
Set B: [2, 3]
```

## Complexity

* **Time Complexity:** O(2ⁿ)
* **Space Complexity:** O(n)

## Pruning

Branches are eliminated when either partition exceeds the required size. This reduces unnecessary recursive exploration.

## Software Requirements

* Python 3.x
* Visual Studio Code / PyCharm / IDLE

## How to Run

1. Open the Python source code.
2. Run the program using Python 3.
3. Observe the generated graph partitions.
4. Verify that both subsets contain an equal number of vertices.

## Learning Outcomes

* Understand the Backtracking algorithm.
* Apply recursive problem-solving techniques.
* Use pruning to improve search efficiency.
* Analyze exponential-time algorithms.
* Solve combinatorial optimization problems.

## Author

**Name:** Lakshmi Devi J
