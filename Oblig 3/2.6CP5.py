import numpy as np
import scipy.sparse as sp

def ConjugateGradientMethod(x0, A, b):
    TOL = 1e-50
    n = b.size
    x0 = sp.csc_matrix(x0)
    b = np.transpose(sp.csc_matrix(b))
    A = A.tocsc()
    d = b - (A * x0)
    r0 = d
    x = x0

    for i in range(n):
        if (maxRValue(r0, TOL)):
            return i, infNorm(b, A, x)

        alpha = (np.transpose(r0) * r0) / (np.transpose(d) * A * d)
        x = x + d.multiply(alpha)
        r1 = r0 - (A * d).multiply(alpha)
        beta = (np.transpose(r1) * r1) / (np.transpose(r0) * r0)
        d = r1 + d.multiply(beta)
        r0 = r1

    return n, infNorm(b, A, x)

def infNorm(b, A, x):
    r = b - (A * x)
    max = -1.0

    for i in range(r.size):
        if (abs(r[i]) > max):
            max = abs(r[i])
    if (max == -1.0):
        raise ValueError("Max not found")
    return max

def maxRValue(x, TOL):
    for i in range(x.size):
        if (abs(x[i]) > TOL):
            return False
    return True

def makeMatrix(n):
    if (n % 2 != 0):
        raise ValueError("Må være partall")
    data = np.array([[-1], [3], [-1]]) @ np.ones([1, n])
    offset = np.array([-1, 0, 1])
    A = sp.dia_matrix((data, offset), shape=(n, n))
    A = A.tolil()

    for i in range(n):
        if (2 * i > n or 2 * i < n - 2):
            A[-i - 1, i] = 1 / 2

    b = np.ones(n) * 1.5
    b[0] = 2.5
    b[-1] = 2.5
    b[n // 2] = 1
    b[n // 2 - 1] = 1

    return A, b

n = 10000

A, b = makeMatrix(n)

print(A.toarray())
print(b)

x0 = np.matrix([[0.0] for x in range(n)])
n_itr, BE = ConjugateGradientMethod(x0, A, b)

print("Iterasjoner: ", n_itr)
print("BE: ", BE.toarray()[0][0])