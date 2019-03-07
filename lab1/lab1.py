from matplotlib.pyplot import *
from numpy import *

#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
#2 ask the user for a number and print its factorial (1p)
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)

'''
# TASK 1

def equation(x):    
    return 2 * x


for i in range(56, 101):
    print(equation(i))

print('-'*20)

# TASK 2

x = int(input('Insert your value here which ia a natural number:'))


def factorial(x):

    if x in range(0,2):
        return 1
    elif x>2:
        return x*factorial(x-1)
    else:
        return 'Error'


print(factorial(x))

print('-'*20)
'''
# TASK 3

myArr = [8, 4, 3, 6, 2, 54, 2, 2]
minNr = myArr[0]
minIndexPosition = []

for i in range(0, len(myArr)):

    if myArr[i] < minNr:
        minNr = myArr[i]


for i in range(0, len(myArr)):

    if myArr[i] == minNr:
        minIndexPosition.append(i)


if len(minIndexPosition) == 1:
    print('There is one minimum found: number', minNr)
else:
    print('There are found', len(minIndexPosition), 'minimums on positions', minIndexPosition, 'in the array')


print('-'*20)

# TASK 4

a = int(input(f"Choose the length of chart:"))

x = linspace(0, a, 50)
y = 2*x**2
plot(x, y)
show()
