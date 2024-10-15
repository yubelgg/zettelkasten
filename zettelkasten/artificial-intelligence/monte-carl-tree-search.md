---
id: monte-carl-tree-search
aliases: []
tags: []
---

# Monte Carlo Tree Search (MCTS)

MCTS combines two important ideas:

- evaluation by payout - play multiple games to termination from state s
- selective search - explore parts of tree that will improve decision at root

### MCTS version 0

- do **N** playouts from each child of the root
- pick move that give best outcome

### MCTS version 0.9

also need selection policy.

- exploitation: allocate playouts to promising nodes

### MCTS version 1

adds:

- exploitation: allocate playouts to uncertain nodes

### MCTS version 2

Repeat until **timeout**:

- select: given current search tree, recursively apply **selection policy** to leave
- expand: add new child c to n
- simulate: run N playouts from c
- backpropagation: update win counts from c back to root

Choose action leading to child with highest N (number of playouts)
