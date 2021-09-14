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

def LUfactor(m):
    U = numpy.matrix(m)
    cols = U.shape[1]
    rows = U.shape[0]
    L = numpy.matrix([[0. for x in range(cols)] for y in range(rows)])
    numpy.fill_diagonal(L, 1)

    for i in range(0, cols):
        for j in range(i + 1, rows):
            if (U[i, i] == 0):
                print("Zero on digaonal")
                return
            multi = U[j, i] / U[i, i]
            L[j, i] = multi

            for k in range(i, cols):
                U[j, k] -= multi * U[i, k]


    return L, U

def backSub(L, U, b):
    #Solve Lc = b first
    cols = U.shape[1]
    rows = U.shape[0]
    c = numpy.matrix([[0. for x in range(1)] for y in range(rows)])
    Lcb = numpy.matrix([[0. for x in range(cols + 1)] for y in range(rows)])
    for i in range(rows):
        for j in range(cols):
            Lcb[i, j] = L[i, j]
    for i in range(rows):
        Lcb[i, cols] = b[i, 0]

    LcbAns = gauss(Lcb, Lcb.shape[0], Lcb.shape[1])

    for i in range(rows):
        c[i, 0] = LcbAns[i, LcbAns.shape[1] - 1]
    #Then solve for Ux = c
    Uxc = numpy.matrix([[0. for x in range(cols + 1)] for y in range(rows)])
    for i in range(rows):
        for j in range(cols):
            Uxc[i, j] = U[i, j]
    for i in range(rows):
        Uxc[i, cols] = c[i, 0]

    UxcAns = gauss(Uxc, Uxc.shape[0], Uxc.shape[1])
    x = b #x and b are the same size
    for i in range(rows):
        x[i, 0] = UxcAns[i, UxcAns.shape[1] - 1]

    return x

def solve(A, b):
    L, U = LUfactor(A)
    return backSub(L, U, b)



a1 = numpy.matrix('3, 1, 2; 6, 3, 4; 3, 1, 5')
b1 = numpy.matrix('0; 1; 3')

a2 = numpy.matrix('4, 2, 0; 4, 4, 2; 2, 2, 3')
b2 = numpy.matrix('2; 4; 6')

print(solve(a1, b1), "\n\n", solve(a2, b2))
