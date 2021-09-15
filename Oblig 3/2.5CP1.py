import numpy as np
from numpy import *
import scipy.sparse as sp

def Jacobi(A, b, k):
    n = len(b) # find n
    r = A.copy()
    r.setdiag(0)
    d = A - r
    for i in range (n):
        d[i, i] = 1 / d[i, i] #invers
    x = np.transpose(np.matrix(zeros(n))) # initialize vector x
    b = np.transpose(np.matrix(b))
    for j in range (k): # loop fr jacobi iteration
        x = (d @ (b - (r @ x)))
        if (forwardError(x)):
            return j, backwardError(A, b, x)
    return k, backwardError(A, b, x), x

def makeMatrix(n):
    if (n % 2 != 0):
        raise ValueError(f"Input må være et partall. Du skrev makeMatrix({n})")
    data = np.array([[-1], [3], [-1]]) @ np.ones([1, n])
    offset = np.array([-1, 0, 1])
    A = sp.dia_matrix((data, offset), shape = (n, n))
    A = A.tolil()
    b = np.ones(n) * 1
    b[0] = 2
    b[-1] = 2

    return A , b

def forwardError(x0):
    x = np.transpose(np.matrix(ones(x0.size)))
    tol = 1e-07
    max = -1.0
    for i in range (x.size):
        if (abs(x[i] - x0[i]) > max):
            if (max > tol):
                return False
            max = abs(x[i] - x0[i])
    return max < tol

def backwardError(a, b, x0):
    r = b - (a @ x0)
    max = -1.0
    for i in range(r.size):
        if (abs(r[i]) > max):
            max = abs(r[i])
    return max

n = 100
A, b = makeMatrix(n)

print("Matrise A: ", A.toarray())
print("b: ", b)
print("Jacobi: ", Jacobi(A, b, n))


