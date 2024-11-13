---
id: reinforcement-learning
aliases: []
tags: []
---

# Reinforcement Learning

Basic Idea:
![[reinforcement learning.png]]

- receives feedback in form of rewards
- agent's [[utility]] is defined by reward function
- must (learn to) act to **maximize expected rewards**
- all learning is based on observed sample of outcomes

Still assume [[MDP]]:

- states
- actions
- transition model
- reward function
- policy pi(s)

New twist is that T and R are **unknown**

## Model Based Learning

Model-based: learn the model, solve it, execute the solution
Model-free (values-based): learn values from experience, make decisions on that

- direct evaluation
- temporal difference learning
- Q-learning
  model-free (policy-based): learn policies directly

![[model based learning.png]]
