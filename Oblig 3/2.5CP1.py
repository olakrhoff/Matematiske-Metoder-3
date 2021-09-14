import numpy
import scipy.sparse
import scipy.sparse as sp
import scipy.sparse.linalg as spLin


def makeMatrix2(n):
    if (n % 2 != 0):
        raise ValueError("Må være partall")
    A = numpy.matrix([[0.0 for x in range(n)] for y in range(n)])
    numpy.fill_diagonal(A, 3)

    for i in range(1, n):
            A[i, i - 1] = -1
            A[i - 1, i] = -1

    b = numpy.ones(n) * 1.0
    b[0] = 2
    b[-1] = 2

    return A, b

def makeMatrix(n):
    if (n % 2 != 0):
        raise ValueError("Må være partall")
    data = numpy.array([[-1], [0], [-1]]) @ numpy.ones([1, n])
    offset = numpy.array([-1, 0, 1])
    R = sp.dia_matrix((data, offset), shape=(n, n))
    R = R.tolil()

    data = numpy.array([[1 / 3]]) @ numpy.ones([1, n])
    offset = numpy.array([0])
    D = sp.dia_matrix((data, offset), shape=(n, n))

    b = numpy.ones(n) * 1
    b[0] = 2
    b[-1] = 2

    return R, D, b


def Jacobi(R, d_inv, b, num_itr):
    n = b.size
    x = numpy.zeros(n)

    for j in range(num_itr):
        t = R * x

        for i in range(n):
            if (t[i] != 0 or b[i] != 0):
                t[i] = b[i] - t[i]

        x = d_inv * t

        if (forwardError(numpy.array([1.0 for x in range(n)]), x, 0.0000005)):
            return backwardError(x), j
    return backwardError(x), num_itr


def forwardError(x, xA, t):
    max = -1.0
    for i in range(x.size):
        if (abs(x[i] - xA[i]) > max):
            max = abs(x[i] - xA[i])

    return max < t

def backwardError(xA):
    n = xA.size
    data = numpy.array([[-1], [3], [-1]]) @ numpy.ones([1, n])
    offset = numpy.array([-1, 0, 1])
    A = sp.dia_matrix((data, offset), shape=(n, n))
    A = A.tolil()

    b = numpy.ones(n) * 1
    b[0] = 2
    b[-1] = 2

    t = A * xA

    max = -1.0

    for i in range(n):
        if (abs(b[i] - t[i]) > max):
            max = abs(b[i] - t[i])

    return max



num_itr = 100
R, D_inv, b = makeMatrix(num_itr)
x0 = 1
print(R.toarray())
print(D_inv.toarray())
print(b)

print()

x, n = Jacobi(R, D_inv, b, num_itr)

print("Iterasjoner: ", n)
print("Backward error: ", x)
