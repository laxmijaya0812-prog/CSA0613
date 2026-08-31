# Exact Cover Problem – Design and Analysis of Algorithms

## Overview

This project implements the Exact Cover Problem using a Backtracking algorithm.

The Exact Cover Problem is a constraint satisfaction problem in which a collection of subsets is given, and the objective is to select subsets such that every element in the universe is covered exactly once.

## Problem Definition

Given:

* A universe containing a set of elements.
* A collection of subsets.

Find a selection of subsets satisfying:

1. Every element must be covered.
2. Every element must be covered exactly once.
3. Selected subsets must not overlap.

## Algorithm Used

**Backtracking with Pruning**

The algorithm:

1. Selects an uncovered element.
2. Finds possible subsets containing that element.
3. Rejects overlapping subsets.
4. Recursively explores valid selections.
5. Backtracks when a selection cannot produce an Exact Cover.

## Constraints

### Coverage Constraint

All elements in the universe must be included in the selected subsets.

### Exclusivity Constraint

No element can occur in more than one selected subset.

## Pruning

Subsets that overlap with already covered elements are immediately rejected.

This reduces unnecessary exploration and improves practical efficiency.

## Example

### Universe

```text
{1, 2, 3, 4, 5}
```

### Exact Cover

```text
{1, 2}
{3}
{4, 5}
```

All elements are covered exactly once.

## Complexity

* **Time Complexity:** O(2^m)
* **Space Complexity:** O(m + n)

Where:

* `m` is the number of subsets.
* `n` is the number of elements.

## Concepts Covered

* Backtracking
* Constraint Satisfaction
* Exact Cover
* NP-Complete Problems
* Pruning
* Recursive Algorithms
* Complexity Analysis

## Software Requirements

* Python 3.x
* Visual Studio Code / PyCharm / IDLE

## How to Run

1. Open the Python source code file.
2. Run the program using Python 3.
3. Observe the Exact Cover solution.
4. Verify that every element is covered exactly once.

## Course

**Design and Analysis of Algorithms**

## Author

**Name:** Lakshmi Devi J
