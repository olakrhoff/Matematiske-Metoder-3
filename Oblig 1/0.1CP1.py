from numpy import *

def nest(c, x, b=[]):
    d = len(c) - 1
    if b == []:
        b = zeros(d)
    y = c[d]
    for i in range(d - 1, -1, -1):
        y *= (x - b[i])
        y += c[i]
    print("ANS: ", y)
    return y


c = ones(51)
c11 = zeros(52)
c11[51] = 1
c11[0] = -1
c12 = [-1, 1]


first = nest(c, 1.00001)
top = nest(c11, 1.00001)
bot = nest(c12, 1.00001)
c2 = top / bot

print("ANS: (x^51 - 1)/(x - 1) = ", c2)

print("Error: ", first - c2)