from cs50 import get_int
import math
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# TASKS (8p)- calculate & print:

# 0 Use alternative way of reading inputs - using library (0.5p)
# 1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
# 2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
# 3 Check if X is divisible by Y (do it in one line of code),
#   print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
# Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
# 4 Add rounding for the above x/y operation. Round to 2 decimal points.
#   Hint: look up in Google "python limiting number of decimals". (1p)
# 5 Look at lab2-plot.py and create your own script which takes a number
#   as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
# 6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)


# TASK 0

x = get_int("x: ")
y = get_int("y: ")

print('-'*20)
'''
# TASK 1

# perimeterOfCircle1 = 2*math.pi * x
# perimeterOfCircle2 = 2*math.pi * y

# fieldOfCircle1 = math.pi*math.pow(x, 2)
# fieldOfCircle2 = math.pi*math.pow(y, 2)

# print(perimeterOfCircle1, fieldOfCircle1)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter_circle(self):
        if self.radius >= 0:
            print('Perimeter od this circle equals:', 2 * math.pi * self.radius)
        elif self.radius < 0:
            print('Radius can\'t be negative ')

    def field_circle(self):
        if self.radius >= 0:
            print('Field od this circle equals:', math.pi*math.pow(self.radius, 2))
        elif self.radius < 0:
            print('Radius can\'t be negative ')


circle1 = Circle(x)
circle2 = Circle(y)

print('CIRCLE 1')
circle1.perimeter_circle()
circle1.field_circle()

print('CIRCLE 2')
circle2.perimeter_circle()
circle2.field_circle()

print('-' * 20)


# TASK 2

try:
    if x % y == 0 and x % 2 == 0 and y % 2 == 0:
        print('These numbers sadisfy requirements')
except ZeroDivisionError:
    print("division by zero!")
finally:
    print("Find other numbers")


print('-'*20)


# TASK 3
try:
    print('X is divisible by Y') if x % y == 0 else print('X is not divisible by Y')
        
except ZeroDivisionError:
    print("division by zero!")


print('-'*20)

'''
# TASK 4

try:
    convertToDecimal = Decimal(x / y)
    output = round(convertToDecimal, 4)
    print(output)
except ZeroDivisionError:
    print("division by zero!")


print('-'*20)
'''
# TASK 5

x_knots = np.linspace(x, y, 300)
y_knots = np.linspace(x, y, 300)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.3*R)
ax = Axes3D(plt.figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()

'''




