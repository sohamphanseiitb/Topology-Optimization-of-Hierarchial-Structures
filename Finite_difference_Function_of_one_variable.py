
# we have to use the finite difference methods for u"(x) + sin(x). We have the domain of of [0,1].
import numpy as np
import math as m
import matplotlib.pyplot as plt
# Specify the number of divisions and tolerance values
N, eps = 10, 0.001

# Specify the boundary conditions
u_0, u_1 = 0, 0

# Set up the functions
X = np.linspace(0.1,0.9,9)
Y = np.zeros(9)
for i in range(1,9):
    Y[i] = m.sin(X[i])
M = np.zeros([9,9])

for i in range(0,9):
    for j in range(0,9):
        if i==j:
            M[i,j] = 2
        elif abs(i-j)==1:
            M[i,j] = -1

M_1 = np.linalg.inv(M)
u_vals = np.dot(M_1,Y)
plt.plot(u_vals)
plt.show()
#start = int(input("Specify the lower constraint of the domain"))
#end = int(input("Specify the upper constraint of the domain"))
#N = int(input("Number of Intervals between the specified domain")
#eps = float(input("Specify the error constraint"))
