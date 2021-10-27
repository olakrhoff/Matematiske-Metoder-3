import numpy as np

def NewtonMulti(f, J, x0, tol):
    x = x0
    f_x = f(x)
    while (np.abs(np.linalg.norm(f_x)) > tol):
        J_x = J(x)
        s = np.linalg.solve(J_x, -f_x)
        x = x + s
        f_x = f(x)

    return x

f = lambda x: np.array([x[0]**3 - x[1]**3 + x[0], x[0]**2 + x[1]**2 - 1.0]).reshape((2, 1)) #u^3 - v^3 + u = 0, u^2 + v^2 - 1 = 0
J = lambda x: np.array([3.0 * x[0]**2 + 1, -3.0 * x[1]**2, 2.0 * x[0], 2.0 * x[1]]).reshape((2, 2)) #3u^2 + 1, -3v^2, 2u, 2v
x0 = np.array([-1.0, 1.0]).reshape((2, 1))

x = NewtonMulti(f, J, x0, 0.00001)
print(x)
print("\n")

