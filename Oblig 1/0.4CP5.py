import numpy
from numpy import *

def hyp(length, height):
    long = 0
    short = 0
    if length >= height:
        long = length
        short = height
    else:
        long = height
        short = length

    return (float_power(short, 2)) / (numpy.sqrt(float_power(long, 2) + float_power(short, 2)) + long)

print(hyp(3344556600, 1.2222222))

