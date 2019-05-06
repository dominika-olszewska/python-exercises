from scipy import linspace, cos, exp, random, meshgrid, zeros
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel

# TASKS (9p)

# 4 Look at the example of optimization for exponential function. wykladnicza
# Did you encounter any errors? Where in code do we display the optimal point?
# Do we minimize or maximize and which function?
# Start your search always from the point (0, -2). (1p)


# TASK 4


def f(x):
    return cos(x) - 3 * exp(-(x - 0.2) ** 2)


x0 = 0
x_min = fmin(f, x0)

delta = 3
x = linspace(x_min - delta, x_min + delta, 301)
y = f(x)
plot(x, y)
plot(x0, f(x0), 'go', label='initial x')
plot(x_min, f(x_min), 'ro', label='optimal x')
legend(loc='upper right')
show()