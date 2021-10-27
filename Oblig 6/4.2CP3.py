import numpy as np
import matplotlib.pyplot as plt

rows = 4
cols = 2
data = np.array([1960, 3039585530, 1970, 3707475887, 1990, 5281653820, 2000, 6079603571]).reshape((rows, cols))
#data = np.array([1950, 53.05, 1955, 73.04, 1960, 98.31, 1965, 139.78, 1970, 193.48, 1975, 260.20, 1980, 320.39]).reshape((rows, cols))
#data[:, 0] = data[:, 0] - min(data[:, 0])
#data[:, 1] = np.log(data[:, 1])
#Oppgave a
b = np.zeros((rows, 1))
b = np.log(data[:, 1])
A = np.ones((rows, cols))
#A[:, 0] = 1
A[:, 1] = data[:, 0] - min(data[:, 0])
Q, R = np.linalg.qr(A)
b_1 = Q.T @ b
print("A:\n", A)
#print("A.T:\n", A.T)
#print("Q:\n", Q)
#print("Q.T:\n", Q.T)
#print("R:\n", R)
print("b:\n", b)

ATA = A.T @ A
#print("ATA:\n", ATA)
#print("Cond(R):\n", np.linalg.cond(R))
ATb = A.T @ b
#print("ATb:\n", ATb)
#params = np.linalg.solve(R, b_1)
params = np.linalg.solve(ATA, ATb)
print("Params:\n", params)
start_year = min(data[:, 0]) - 10
end_year = max(data[:, 0]) + 10
t_1 = np.linspace(start_year, end_year, end_year - start_year)
s_func = lambda t: np.exp(params[0]) * np.exp(params[1] * (t - min(data[:, 0])))
estimate_values = s_func(data[:, 0])
plt.plot(data[:, 0], data[:, 1], 'bo')
print("Estimate 1980: ", s_func(1980))
plt.plot(t_1, s_func(t_1))
r = b - A@params
m = len(b)
print("RMSE: ", (np.linalg.norm(b - A@params)) / (np.sqrt(len(b))))
print("Estimation error: ", abs(4304533501 - s_func(1980)))
#print("s_func(b):\n", s_func(b))
#print("s_func(t_1):\n", s_func(t_1))
plt.show()