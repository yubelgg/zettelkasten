---
id: probability-review
aliases: []
tags: []
---

# Probability Review

## Basic Probability Concepts

### Sample Space and Events

- Sample Space ($S$ or $\Omega$): Set of all possible outcomes
- Event ($E$): Subset of sample space
  Example:
  $$ S = \{1,2,3,4,5,6\} \text{ for a die roll} $$
$$ E = \{2,4,6\} \text{ for even numbers} $$

### Probability Axioms

1. Non-negativity: $P(E) \geq 0$
2. Normalization: $P(S) = 1$
3. Additivity: For disjoint events $A$ and $B$:
   $$ P(A \cup B) = P(A) + P(B) $$

### Basic Probability Rules

$$ P(\emptyset) = 0 $$
$$ P(E^c) = 1 - P(E) $$
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

### Definition

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$

Example:
Given two cards drawn without replacement:
$$ P(\text{second ace}|\text{first ace}) = \frac{3}{51} $$

### Multiplication Rule

$$ P(A \cap B) = P(A|B)P(B) = P(B|A)P(A) $$

### Bayes' Theorem

$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$

Example:
Example (Medical Test):

- $P(Disease) = 0.01$ (1% have the disease)
- $P(Test+|Disease) = 0.95$ (95% sensitivity)
- $P(Test+|No Disease) = 0.10$ (10% false positive)
  $$ P(Disease|Test+) = \frac{0.95 \cdot 0.01}{0.95 \cdot 0.01 + 0.10 \cdot 0.99} \approx 0.088 $$

### Law of Total Probability

For partition $B_1, B_2, ..., B_n$:
$$ P(A) = \sum\_{i=1}^n P(A|B_i)P(B_i) $$

Example (Email Classification):
$$ P(\text{contains "free"}) = P(\text{"free"}|\text{spam})P(\text{spam}) + P(\text{"free"}|\text{not spam})P(\text{not spam}) $$
$$ = 0.60 \cdot 0.30 + 0.05 \cdot 0.70 = 0.215 $$

### Independence

Events $A$ and $B$ are independent if:
$$ P(A \cap B) = P(A)P(B) $$

Example (Two Dice):
$$ P(\text{first die = 6 and second die = 6}) = P(\text{first = 6})P(\text{second = 6}) $$
$$ = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36} $$

## Chain Rule in Probability

### Basic Chain Rule

For any events $A_1, A_2, ..., A_n$:
$$ P(A*1 \cap A_2 \cap ... \cap A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1 \cap A_2)...P(A_n|A_1 \cap A_2 \cap ... \cap A*{n-1}) $$

### Simple Example (2 Events)

Drawing cards without replacement:
$$ P(\text{two aces}) = P(\text{first ace})P(\text{second ace}|\text{first ace}) $$
$$ = \frac{4}{52} \cdot \frac{3}{51} = \frac{12}{2652} $$

### Extended Example (3 Events)

Drawing three aces without replacement:
$$ P(\text{three aces}) = P(A_1)P(A_2|A_1)P(A_3|A_1 \cap A_2) $$
$$ = \frac{4}{52} \cdot \frac{3}{51} \cdot \frac{2}{50} = \frac{24}{132600} $$
