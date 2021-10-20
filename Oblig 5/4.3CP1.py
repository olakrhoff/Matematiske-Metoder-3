import numpy as np


def ClassicGramSchmidt(A):
    m, n = A.shape
    r = np.matrix(np.zeros(n * n)).reshape((n, n))
    q = np.matrix(np.zeros(m * n)).reshape(m, n)

    for j in range(n):
        y = A[:, j].reshape(1, n)
        for i in range(j):
            r[i, j] = q[:][i] @ A[:, j].reshape(n, 1)
            y = y - r[i, j] * q[:][i]
        r[j, j] = np.linalg.norm(y, 2)
        q[:][j] = y * (1 / r[j, j])

    return q.T, r

A = np.matrix("4, 0; 3, 1")


q, r = ClassicGramSchmidt(A)
print("A:\n", A)
print("Q:\n", q)
print("R:\n", r)

