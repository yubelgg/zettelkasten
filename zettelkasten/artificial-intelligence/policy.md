---
id: policy
aliases: []
tags: []
---

# Policy

Policy tells us for any possible situation we have encounter, what is the right thing to do is.

Policy evaluation: value function for a policy

$$
v_{i+1}^{\pi_k}(s) \leftarrow \sum_{s'} P(s, \pi_k(s), s') [r(s, \pi_k(s), s') + \gamma v_i^{\pi_k}(s')]
$$

Policy improvement: best action for v$^{\pi_k}$(.) via one step lookahead

$$
\pi_{k+1}(s) \leftarrow \arg\max_a \sum_{s'} P(s, a, s') [r(s, a, s') + \gamma v_i^{\pi_k}(s')]
$$
