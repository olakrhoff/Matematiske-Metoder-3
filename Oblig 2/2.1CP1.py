import numpy
from numpy import *

def gauss(m, rows, coloums):
    for i in range(0, coloums - 1):
        for j in range(i + 1, rows):
            if (m[i, i] == 0):
                print("Zero on digaonal")
                return
            multi = m[j, i] / m[i, i]

            for k in range(i, coloums):
                m[j, k] -= multi * m[i, k]

    for i in range(coloums - 2, -1, -1):
        for j in range(i - 1, -1, -1):
            multi = m[j, i] / m[i, i]
            m[j, i] -= multi * m[i, i]
            m[j, coloums - 1] -= multi * m[i, coloums - 1]

    for i in range(0, rows):
        m[i, coloums - 1] = m[i, coloums - 1] / m[i, i]
        m[i, i] /= m[i, i]

    return m

a = numpy.matrix('2.0, -2, -1, -2; 4, 1, -2, 1; -2, 1, -1, -3')
b = numpy.matrix('1.0, 2, -1, 2; 0, 3, 1, 4; 2, -1, 1, 2')
c = numpy.matrix('2.0, 1, -4, -7; 1, -1, 1, -2; -1, 3, -2, 6')

print(a)
print(gauss(a, 3, 4))
print()
print(b)
print(gauss(b, 3, 4))
print()
print(c)
print(gauss(c, 3, 4))
