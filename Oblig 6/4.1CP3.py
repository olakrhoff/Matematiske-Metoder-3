import numpy as np
import matplotlib.pyplot as plt

data = np.array([1960, 3039585530, 1970, 3707475887, 1990, 5281653820, 2000, 6079603571]).reshape((4, 2))

#Oppgave a
b = np.zeros((4, 1))
b = data[:, 1]
A = np.ones((4, 2))
#A[:, 0] = 1
A[:, 1] = data[:, 0]
Q, R = np.linalg.qr(A)
b_1 = Q.T @ b
#print("b_1:\n", b_1)
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
s_func = lambda t: params[0] + params[1] * t
estimate_values = s_func(data[:, 0])
plt.plot(data[:, 0], data[:, 1], 'bo')
plt.plot(t_1, s_func(t_1))
print("Estimate 1980: ", s_func(1980))
r = b - A@params
m = len(b)
print("RMSE: ", (np.linalg.norm(b - A@params)) / (np.sqrt(len(b))))
#print("s_func(b):\n", s_func(b))
#print("s_func(t_1):\n", s_func(t_1))
print("Estimation error: ", abs(4304533501 - s_func(1980)))
plt.show()


#Oppgave b

b = np.zeros((4, 1))
b = data[:, 1]
A = np.ones((4, 3))
#A[:, 0] = 1
A[:, 1] = data[:, 0] - min(data[:, 0])
A[:, 2] = (data[:, 0] - min(data[:, 0]))**2
Q, R = np.linalg.qr(A)
b_1 = Q.T @ b
#print("b_1:\n", b_1)
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
#params = np.linalg.lstsq(ATA, ATb)[0]
print("Params:\n", params)

start_year = min(data[:, 0]) - 10
end_year = max(data[:, 0]) + 10
t_1 = np.linspace(start_year, end_year, end_year - start_year)
s_func = lambda t: params[0] + params[1] * (t  - min(data[:, 0])) + params[2] * (t - min(data[:, 0]))**2
plt.plot(data[:, 0], data[:, 1], 'bo')
plt.plot(t_1, s_func(t_1))
print("Estimate 1980: ", s_func(1980))
print("RMSE: ", (np.linalg.norm(b - A@params)) / (np.sqrt(len(b))))
print("Estimation error: ", abs(4304533501 - s_func(1980)))
#print("s_func(b):\n", s_func(b))
plt.show()