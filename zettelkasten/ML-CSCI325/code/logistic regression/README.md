# Logistic Regression with Regularization

## Overview
This project implements logistic regression with regularization to classify breast cancer tumors as malignant or benign. The implementation includes feature transformation and cross-validation to evaluate model performance.

## Technical Details

### Logistic Regression
The algorithm uses the sigmoid function to map numerical inputs to probabilities between 0 and 1:

Sigma(z) = 1/(1 + e^(-z))

The model combines features using weights to predict probabilities, then iteratively updates these weights based on comparison with actual results.

### Implementation Details with Scikit-learn
The core logistic regression formula used:

P(y=1|x) = 1 / (1 + exp(-w⋅x))

Where:
- P(y=1|x) is the probability that y=1 given input x
- w is the vector of weights (coefficients)
- x is the input feature vector
- exp is the exponential function (e^x)
- w⋅x is the dot product: w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ

Binary classification is determined by:
y = 1 if P(y=1|x) ≥ 0.5
y = 0 if P(y=1|x) < 0.5

With L2 regularization (Ridge), the cost function is:
Cost = -1/m ∑[y⋅log(h(x)) + (1-y)⋅log(1-h(x))] + λ/(2m) ∑(w²)

Where:
- m is the number of training examples
- h(x) is the logistic function (sigmoid)
- y is the actual label
- λ is the regularization parameter (inverse of sklearn's C parameter)
- The sum of w² excludes the bias term w₀

Key sklearn parameters used:

### Feature Transformation
We implement different degrees of feature combinations:

1. First Order Example:
f(x) = w1(size) + w2(texture) + w3(perimeter)

2. Second Order Example:
f(x) = w1(size) + w2(texture) + w3(size × texture) + w4(size^2)

### Regularization
- Uses Ridge regression (L2 regularization)
- Lambda parameter controls regularization strength:
  - Higher lambda → weaker model
  - Lower lambda → stronger regularization

### Cross-Validation
- Implementation uses 5-fold cross validation
- Each fold contains approximately 114 samples
- Process:
  1. Data is randomly shuffled
  2. Split into 5 equal-sized parts (folds)
  3. For each iteration:
     - Use 4 folds for training (≈456 samples)
     - Use 1 fold for validation (≈114 samples)
     - Rotate which fold is used for validation
  4. Each data point appears in the validation set exactly once
  5. Each data point appears in the training set 4 times

- Error measure computation:
Eval = (error_1 + error_2 + error_3 + error_4 + error_5) / 5

## Results

### Performance Metrics
- Overall accuracy around 95% for training data
- Feature transformation findings:
  - Second-degree polynomial showed similar results to first-degree
  - Third-degree polynomial showed no significant improvement
  - Higher dimensions did not yield better performance

### Regularization Impact
- Optimal lambda range: 10^-1 to 10^1 across all degrees
- Lower lambda values resulted in worse performance
- Higher lambda values generally improved performance

## Key Learnings
1. Higher dimensional feature transformations don't always improve model performance
2. Linear model (degree one) is preferred due to its simplicity and comparable performance
3. Low regularization parameters (lambda) have a more negative impact on performance compared to higher values

## Environment
- Python 3.12
- Linux
- 5-fold cross validation implementation

## Resources
- [Logistic Regression and Regularization: Avoiding Overfitting and Improving Generalization](https://medium.com/@rithpansanga/logistic-regression-and-regularization-avoiding-overfitting-and-improving-generalization-e9afdcddd09d)
- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=Q81RR3yKn30)
- [StatQuest: Logistic Regression Details Pt 1](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- [StatQuest: Logistic Regression Details Pt 2](https://www.youtube.com/watch?v=yIYKR4sgzI8)
