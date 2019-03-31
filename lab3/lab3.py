import math
from decimal import Decimal
# 1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

# 2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
# 3 Test your solutions

# TASK 1


def count_field(figure_type, x, y=0):
    text = 'Calculated field of given '
    text2 = ' is '
    if figure_type == 'circle' and x > 0:
        convertToDecimal = Decimal(math.pi * x ** 2)
        calculated_field = round(convertToDecimal, 2)
        result = text + str(figure_type) + text2 + str(calculated_field)
        return result
    elif figure_type == 'rectangle' and x > 0 and y > 0:
        calculated_field = x * y
        result = text + str(figure_type) + text2 + str(calculated_field)
        return result
    elif figure_type == 'triangle' and x > 0 and y > 0:
        calculated_field = 0.5 * x * y
        result = text + str(figure_type) + text2 + str(calculated_field)
        return result
    elif figure_type == 'rhombus' and x > 0 and y > 0:
        calculated_field = 0.5 * x * y
        result = text + str(figure_type) + text2 + str(calculated_field)
        return result
    else:
        result = 'Write another values'
        return result


circle = count_field('circle', 1)
rectangle = count_field('rectangle', 1, 5)
triangle = count_field('triangle', 3, 2)
rhombus = count_field('rhombus', 1, 2)

print(circle)
print(rectangle)
print(triangle)
print(rhombus)

print('-'*20)
