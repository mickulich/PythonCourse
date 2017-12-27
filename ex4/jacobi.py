#encoding=utf-8
import math
import time
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot, zeros_like, ones_like, fabs, linalg


def Jacobi (A, b, exp=None):
    if linalg.norm(linalg.matrix_power(A,-1)) >= 1:
        print("Method diverges.")
        return

    if exp is None:
        x_previous = zeros_like(b)
    else:
        x_previous = exp
    eps = 1E-10
    x_this = zeros_like(b)
    iterations = 1
    it = 0
    while it < iterations:
        print (it)
        for i in range(len(b)):
            x_this[i] = b[i]
            for j in range(len(b)):
                if j != i:
                    x_this[i] -= A[i][j] * x_previous[j]
            x_this[i] /= A[i][i]
        norm = fabs(x_this[0] - x_previous[0])
        for j in range(1, len(b)):
            if fabs(x_this[j] - x_previous[j]) > norm:
                norm = x_this[j] - x_previous[j]
        if norm < eps:
            return x_this
        iterations += 1
        it += 1
        x_previous = x_this
        x_this = zeros_like(b)



if __name__ == '__main__':

    start_time = time.time()

    eps = 0.001
    A = array([[5., -2., 0., -1.],
               [0., 4., -4., 0.],
               [1., -5., 5., 1.],
               [2., -2., -1., 4.]])
    b = array([0.,  0.,  0.,  0.])

    sol = Jacobi(A, b)

    print ("x:")
    pprint(sol)
    print("--- {} seconds ---".format(time.time() - start_time))