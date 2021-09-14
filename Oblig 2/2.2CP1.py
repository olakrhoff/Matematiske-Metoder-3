import numpy


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


a = numpy.matrix('3., 1, 2; 6, 3, 4; 3, 1, 5')
b = numpy.matrix('4., 2 ,0; 4, 4, 2; 2, 2, 3')
c = numpy.matrix('1., -1, 1, 2; 0, 2, 1, 0; 1, 3, 4, 4; 0, 2, 1, -1')

La, Ua = LUfactor(a)
Lb, Ub = LUfactor(b)
Lc, Uc = LUfactor(c)

print("L:\n", La, "\nU:\n", Ua)
print("L:\n", Lb, "\nU:\n", Ub)
print("L:\n", Lc, "\nU:\n", Uc)
