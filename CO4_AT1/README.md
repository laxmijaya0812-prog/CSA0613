# CO4_AT1 – Design and Analysis of Algorithms

## Student Information

* **Course:** Design and Analysis of Algorithms
* **Assessment:** CO4_AT1
* **Question:** Job Scheduling with Deadlines

## Overview

This repository contains the implementation and analysis of the Job Scheduling with Deadlines problem using a Greedy algorithm.

The objective is to schedule jobs with given deadlines and profits so that the total profit is maximized while ensuring that each selected job is completed before its deadline.

## Problem

Each job has:

* A unique job ID
* A deadline
* A profit
* A processing time of one unit

Only one job can be scheduled at a time. The algorithm selects jobs based on their profit and assigns them to available time slots before their deadlines.

## Algorithm Used

**Greedy Job Scheduling with Deadlines**

The algorithm:

1. Sorts jobs in decreasing order of profit.
2. Finds the latest available slot before each job's deadline.
3. Schedules the job if a suitable slot is available.
4. Calculates the total profit.

## Sample Input

```text
n = 4
deadline = 2 1 2 1
profit = 100 19 27 25
```

## Expected Output

```text
Scheduled Jobs: J3 J1
Max Profit = 127
```

## Complexity

* **Sorting:** O(n log n)
* **Scheduling:** O(n × d)
* **Overall:** O(n log n + n × d)
* **Space Complexity:** O(d)

where `n` is the number of jobs and `d` is the maximum deadline.

## Learning Outcomes

* Understand the Greedy algorithmic strategy.
* Solve optimization problems using greedy selection.
* Implement job scheduling with deadlines.
* Analyze time and space complexity.
* Understand how deadlines and profits affect scheduling decisions.

## Software Requirements

* Python 3.x
* Visual Studio Code, PyCharm, IDLE, or any Python IDE

## How to Run

1. Open the Python source-code file.
2. Run the program using Python 3.
3. Enter or use the provided job deadlines and profits.
4. Observe the scheduled jobs and maximum profit.

## Author

**Name:** Lakshmi Devi J
