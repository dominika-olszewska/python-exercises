import numpy as np
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import linspace , cos , exp, random, meshgrid, zeros, optimize
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import basinhopping
import time
# TASKS (9p)

# 5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check
# if the returned result is what you expected.
# Measure the success / total trials rate (2p).


# TASK 5

'''

def f(x):
    return 5*(1-(x[0]**2+x[1]**3))*np.e**(-(x[0]**2+x[1]**2)/2)


def neg_f(x):
    return -f(x)

x0 = random.randn(2)
x_min = fmin(neg_f, x0)

delta = 3
x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')
ax.legend()
show()

x0=[5.]
minimizer_kwargs = {"method": "BFGS"}
ret = basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=200)
print("global minimum: x = %.4f, f(x0) = %.4f" % (ret.x, ret.fun))



'''
start = time.time()
def f(x):
    return 5*(1-(x[0]**2+x[1]**3))*np.e**(-(x[0]**2+x[1]**2)/2)
    #return np.cos(14.5 * x - 0.3) + (x + 0.2) * x


def neg_f(x):
    return -f(x)

x0 = random.randn(2)
x_min = fmin(neg_f, x0)

delta = 3
x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])


ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')
ax.legend()
show()

end = time.time()
print(end - start)