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

a = numpy.matrix('1.e-20, 1, 1; 1, 2, 4') #If we had allowed line switching the correct answer could have been given
b = numpy.matrix('1, 2, 4; 1.e-20, 1, 1') #If we had allowed line switching the correct answer could have been given

print("\n\n", gauss(a, a.shape[0], a.shape[1]))
print("\n\n", gauss(b, b.shape[0], b.shape[1]))