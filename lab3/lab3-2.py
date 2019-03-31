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

# TASK 2


class Fields:
    def __init__(self, figure_type, x, y=0):
        self.x = x
        self.y = y
        self.figure_type = figure_type

    def count_field(self):
        if self.figure_type == 'circle' and self.x > 0:
            convertToDecimal = Decimal(math.pi * self.x ** 2)
            result = round(convertToDecimal, 2)
            return result
        elif self.figure_type == 'rectangle' and self.x > 0 and self.y > 0:
            result = self.x * self.y
            return result
        elif self.figure_type == 'triangle' and self.x > 0 and self.y > 0:
            result = 0.5 * self.x * self.y
            return result
        elif self.figure_type == 'rhombus' and self.x > 0 and self.y > 0:
            result = 0.5 * self.x * self.y
            return result
        else:
            result = 'Write another values'
            return result

    def to_string(self):
        return self.figure_type


circle = Fields('circle', 1)
rectangle = Fields('rectangle', 1, 2)
triangle = Fields('triangle', 3, 2)
rhombus = Fields('rhombus', 1, 2)


def compare(figure1, figure2):
    if figure1.count_field() > figure2.count_field():
        return str(figure1.to_string()) + ' has larger field'
    elif figure1.count_field() < figure2.count_field():
        return str(figure2.to_string()) + ' has larger field'
    else:
        return 'Fields are equal'


print(compare(circle, rectangle))
print(compare(triangle, rectangle))

print('-'*20)
