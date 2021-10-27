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

f_a = lambda x: np.array([x[0]**2 + x[1]**2 - 1.0, (x[0] - 1.0)**2 + x[1]**2 - 1.0]).reshape((2, 1)) #u^2 + v^2 - 1 = 0, (u - 1)^2 + v^2 - 1 = 0
J_a = lambda x: np.array([2.0 * x[0], 2.0 * x[1], 2.0 * (x[0] - 1), 2.0 * x[1]]).reshape((2, 2)) #2u, 2v, 2(u - 1), 2v
x0_a = np.array([1, -1]).reshape((2, 1))

f_b = lambda x: np.array([x[0]**2 + 4.0 * x[1]**2 - 4.0, 4.0 * x[0]**2 + x[1]**2 - 4.0]).reshape((2, 1)) #u^2 + 4v^2 - 4 = 0, 4u^2 + v^2 - 4 = 0
J_b = lambda x: np.array([2.0 * x[0], 8.0 * x[1], 8.0 * x[0], 2.0 * x[1]]).reshape((2, 2)) #2u, 8v, 8u, 2v
x0_b = np.array([-1, -1]).reshape((2, 1))

f_c = lambda x: np.array([x[0]**2 - 4.0 * x[1]**2 - 4.0, (x[0] - 1.0)**2 + x[1]**2 - 4.0]).reshape((2, 1)) #u^2 - 4v^2 - 4 = 0, (u - 1)^2 + v^2 - 4 = 0
J_c = lambda x: np.array([2.0 * x[0], -8.0 * x[1], 2.0 * (x[0] - 1), 2.0 * x[1]]).reshape((2, 2)) #2u, -8v, 2(u - 1), 2v
x0_c = np.array([1, -1]).reshape((2, 1))

x = NewtonMulti(f_a, J_a, x0_a, 0.001)
print(x)
print("\n")

x = NewtonMulti(f_b, J_b, x0_b, 0.001)
print(x)
print("\n")

x = NewtonMulti(f_c, J_c, x0_c, 0.001)
print(x)
print("\n")
