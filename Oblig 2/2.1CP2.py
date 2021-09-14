import numpy

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

def createNxNHilbert(n):
    m = numpy.matrix([[1.0 for x in range (n + 1)] for y in range(n)])

    for i in range(n):
        for j in range(n):
            m[i, j] = 1 / (i + j + 1) #Python er 0 indeksert så må leggge til èn på 'i' og 'j' derfor +1 og ikke -1
    return m

print(createNxNHilbert(2))
print(gauss(createNxNHilbert(2), 2, 3))
print()
print(gauss(createNxNHilbert(5), 5, 6))
print()
print(gauss(createNxNHilbert(10), 10, 11))
