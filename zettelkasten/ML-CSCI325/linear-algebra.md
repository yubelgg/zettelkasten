---
id: linear-algebra
aliases: []
tags: []
---

# linear algebra

## unit vector

A unit vector is a vector with a magnitude (length) of exactly 1.

## Mathematical Definition

For a vector $\vec{v}$, if $\|\vec{v}\| = 1$, then $\vec{v}$ is a unit vector.

## How to Create a Unit Vector

To create a unit vector from any non-zero vector $\vec{v}$, you normalize it by dividing by its magnitude:

$\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$

## Examples

### 2D Example

For vector $\vec{v} = [3, 4]$:

1. Calculate magnitude: $\|\vec{v}\| = \sqrt{3^2 + 4^2} = 5$
2. Normalize: $\hat{v} = [\frac{3}{5}, \frac{4}{5}] = [0.6, 0.8]$

### 3D Example

For vector $\vec{v} = [2, 2, 1]$:

1. Calculate magnitude: $\|\vec{v}\| = \sqrt{2^2 + 2^2 + 1^2} = 3$
2. Normalize: $\hat{v} = [\frac{2}{3}, \frac{2}{3}, \frac{1}{3}]$

## Common Unit Vectors

- $\hat{i} = [1, 0]$ or $[1, 0, 0]$ (x-axis)
- $\hat{j} = [0, 1]$ or $[0, 1, 0]$ (y-axis)
- $\hat{k} = [0, 0, 1]$ (z-axis)

## Properties

1. Length is always 1
2. Direction is preserved from original vector
3. Used for indicating direction without magnitude
4. Important in machine learning for:
   - Normalization
   - Feature scaling
   - Directional calculation
