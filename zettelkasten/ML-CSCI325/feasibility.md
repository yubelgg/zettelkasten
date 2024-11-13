---
id: feasibility
aliases: []
tags: []
---

# feasibility of learning

whether it is possible for a machine learning system to learn from the data given and achieve its goal.

### sample complexity

how many sample are needed for reliable learing?

## Standard Hoeffding's Inequality:

$\mathbb{P}[|\nu-\mu| > \epsilon] \leq 2\exp(-2\epsilon^2N)$

- $\mathbb{P}$ = $P$ (both mean probability)
- $\nu$ = $\hat{\mu}$ (both represent sample mean)
- $\mu$ = $\mu$ (both represent true population mean)
- $N$ = $n$ (both represent sample size)
- $\exp$ = $e$ (both represent exponential function)
- $\epsilon$ = $\epsilon$ (both represent error tolerance)

## Key Insights:

1. Trade-offs:

   - Larger N ➡️ Better accuracy but more cost/time
   - Smaller ε ➡️ More precision but needs larger N
   - Higher confidence ➡️ Needs larger N

2. Diminishing Returns:

   - Doubling N doesn't double accuracy
   - Following square root relationship

3. Practical Uses:
   - Sample size determination
   - Confidence interval calculation
   - Error bound estimation

### $E_{in}$ and $E_{out}$

in sample error ($E_{in}(h)$)

- error rate on training data
- data we use to train the model
- what we can actually measure
- like testing marbles

out of sample error ($E_{out}(h)$)

- error rate on unseen data
- true error in the real world
- what we care about
- like predicting marbles still in the bin
