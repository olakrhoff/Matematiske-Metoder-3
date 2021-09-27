import matplotlib.pyplot as plt
import prettytable as pt
import numpy as np

def MidtPunkt(h, interval, f, y0, f_exact):
    total_steps = (int)((interval[1] - interval[0]) / h) + 1
    steps = [x for x in range(total_steps)]
    w = [1] * total_steps
    t = [0] * total_steps
    for i in range(total_steps):
        t[i] = h * i
    w[0] = y0;

    for i in range(total_steps - 1):
        s1 = f(t[i], w[i])
        s2 = f(t[i] + h / 2, w[i] + h / 2 * s1)
        s3 = f(t[i] + h / 2, w[i] + h / 2 * s2)
        s4 = f(t[i] + h, w[i] + h * s3)

        w[i + 1] = w[i] + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)

    y = [1] * total_steps
    global_trunc = [0] * total_steps
    for i in range(total_steps):
        y[i] = f_exact(t[i], y[i])
        global_trunc[i] = y[i] - w[i]

    table = pt.PrettyTable()

    table.add_column("n", steps)
    table.add_column("t_i", t)
    table.add_column("w_i", w)
    table.add_column("y_i", y)
    table.add_column("g_i", global_trunc)
    print(table)

    return w, y, t

def function_exact(t, y):
    return np.exp(t**3 / 3)

def function(t, y):
    return t**2 * y

w1, y1, t1 = MidtPunkt(0.1, [0, 1], function, 1.0, function_exact)
w5, y5, t5 = MidtPunkt(0.05, [0, 1], function, 1.0, function_exact)
w25, y25, t25 = MidtPunkt(0.025, [0, 1], function, 1.0, function_exact)


fig, axs = plt.subplots(1, 1, constrained_layout=False)

axs.plot(t1, w1)
axs.plot(t5, w5)
axs.plot(t25, w25)
axs.plot(t25, y25)


axs.legend(["w (h = 0.1)", "w (h = 0.05)", "w (h = 0.025)", "Exact"])

plt.show()


