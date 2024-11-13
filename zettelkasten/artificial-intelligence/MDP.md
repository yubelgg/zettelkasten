---
id: MDP
aliases: []
tags: []
---

# MDP

Decision making in situations where outcomes are partly random and partly under the control of an agent.

Policy = map of states to actions
Utility = sum of discounted rewards
Values = expected future utility from a state (max node)
Q-Values = expected future utility from q-state (chance node)

# Bellman Equation

$$
V^{*}(s) = \max_{a \in A} \sum_{s'} T(s,a,s')(R(s,a,s') + \gamma V^{*}(s'))
$$

The optimal value of a state is the maximum expected sum of:

1. Immediate reward
2. Discounted future value

Calculated over all possible actions and resulting states.

Key components:

- $V^{*}(s)$: Optimal value of state $s$
- $\max_{a \in A}$: Best action choice
- $T(s,a,s')$: Transition probability
- $R(s,a,s')$: Immediate reward
- $\gamma$: Discount factor
- $V^{*}(s')$: Future state value

## Value Iteration

$$
k_{k+1}(s)  V^{*}(s) = \max_{a \in A} \sum_{s'} T(s,a,s')(R(s,a,s') + \gamma V_k(s'))
$$

![[value iteration.png]]
![[value iteration example.png]]

### Policy Methods

Fixed Policies:

- pi(s) tells us what action to take.
