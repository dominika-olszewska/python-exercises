import math

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

# zabezpiecz prze 0 i ujemnymi


def count_field(figure_type, x, y):
    if figure_type == 'circle' and x > 0 and y > 0:
        print(math.pi * x ** 2)
    elif figure_type == 'rectangle' and x > 0 and y > 0:
        print(x * y)
    elif figure_type == 'triangle' and x > 0 and y > 0:
        print(0.5 * x * y)
    elif figure_type == 'rhombus' and x > 0 and y > 0:
        print(0.5 * x * y)
    else:
        print('Write another values')


# Circle = count_field('circle', 1, 2) ????

# Circle() ????/

count_field('rectangle', 3, 4)

count_field('rhombus', -1, 4)


# TASK 2



# def compare():


'''
try:
    convertToDecimal = Decimal(x / y)
    output = round(convertToDecimal, 4)
    print(output)
except ZeroDivisionError:
    print("division by zero!")

'''
'''
class SampleClass1:

    def __init__(self, a):
        self.set_a(a)

    def get_a(self):
        return self.__a

    def set_a(self, a):

        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2

'''
print('-'*20)
