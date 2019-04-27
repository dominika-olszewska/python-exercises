import numpy as np
import matplotlib.pyplot as plt



# TASKS (9p)

# 2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
# 2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'


# TASK 2


def Euler(a, T, h):
    initial_x = 1

    t = np.arange(0, T, h)  # start stop step
    x = np.zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (a * x[i])

    plt.plot(t, x, 'o', label='euler')
    plt.plot(t, x, 'g', label='aprrox')

    plt.xlabel('t', fontsize=14)
    plt.ylabel('x', fontsize=14)
    plt.legend(loc='upper left', fontsize=14)
    plt.show()


try:
    Euler(1, 5, 0.1)

except TypeError as e:
    print(e)

except AttributeError as e:
    print(e)