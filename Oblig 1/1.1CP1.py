import numpy
from numpy import *


TOL = 1000

def bisection(a, b, f):
    count = 0
    temp = 1
    while f(a) * f(b) >= 0:
        a -= temp
        b += temp
        temp += 1

    while ((b - a) / 2) and count < TOL:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        count += 1

    return c

def funcA(x):
    return float_power(x, 3) - 9

def funcB(x):
    return ((3 * x + 1) * x - 1) * x - 5


def funcC(x):
    return float_power(numpy.cos(x), 2) + 6 - x

print(bisection(2, 3, funcA))
print(bisection(-10, 10, funcB))
print(bisection(10, 0, funcC))

