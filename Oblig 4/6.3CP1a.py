import inline as inline
import matplotlib.pyplot as plt
import prettytable as pt
import numpy as np


def EulersMethod(h, interval, f_arr, y0_arr, f_exact_arr):
    total_steps = (int)((interval[1] - interval[0]) / h) + 1
    steps = [x for x in range(total_steps)]
    functions = len(f_arr)
    w = np.zeros((total_steps, functions))
    t = [0] * total_steps
    for i in range(total_steps):
        t[i] = h * i

    for f in range(functions):
        w[0][f] = y0_arr[f];

    for i in range(total_steps - 1):
        for y in range(functions):
            w[i + 1][y] = w[i][y] + h * f_arr[y](t[i], w[i][0], w[i][1])

    y = np.ones((total_steps, functions))
    global_trunc = np.zeros((total_steps, functions))
    for i in range(total_steps):
        for j in range(functions):
            y[i][j] = f_exact_arr[j](t[i])
            global_trunc[i][j] = abs(w[i][j] - y[i][j])

    table = pt.PrettyTable()

    table.add_column("n", steps)
    table.add_column("t_i", t)
    table.add_column("w_1_i", w[:, 0])
    table.add_column("w_2_i", w[:, 1])
    table.add_column("y_1_i", y[:, 0])
    table.add_column("y_2_i", y[:, 1])
    table.add_column("e_1_i", global_trunc[:, 0])
    table.add_column("e_2_i", global_trunc[:, 1])

    print(table)

    fig, axs = plt.subplots(1, 2, constrained_layout = False)

    axs[0].plot(t, w[:, 0])
    axs[0].plot(t, w[:, 1])
    axs[0].plot(t, y[:, 0])
    axs[0].plot(t, y[:, 1])
    axs[1].plot(t, global_trunc[:, 0])
    axs[1].plot(t, global_trunc[:, 1])

    axs[1].loglog()


    axs[0].legend(["w_1", "w_2", "y_1", "y_2"])
    axs[1].legend(["g_1", "g_2"])

    plt.show()


def function_exact_y1(t):
    return np.exp(t) * np.cos(t)

def function_y1(t, y1, y2):
    return y1 + y2

def function_exact_y2(t):
    return -np.exp(t) * np.sin(t)

def function_y2(t, y1, y2):
    return y2 - y1

EulersMethod(0.1, [0, 1], [function_y1, function_y2], [1.0, 0.0], [function_exact_y1, function_exact_y2])
