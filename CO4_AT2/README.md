# CO4_AT2 – Design and Analysis of Algorithms

## Student Information

* **Course:** Design and Analysis of Algorithms
* **Assessment:** CO4_AT2
* **Question:** Ride-Sharing Matching System Optimization

## Overview

This repository contains the implementation of a Ride-Sharing Matching System using Bipartite Graph Matching.

The system models drivers and passengers as two separate sets of vertices in a bipartite graph. An edge represents a possible match between a driver and a passenger based on conditions such as driver availability and location proximity.

The objective is to maximize the number of successful driver-passenger assignments.

## Algorithm Used

**Bipartite Graph Matching using Depth First Search (DFS)**

The algorithm:

1. Represents drivers and passengers as graph vertices.
2. Creates edges for valid driver-passenger matches.
3. Searches for augmenting paths using DFS.
4. Assigns each passenger to at most one driver.
5. Maximizes the total number of matches.

## Constraints Considered

* Driver availability
* Passenger demand
* Location proximity
* One-to-one driver-passenger matching
* Real-time response requirements

## Complexity

### DFS-Based Bipartite Matching

* **Time Complexity:** O(V × E)
* **Space Complexity:** O(V)

### Optimized Approach

For large datasets, the Hopcroft-Karp algorithm can achieve:

* **Time Complexity:** O(E√V)

## Sample Result

```text
D1 → P1
D2 → P2
D3 → P3

Maximum Number of Matches = 3
```

## Software Requirements

* Python 3.x
* Visual Studio Code / PyCharm / IDLE

## How to Run

1. Open the source code file.
2. Run the program using Python 3.
3. Observe the driver-passenger matching results.
4. Analyze the maximum number of successful matches.

## Learning Outcomes

* Understand Bipartite Graphs.
* Apply Graph Matching algorithms.
* Analyze algorithmic complexity.
* Study scalability in real-time systems.
* Understand optimization techniques for large-scale matching systems.

## Author

**Name:** Lakshmi Devi J
