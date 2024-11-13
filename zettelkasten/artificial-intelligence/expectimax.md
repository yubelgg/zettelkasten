---
id: expectimax
aliases: []
tags: []
---

# Expectimax Search

Expectimax is a decision making algorithm that involves randomness.
Taking a chance for example in pacman that the ghost moves away and you win the game instead of instantly killing yourself.

It computes the average score under the optimal play.

Values should be **average case** (expectimax), not the **worst case** (minimax).

```python
def value(state):
    if the state is a terminal state: return the state’s utility
    if the next agent is MAX: return max-value(state)
    if the next agent is EXP: return exp-value(state)
```

```python
def max-value(state):
    initialize v = -∞
    for each successor of state:
            v = max(v, value(successor))
    return v
```

```python
def max-value(state):
    initialize v = 0
    for each successor of state:
            p = proability(successor)
            v += p * value(successor)
    return v
```

You cannont pruning with expectimax since you could have a really large number making the average better for the max.

### Probability

In expectimax search, probability model of the opponent or environment:

- model can have a simple unform distribution (roll a dice)
- model can be sophisticated and require lots of computation

### Optimism and Pessimism

Dangerous optimism assume change when world is adversarial
Dangerous pessimism assume the worst case when its not likely to happen.
