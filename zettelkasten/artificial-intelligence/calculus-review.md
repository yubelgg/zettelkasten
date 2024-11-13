---
id: calculus-review
aliases: []
tags: []
---

Calculus Review

## Basic Derivatives

### Power Rule

$$ {\frac {d}{dx}(x^{n})} = n \cdot x^{n-1} $$

### Constant Rule

$$ \frac {d}{dx}(c) = 0 $$
$$ \frac {d}{dx}(cx) = c $$

### Product Rule

$$ \frac {d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x) $$
Example:
$$ \frac {d}{dx}(x^2 \cdot \sin x) = 2x\sin x + x^2\cos x $$

### Quotient Rule

$$ \frac {d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac {f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} $$

Example:
$$ \frac{d}{dx}\left(\frac{x^2}{\sin x}\right) = \frac{2x\sin x - x^2\cos x}{\sin^2 x} $$

### Chain Rule

$$ \frac {d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) $$
Example:
$$ \frac{d}{dx}\sin(x^2) = \cos(x^2) \cdot 2x $$

## Partial Derivatives

$$ \frac{\partial f}{\partial x} = \text{treat all variables except x as constants} $$
Example:
$$ f(x,y) = x^2y + xy^3 $$
$$ \frac{\partial f}{\partial x} = 2xy + y^3 $$
$$ \frac{\partial f}{\partial y} = x^2 + 3xy^2 $$

### Second Order Partials

$$ \frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) $$
Example:
$$ f(x,y) = x^2y + xy^3 $$
$$ \frac{\partial^2 f}{\partial x^2} = 2y $$

### Mixed Partials

$$ \frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y} $$
Example:
$$ f(x,y) = x^2y + xy^3 $$
$$ \frac{\partial^2 f}{\partial y \partial x} = 2x + 3y^2 $$

## Trigonometric Derivatives

### Basic Trig Derivatives

$$ \frac{d}{dx}(\sin x) = \cos x $$
Example:
$$ \frac{d}{dx}(\sin(2x)) = 2\cos(2x) $$

$$ \frac{d}{dx}(\cos x) = -\sin x $$
Example:
$$ \frac{d}{dx}(\cos(x^2)) = -\sin(x^2) \cdot 2x $$

$$ \frac{d}{dx}(\tan x) = \sec^2 x $$
Example:
$$ \frac{d}{dx}(\tan(3x)) = 3\sec^2(3x) $$

### Inverse Trig Derivatives

$$ \frac{d}{dx}(\arcsin x) = \frac{1}{\sqrt{1-x^2}} $$
Example:
$$ \frac{d}{dx}(\arcsin(2x)) = \frac{2}{\sqrt{1-4x^2}} $$

## Integration Formulas

### Basic Integrals

$$ \int x^n dx = \frac{x^{n+1}}{n+1} + C $$
Example:
$$ \int x^3 dx = \frac{x^4}{4} + C $$

$$ \int \frac{1}{x} dx = \ln|x| + C $$
Example:
$$ \int \frac{1}{2x} dx = \frac{1}{2}\ln|x| + C $$

### Trigonometric Integrals

$$ \int \sin x \, dx = -\cos x + C $$
Example:
$$ \int \sin(2x) \, dx = -\frac{1}{2}\cos(2x) + C $$

## Integration Techniques

### Integration by Parts

$$ \int u \, dv = uv - \int v \, du $$
Example:
$$ \int x\sin x \, dx = -x\cos x + \int \cos x \, dx = -x\cos x + \sin x + C $$

### Trigonometric Substitution

For $\sqrt{a^2-x^2}$: use $x = a\sin \theta$
Example:
$$ \int \sqrt{4-x^2} \, dx \quad \text{(let } x = 2\sin \theta) $$
