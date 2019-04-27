import numpy as np
import matplotlib.pyplot as plt


# TASKS (9p)
# 1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)


# TASK 1


def Euler(a, T, h):
    initial_x = 1

    t = np.arange(0, T, h)  # start stop step
    x = np.zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (a * x[i])

    plt.plot(t, x, 'o')
    plt.xlabel('t', fontsize=14)
    plt.ylabel('x', fontsize=14)
    plt.show()


try:
    Euler(1, 5, 0.1)

except TypeError as e:
    print(e)

except AttributeError as e:
    print(e)
