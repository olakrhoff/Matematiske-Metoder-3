import numpy
from numpy import *

MAX = 10000

def fixedPointIteration(x, f):
    k = 1
    loop = True
    while loop:
        prev = x
        x = f(x)
        if prev == x:
            return prev
        k += 1
        if k > MAX:
            loop = False
    return False


def funcA(x):
    return float_power(2 * x + 2, 1 / 3)

def funcB(x):
    return numpy.log(7.0 - x)

def funcC(x):
    return numpy.log(4 - numpy.sin(x))


print(fixedPointIteration(2, funcA))
print(fixedPointIteration(1, funcB))
print(fixedPointIteration(1, funcC))

