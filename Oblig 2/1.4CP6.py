import numpy
from numpy import *

h = 10 #cm
v = 60 #cm^3

def newton(x0, f, fd):
    count = 0
    xi = x0
    while (count < 100):
        print("Guess", count, ": ", xi)
        count += 1
        xi = xi - f(xi) / fd(xi)


def func(r):
    return (h + 2 * r) * numpy.pi * float_power(r, 2) - 3 * v

def funcD(r):
    return (3 * r + h) * 2 * numpy.pi * r

newton(1, func, funcD)