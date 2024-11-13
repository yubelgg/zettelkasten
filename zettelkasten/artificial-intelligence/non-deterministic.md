---
id: non-deterministic
aliases: []
tags: []
---

# Non-Deterministic

randomness can decide what happens next

![[non-deterministic.png]]

## Markov Decision Processes

For non-deterministic search problems:

- **action outcomes** only depend on **current state**

Transition function **T(s, a, s')**
same as P(s'| s, a)

- s = current state
- a = action
- s' = state you land on

## Policies

For **[[MDP]]**, optimal policy pi\*: S -> A:

- maps states to actions
- optimal policy is one that maximizes [[policy]]
- an explicit policy defines a [[agents#Reflex Agents|reflex agent]]

**(s, a) is a q-state**

Each MDP state creates an **expectimax-like** search tree

### Discounting

worth now = 1
worth next step = gamma (0, 1)
worth next two steps = gamma$^2$ (0, 1)

Having a gamma will help us find a solution, it converges

![[discounting.png]]

### Infinite Utilities

Bound the horizon to a finite horizon

- terminate episode after fixed T steps
- give **non-stationary** policies: pi(s) -> pi(s, time left)

## Optimal Quantities

**value(utility)** of a state s:
V\*(s) = expected utility starting in s and acting optimally.

**value(utility)** of a q-state(s,a):
q\*(s,a) = expected utility starting out having taken an action a from state s and acting optimally.

![[value of states.png]]

## Depth Limited Expectimax

Lots of repeated work
Think of this as a graph and cache it or do bottom up dp
Doesn't matter if tree goes on infinite depth since rewards decrease, so stop at some depth.

### Value Iteration

**Repeat** until convergence
![[value iteration.png]]
