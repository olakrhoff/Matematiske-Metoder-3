import prettytable as pt
import numpy as np

def EulersMethod(h, interval, f, y0, f_exact):
    total_steps = (int)((interval[1] - interval[0]) / h) + 1
    steps = [x for x in range(total_steps)]
    w = [1] * total_steps
    t = [0] * total_steps
    for i in range(total_steps):
        t[i] = h * i
    w[0] = y0;

    for i in range(total_steps - 1):
        w[i + 1] = w[i] + h * f(t[i], w[i])

    y = [1] * total_steps
    error = [0] * total_steps
    for i in range(total_steps):
        y[i] = f_exact(t[i], y[i])
        error[i] = y[i] - w[i]


    table = pt.PrettyTable()

    table.add_column("n", steps)
    table.add_column("t_i", t)
    table.add_column("w_i", w)
    table.add_column("y_i", y)
    table.add_column("e_i", error)



    print(table)


def function_exact_A(t, y):
    return 0.5 * t**2 + 1

def function_A(t, y):
    return t

def function_exact_B(t, y):
    return np.exp(1/3 * t**3)

def function_B(t, y):
    return t**2 * y


EulersMethod(0.1, [0, 1], function_A, 1.0, function_exact_A)

EulersMethod(0.1, [0, 1], function_B, 1.0, function_exact_B)