import math
from decimal import Decimal


# 1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

# 2 Write a function which takes sets of parameters of two figures and compares their Figure. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
# 3 Test your solutions

# TASK 1 & 2


class Figure:
    def __init__(self, figure_type=0, x=0, y=0):
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
        elif self.x <= 0 or self.y <= 0:
            print('You wrote negative values, your input should be positive')
            return -1
        else:
            return 'Incorrect input'

    def to_string(self):
        return self.figure_type


def compare(figure1=0, figure2=0):
    try:
        if figure1.count_field() > figure2.count_field():
            return str(figure1.to_string()) + ' has larger field'
        elif figure1.count_field() < figure2.count_field():
            return str(figure2.to_string()) + ' has larger field'
        else:
            return 'Fields are equal'
    except TypeError as e:
        print(e)

    except AttributeError:
        print("Object has no attributes!")


def main():

    circle = Figure('ciRcle'.lower(), 1)
    rectangle = Figure('recTangle'.lower(), 2.5, 3)
    triangle = Figure('triAngle'.lower(), 3, 2)
    rhombus = Figure('Rhombus'.lower(), 1, 2)

    fieldOfCircle = circle.count_field()
    fieldOfRectangle = rectangle.count_field()
    fieldOfTriangle = triangle.count_field()
    fieldOfRhombus = rhombus.count_field()

    text = 'Calculated field of given '
    text2 = ' is: '

    print(text, circle.to_string(), text2, fieldOfCircle)
    print(text, rectangle.to_string(), text2, fieldOfRectangle)
    print(text, triangle.to_string(), text2, fieldOfTriangle)
    print(text, rhombus.to_string(), text2, fieldOfRhombus)

    print('-' * 20)
    try:
        print(compare(circle, circle))
        print(compare(triangle, rectangle))
    except TypeError as e:
        print(e)
    print('-' * 20)


if __name__ == '__main__':
    main()
