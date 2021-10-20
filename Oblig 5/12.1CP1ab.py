import numpy as np

def PowerIterationMethod(A):
    MAX_ITR = 10000
    (m, n) = A.shape
    x0 = np.matrix(np.ones(A.shape[0])).reshape(n, 1)
    lamda = 0
    for j in range(1, MAX_ITR):
        u = x0 / np.linalg.norm(x0, 2)
        x0 = A @ u
        lamda = u.T @ x0
        #lamda = u.T @ A @ u

    u = x0 / np.linalg.norm(x0, 2)
    return u * abs((1 / np.min(u))), lamda
    #return u * (1 / np.min(u)), lamda


A = np.matrix("10, -12, -6; 5, -5, -4; -1, 0, 3")
B = np.matrix("-14, 20, 10; -19, 27, 12; 23, -32, -13")

u, lamda = PowerIterationMethod(A)
print(u)
print(lamda)

print()

u, lamda = PowerIterationMethod(B)
print(u)
print(lamda)

