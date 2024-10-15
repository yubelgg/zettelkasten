---
id: agents
aliases: []
tags: []
---

# Agent

An agent is an entity that perceives and acts.

A **rational agent** selects actions that maximizes its (expected) **[[utility]]**.

Selecting rational actions:

- percepts
- environment
- action space

## Rational Agent design

- Observability: sensors withs relevant information
- number of agents

- determinism: next state is determined by current state and action
  ^test

- dynamism: does environment change when agent is making decision?
- Episodic vs. sequential:
  - episodic: each action is independent of previous actions, doesn't remember previous actions
    - e.g. spam filtering, without considering previous emails
  - sequential: continuous stream of percepts and actions, remembers previous actions and uses them to make decisions
    - e.g. chess as each move influences future moves
- discrete vs continuous

## Reflex Agents

Reflex agents choose actions based on current precept.

- agents input or observation, through sensors

May need memory and a model of the environment's current state.
Does not consider future consequences of their actions.

Reflex agent can be rational if:

- environment is **fully observable**
- environment is **deterministic**
- environment is **static**

## Planning Agents

Makes decisions based on predicting the outcome without pior experience.
Must formulate a **goal(test)** and **[[utility]] (scoring) function** to determine
the best current action.