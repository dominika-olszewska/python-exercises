import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

# TASKS (9p)

# 3 Find a differential equation which represents a process / model (your choice)
# and implement it using odeint python function (1p)


# model: Function name that returns derivative values
# at requested y and t values as dydt = model(y,t)


def differentialEquation(y0, tk):
    # function that returns dy/dt
    def model(y, t):
        # dydt = -y + 1.0
        dydt = 3.0 * np.exp(-t)
        return dydt


    # time points
    t = np.linspace(0, tk)

    y = odeint(model, y0, t)

    print('Funkcja, której stanem początkowym jest y0 =', y0, ' , a czas końcowy równa się tk =', tk)

    plt.plot(t, y)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()


try:
    differentialEquation(0, 5)

except TypeError as e:
    print(e)

except AttributeError as e:
    print(e)
