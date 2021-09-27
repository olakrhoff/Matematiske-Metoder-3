import prettytable as pt
import numpy as np

def ExplicitTrapeziodMethod(h, interval, f, y0, f_exact):
    total_steps = (int)((interval[1] - interval[0]) / h) + 1
    steps = [x for x in range(total_steps)]
    w = [1] * total_steps
    t = [0] * total_steps
    for i in range(total_steps):
        t[i] = h * i
    w[0] = y0;

    for i in range(total_steps - 1):
        f1 = f(t[i], w[i])
        w[i + 1] = w[i] + h/2 * (f1 + f(t[i] + h, w[i] + h * f1))

    y = [1] * total_steps
    g_trunc = [0] * total_steps
    for i in range(total_steps):
        y[i] = f_exact(t[i], y[i])
        g_trunc[i] = abs(w[i] - y[i])


    table = pt.PrettyTable()

    table.add_column("n", steps)
    table.add_column("t_i", t)
    table.add_column("w_i", w)
    table.add_column("y_i", y)
    table.add_column("g_i", g_trunc)



    print(table)


def function_exact(t, y):
    return 0.5 * t**2 + 1

def function(t, y):
    return t


ExplicitTrapeziodMethod(0.1, [0, 1], function, 1.0, function_exact)

