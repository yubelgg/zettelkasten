---
id: local-search
aliases: []
tags: []
---

# Local Search

In many search and optimization problem the **path** is irrelevant, only care about the goal.

Iterative Improvement Algorithms:

- start with initial state n$_0$
- each step t, improve by choosing "better" state n$_{t+1}$
- requires the **evaluation** or **cost** function h(n)
- no search tree needed
- constant memory

## Hill Climbing

General type of iterative improvement algorithm

- start anywhere (random or given)
- repeat: move to the best neighbor (based on evaluation or cost function h(n))
- no neighbor that are better, terminate
- no backtracking, no memory, local maxima (suboptimal solution), limited exploration

## Local Beam Search

Local Beam Search:
compromise between **local** search (no storage) and **complete** search like A\* (storing all explored states).

Each iteration:

- generate all successors from **K** current states
- choose best **K** of these for new current state, or
- choose **K** states randomly with "better" states more highly weighted
