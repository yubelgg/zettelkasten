---
id: uninformed-search
aliases: []
tags: []
---

# Searching

Search Problem

- states
- actions and cost
- successor functions
- start and end state

Search Tree

- Nodes: states, Edges: actions
- path

Search Algorithm

- building the search tree
- chooing the order of unexplored nodes
- Optimal: always finding lowest cost (dijkstra's)
- Complete: always find a solution (if it exist)
  - dfs, complete but not optimal path
  - bfs, complete with optimal path with **actions** not **cost**

## Dijkstra's Algorithm

**strategy:** expand the cheapest node first
**implementation:** using a priority queue, keeping cumulative cost

## Uniformed Cost Search (UCS)

It is like BFS but it will take in cost into consideration.
Pros:

- UCS is complete and optimal!

Cons:

- explores options in every "direction"
- no information about the end location

What nodes does UCS expand?

- proccess all nodes with cost less than the cheapest colution
- solution cost C^\* and arcs cost at least E
- takes time O(b^d)

How much space does the frontier take?

- roughly the last tier. so O(b^d)

It is complete assuming best solution has finite cost and minimum arc cost is positive.

**Search Heuristics** is a function `h(n)` that estimates how close a state n is to a goal.

- designed for particular searh problem
- pathfinding examples:
  - manhattan distance (d1 = abs(x1-x2) + abs(y1-y2), given two points)
  - Euclidean distance

## Greedy Search

Expanding node that seems closest using **straight-line heuristic**.

- Computing the Heuristics function ahead of time.

Common Case:

- **Best-first** takes you to the goal but may not be optimal.
- **worst-case** it will act like DFS

## A\* search

Combines UCS and Greedy search

- uniformed-cost orders by path cost, or backward cost `g(n)`
- Greedy orders by goal proximity, or forward cost `h(n)`
- A\* search orders by the sum: `f(n) = g(n) + h(n)`
- enqueue should stop when we deque the **goal**
- it doesn't guarentee optimal solution
  - when we overestimate the cost
