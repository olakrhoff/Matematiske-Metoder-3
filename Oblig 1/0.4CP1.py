from numpy import *

def first(power):
    return (1 - (1 / cos(pow(10, power)))) / (pow(tan(pow(10, power)), 2)) # (1 - sec(x)) / (tan^2(x))

def second(power):
    return (-1 / (1 + (1 / cos(pow(10, power))))) # (-1 / (1 + sec(x)))

for x in range(1, 15):
    print("First: %f" % first(-x), " | Second: %f" % second(-x), " | 10^(-%d)" %x)
