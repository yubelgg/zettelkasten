# you should fill in the functions in this file,
# do NOT change the name, input and output of these functions

import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_digits, load_iris

# first function to fill, compute distance matrix using loops
def compute_distance_naive(X):
    N = X.shape[0]      # num of rows
    D = X[0].shape[0]   # num of cols
    
    M = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            xi = X[i,:]
            xj = X[j,:]  
            # expanded formula: np.sqrt(np.sum(xi**2) - 2*np.dot(xi, xj) + np.sum(xj**2))
            # computed matrix are not identical, numerical precision issue?
            # simplified formula: np.sqrt(np.sum((xi - xj)**2))
            dist = np.sqrt(np.sum((xi - xj)**2))  
            M[i,j] = dist

    return M

# second function to fill, compute distance matrix without loops
def compute_distance_smart(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols
    
    # computes the squared norms for all rows at the same time
    # 1D array length N
    squared_norms = np.sum(X**2, axis=1)

    # compute the distance matrix
    # np.newaxis is used to make the dimensions of the squared_norms array the same dimensions of the dot product
    row = squared_norms[np.newaxis, :] # broadcasting row to the same dimensions (1, N)
    column = squared_norms[:, np.newaxis] # broadcasting column to the same dimensions (N, 1)

    # compute the distance matrix
    M = np.sqrt(np.maximum(row - 2 * np.dot(X, X.T) + column, 0))

    return M

# third function to fill, compute correlation matrix using loops
def compute_correlation_naive(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols

    # use X to create M
    M = np.zeros([D, D])

    # mean of each column with loop
    mu = np.zeros(D)
    for j in range(D):
        mu[j] =  np.sum(X[:, j]) / N

    # covariance matrix with loops
    S = np.zeros([D, D])
    for i in range(D):
        for j in range(D):
            xi = X[:, i]
            xj = X[:, j]
            covariance =  np.sum((xi - mu[i]) * (xj - mu[j])) / (N - 1.0)
            S[i, j] = covariance

    # standard deviation
    sigma = np.zeros(D)
    for i in range(D):
        sigma[i] = np.sqrt(S[i, i])

    # correlation matrix with loop  
    for i in range(D):
        for j in range(D):
            corr = S[i, j] / (sigma[i] * sigma[j])
            M[i, j] = corr

    return M

# fourth function to fill, compute correlation matrix without loops
def compute_correlation_smart(X):
    N = X.shape[0]  # num of rows
    D = X[0].shape[0]  # num of cols

    # use X to create M
    M = np.zeros([D, D])

    # mean of each column
    mu = np.mean(X, 0)

    # covariance matrix without loops
    covariance = np.dot((X - mu).T, (X - mu)) / (N - 1.0)

    # standard deviation
    sigma = np.sqrt(covariance.diagonal())

    # pairwise sigma with itself
    # np.expand_dims(arr, 1) makes sigma D: D x 1 matrix (column vector), 
    # np.expand_dims(arr, 0) makes sigma D: 1 x D matrix (row vector)      
    # pair_wise_sigma[i,j] = sigma[i] * sigma[j]
    pair_wise_sigma = np.dot(np.expand_dims(sigma, 1), np.expand_dims(sigma, 0))

    # correlation matrix
    M = covariance / pair_wise_sigma

    return M


def main():

    # Question 3
    result = []
    iris = load_iris()
    iris_data = iris.data
    print("iris data shape: ", iris_data.shape)

    # compute distance matrices for iris data
    st = time.time()
    iris_dist_loop = compute_distance_naive(iris_data)
    et = time.time()
    perf_dist_loop = et - st              # time difference

    st = time.time()
    iris_dist_cool = compute_distance_smart(iris_data)
    et = time.time()
    perf_dist_cool = et - st

    result.append(['iris', perf_dist_loop, perf_dist_cool])

    breast_cancer = load_breast_cancer()
    breast_cancer_data = breast_cancer.data
    print("breast cancer data shape: ", breast_cancer_data.shape)

    # compute distance matrices for breast cancer data
    st = time.time()
    breast_cancer_dist_loop = compute_distance_naive(breast_cancer_data)
    et = time.time()
    perf_dist_loop = et - st              # time difference

    st = time.time()
    breast_cancer_dist_cool = compute_distance_smart(breast_cancer_data)
    et = time.time()
    perf_dist_cool = et - st

    result.append(['breast_cancer', perf_dist_loop, perf_dist_cool])

    # print("breast cancer distance loop: ", breast_cancer_dist_loop)
    # print("breast cancer distance cool: ", breast_cancer_dist_cool)

    digits = load_digits()
    digits_data = digits.data
    print("digits data shape: ", digits_data.shape)

    # compute distance matrices for digits data
    st = time.time()
    digits_dist_loop = compute_distance_naive(digits_data)
    et = time.time()
    perf_dist_loop = et - st              # time difference

    st = time.time()
    digits_dist_cool = compute_distance_smart(digits_data)
    et = time.time()
    perf_dist_cool = et - st

    result.append(['digits', perf_dist_loop, perf_dist_cool])

    # print("digits distance loop: ", digits_dist_loop)
    # print("digits distance cool: ", digits_dist_cool)

    max_length = max(len(data[0]) for data in result)

    print(f"{'Dataset':<{max_length}} {'Loops':>12} {'Vectorization':>16}")
    print("-" * (max_length + 30)) 

    for data in result:
        print(f"{data[0]:<{max_length}} {data[1]:>12.6f} {data[2]:>16.6f}")


    print('starting comparing distance computation .....')
    np.random.seed(100)
    params = range(10,141,10)   # different param setting
    nparams = len(params)       # number of different parameters

    perf_dist_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
    perf_dist_cool = np.zeros([10,nparams])
    perf_corr_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
    perf_corr_cool = np.zeros([10,nparams])

    counter = 0

    for ncols in params:
        nrows = ncols * 10

        print("matrix dimensions: ", nrows, ncols)

        for i in range(10):
            X = np.random.rand(nrows, ncols)   # random matrix

            # compute distance matrices
            st = time.time()
            dist_loop = compute_distance_naive(X)
            et = time.time()
            perf_dist_loop[i,counter] = et - st              # time difference

            st = time.time()
            dist_cool = compute_distance_smart(X)
            et = time.time()
            perf_dist_cool[i,counter] = et - st

            assert np.allclose(dist_loop, dist_cool, atol=1e-06) # check if the two computed matrices are identical all the time

            # compute correlation matrices
            st = time.time()
            corr_loop = compute_correlation_naive(X)
            et = time.time()
            perf_corr_loop[i,counter] = et - st              # time difference

            st = time.time()
            corr_cool = compute_correlation_smart(X)
            et = time.time()
            perf_corr_cool[i,counter] = et - st

            assert np.allclose(corr_loop, corr_cool, atol=1e-06) # check if the two computed matrices are identical all the time

        counter = counter + 1

    mean_dist_loop = np.mean(perf_dist_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
    mean_dist_cool = np.mean(perf_dist_cool, axis = 0)
    std_dist_loop = np.std(perf_dist_loop, axis = 0)      # standard deviation
    std_dist_cool = np.std(perf_dist_cool, axis = 0)

    plt.figure(1)
    plt.errorbar(params, mean_dist_loop[0:nparams], yerr=std_dist_loop[0:nparams], color='red',label = 'Loop Solution for Distance Comp')
    plt.errorbar(params, mean_dist_cool[0:nparams], yerr=std_dist_cool[0:nparams], color='blue', label = 'Matrix Solution for Distance Comp')
    plt.xlabel('Number of Cols of the Matrix')
    plt.ylabel('Running Time (Seconds)')
    plt.title('Comparing Distance Computation Methods')
    plt.legend()
    plt.savefig('CompareDistanceCompFig.pdf')
    plt.show()    # uncomment this if you want to see it right way
    print("result is written to CompareDistanceCompFig.pdf")

    mean_corr_loop = np.mean(perf_corr_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
    mean_corr_cool = np.mean(perf_corr_cool, axis = 0)
    std_corr_loop = np.std(perf_corr_loop, axis = 0)      # standard deviation
    std_corr_cool = np.std(perf_corr_cool, axis = 0)

    plt.figure(2)
    plt.errorbar(params, mean_corr_loop[0:nparams], yerr=std_corr_loop[0:nparams], color='red',label = 'Loop Solution for Correlation Comp')
    plt.errorbar(params, mean_corr_cool[0:nparams], yerr=std_corr_cool[0:nparams], color='blue', label = 'Matrix Solution for Correlation Comp')
    plt.xlabel('Number of Cols of the Matrix')
    plt.ylabel('Running Time (Seconds)')
    plt.title('Comparing Correlation Computation Methods')
    plt.legend()
    plt.savefig('CompareCorrelationCompFig.pdf')
    plt.show()    # uncomment this if you want to see it right way
    print("result is written to CompareCorrelationCompFig.pdf")


if __name__ == "__main__": main()