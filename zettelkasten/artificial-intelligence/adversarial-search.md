---
id: adversarial-search
aliases: []
tags: []
---

# Adversarial Search

Policy tells us for any possible situation we have encounter, what is the right thing to do is.
^policy

This is more complex than just a sequence of actions.

Zero Sum Games

- agents have opposite [[utility]]
- [[utility]] is a single value that one **maximizes** and the other **minimizes**
- **Adversarial**

## Adversarial Search (Minimax)

Deterministic, zero-sum games:

- tic tac toe, chess, checkers
- one player maximizes, the other minimizes

```python
def max-value(state):
    initialize v = -inf
    for each successor of state:
        v = max(v, min-value(successor)
    return v
```

```python
def min-value(state):
    initialize v = inf
    for each successor of state:
        v = max(v, max-value(successor)
    return v
```

## Minimax efficency

- Same as [[bfs-dfs|dfs]]
- Time Complexity: O(b$^m$)
- Space Complexity: O(bm)

## Game Tree Pruning

Alpha-Beta Pruning

- maximizer with a child with value less than **v**, prune it
- minimizer with a child with value greater than **v**, prune it

```python
def max-value(state, α, β):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor, α, β))
        if v > β return v
        α = max(α, v)
    return v
```

```python
def min-value(state, α, β):
    initialize v = +∞
    for each successor of state:
        v = min(v, value(successor, α, β))
        if v < α return v
        β = min(β, v)
    return v
```
