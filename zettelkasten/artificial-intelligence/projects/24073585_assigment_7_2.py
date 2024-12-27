import numpy as np


def assignment_7_2(display=False):
    # load
    data = np.loadtxt("a7.csv", delimiter=",")
    # first col
    X = data[:, 0]
    # second col
    Y = data[:, 1]

    # 2.a: compute coefficient matrices
    # YOUR CODE
    # Create coefficient matrices using numpy functions
    # For degree 3: [1, x, x^2, x^3]
    ones = np.ones(len(X))
    x1 = X
    x2 = np.power(X, 2)
    x3 = np.power(X, 3)
    x4 = np.power(X, 4)

    # Set your answers below
    # degree 3 coefficient matrix
    degree3_coeff = np.concatenate(
        (ones.reshape(-1, 1), x1.reshape(-1, 1), x2.reshape(-1, 1), x3.reshape(-1, 1)),
        axis=1,
    )
    # degree 4 coefficient matrix
    degree4_coeff = np.concatenate(
        (
            ones.reshape(-1, 1),
            x1.reshape(-1, 1),
            x2.reshape(-1, 1),
            x3.reshape(-1, 1),
            x4.reshape(-1, 1),
        ),
        axis=1,
    )

    # 2.b: compute least squares solution
    # YOUR CODE

    # Set your answers below
    # degree 3 least squares solution
    degree3_ls = np.matmul(np.linalg.pinv(degree3_coeff), Y)
    # degree 4 least squares solution
    degree4_ls = np.matmul(np.linalg.pinv(degree4_coeff), Y)

    # 2.c: compute mean squared error
    # YOUR CODE
    # mean squared error = (1/n) * sum(y_pred - y_true)^2
    y_pred_degree3 = np.matmul(degree3_coeff, degree3_ls)
    y_pred_degree4 = np.matmul(degree4_coeff, degree4_ls)


    # Set your answers below
    # degree 3 MSE
    degree3_mse = np.mean(np.square(y_pred_degree3 - Y))
    # degree 4 MSE
    degree4_mse = np.mean(np.square(y_pred_degree4 - Y))
    # set to 0 if degree 3 solution is BETTER, 1 if degree 4 is BETTER
    mse_better = 1 if degree4_mse < degree3_mse else 0

    # 2.d: compute l1 regularization
    # YOUR CODE
    # l1 regularization = sum(abs(coefficients))

    # Set your answers below
    # degree 3 l1
    degree3_l1 = np.sum(np.abs(degree3_ls))
    # degree 4 l1
    degree4_l1 = np.sum(np.abs(degree4_ls))
    # set to 0 if degree 3 solution is BETTER, 1 if degree 4 is BETTER
    l1_better = 1 if degree4_l1 < degree3_l1 else 0

    ###
    # DO NOT CHANGE ANY LINES BELOW
    ###
    results_dict = {
        "degree3_coeff": degree3_coeff,
        "degree4_coeff": degree4_coeff,
        "degree3_ls": degree3_ls,
        "degree4_ls": degree4_ls,
        "degree3_mse": degree3_mse,
        "degree4_mse": degree4_mse,
        "mse_better": mse_better,
        "degree3_l1": degree3_l1,
        "degree4_l1": degree4_l1,
        "l1_better": l1_better,
    }
    # print results
    if display:
        for key, value in results_dict.items():
            print(key + ":")
            print(value)

    return results_dict


if __name__ == "__main__":
    results = assignment_7_2(display=True)
