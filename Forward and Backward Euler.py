#This program computes functions using the forward and backward Euler methods .

## forward Euler
## We have, dx/dt = x(t + \delta t) - x(t) / \delta t = f(x(t))

#### Implementing for dx/dt = 2x ; x(0) = 1
#### Fix the time range let it be t=0 to t=100
import numpy as np
import matplotlib.pyplot as plt
import math as m
time = np.linspace(0,4,50)

#### Fix the initial conditions and create an empty array for other values of x_f(t)
###### Forward Euler
x_f = np.zeros(50)
x_f[0] = 1

#### Fix the initial conditions and create an empty array for values of x_b(t)
###### Backward Euler
x_b = np.zeros(50)
x_b[0] = 1

#### Start iterations for forward Euler x(t + \delta t) = x(t) * (1 + 2*\delta t)
for t in range(1,len(time)):
    x_f[t] = x_f[t-1] + (time[t]-time[t-1])*2*x_f[t-1]

#### Start iterations for Backward euler x(t + \delta t) = x(t) / (1 - 2*\delta t)
for m in range(1,len(time)):
    x_b[m] = x_b[m-1] / (1 - 2*time[m] + 2*time[m-1])

#### Define actual x(t) for the given equation
x_act = np.zeros(50)
for i in range(len(time)):
    x_act[i] = np.exp(2*time[i])


#### Plot x(t) versus t in each forward, backward euler and Analytic cases
plt.plot(time, x_f, label= "Forward Euler")
plt.plot(time, x_b, label= "Backward Euler")
#plt.plot(time, x_act,label="Analytic")
plt.grid(b=None, which='major', axis='both')
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.legend()
plt.show()
