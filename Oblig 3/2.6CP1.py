import numpy as np

def ConjugateGradientMethod(x0, A, b):
    n = x0.size
    d = b - A * x0
    r0 = d
    x = x0

    for i in range(n):
        if (np.all((r0 == 0))):
            return x, i

        alpha = (np.transpose(r0) * r0) / (np.transpose(d) * A * d)
        x = x + np.multiply(alpha, d)
        r1 = r0 - np.multiply(alpha, A * d)
        beta = (np.transpose(r1) * r1) / (np.transpose(r0) * r0)
        d = r1 + np.multiply(beta, d)
        r0 = r1

    return x, n


Aa = np.matrix("1, 0; 0, 2")
ba = np.matrix("2; 4")
x0a = np.matrix("0; 0")

Ab = np.matrix("1, 2; 2, 5")
bb = np.matrix("1; 1")
x0b = np.matrix("0; 0")

xa, na = ConjugateGradientMethod(x0a, Aa, ba)
xb, nb = ConjugateGradientMethod(x0b, Ab, bb)

print("Iterasjoner: ", na)
print(xa)

print("Iterasjoner: ", nb)
print(xb)
