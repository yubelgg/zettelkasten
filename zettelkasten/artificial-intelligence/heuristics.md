---
id: heuristics
aliases: []
tags: []
---

# Heuristics

A heuristics function that estimates how close a state is to a goal.

- designed for a particular search problem

## Admissibility

An inadmissible heuristic breaks optimality by trapping the good plan on the frontier/queue.
An admissible heuristic slow down bad plans but never outweight true costs.

Heuristics **h** is **admissible** if:

$$
0 \leq h(n) \leq h^*(n)
$$

where:

- h\*(n) is the actual cost to nearest goal

**Search Heuristics** is a function `h(n)` that estimates how close a state n is to a goal.

- designed for particular searh problem
- pathfinding examples:
  - manhattan distance
  - Euclidean distance

## Creating admissible Heuristics

Creating an admissible heuristic involving the use of relaxed problems.

- relaxed problem:
  - less constrained than the original problem
  - easier to solve
  - often easier to find an admissible heuristic
  - e.g. Pathfinding:
    - original problem: agent can move horizontally or vertically
    - relaxed problem: agent can move diagonally
    - impact: diagonal moves reduce distance to goal, providing lower bound for actual cost
  - e.g. 8-puzzle:
    - original problem: move a tile to a goal state
    - relaxed problem: move a tile to an adjacent space
    - impact: provides optimistic estimate of moves

### Combining Heuristics

$$
h(n) = \max(h_1(n), h_2(n))
$$


