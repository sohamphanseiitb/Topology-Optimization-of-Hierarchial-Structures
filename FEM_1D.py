import numpy as np
import matplotlib.pyplot as plt

# Setting up the grid-----------------------------------------------------------
x = np.linspace(0,1,100)
h = x[1] - x[0]

# Forcing function
def Forcing(arg):
    return np.sin(arg)

#-------------------------------------------------------------------------------
# Now, we construct the basis functions or the shape and shape derivative
# functions.
def shape(i,arg):
    if i==0:
        if arg<x[i]:
            return 0
        elif x[i]<=arg and arg<x[i+1]:
            return (x[i+1]-arg)/h
        elif x[i+1]<=arg:
            return 0
    elif i==99:
        if arg<x[i-1]:
            return 0
        elif arg>=x[i-1] and arg<x[i]:
            return (arg - x[i-1])/h
        elif arg>=x[i]:
            return 0
    elif i>0 and i<99:
        if arg<x[i-1]:
            return 0
        elif x[i-1]<=arg and arg<x[i]:
            return (arg - x[i-1])/h
        elif x[i]<=arg and arg<x[i+1]:
            return (x[i+1]-arg)/h
        elif arg>=x[i+1]:
            return 0
#-------------------------------------------------------------------------------

# Now, we define derivatives of the shape function
def shapederi(i,arg):
    if i==0:
        if arg<x[i]:
            return 0
        elif x[i]<=arg and x[i+1]<arg:
            return 1/h
        elif x[i+1]<arg:
            return 0
    elif i==99:
        if arg<x[i-1]:
            return 0
        elif arg>=x[i-1] and arg<x[i]:
            return 1/h
        elif arg>x[i]:
            return 0
    elif i>0 and i<99:
        if arg<x[i-1]:
            return 0
        elif arg>=x[i-1] and arg>x[i]:
            return 1/h
        elif x[i]<=arg and arg<x[i+1]:
            return -1/h
        elif arg>=x[i+1]:
            return 0
#-------------------------------------------------------------------------------
def eulerintder(lower, upper, index1=0, index2=0):
#Let's fix number of divisions d = 1000
    d = np.linspace(lower, upper,1000)
    dx = d[2] - d[1]
    sum = 0
    for i in range(0,len(d)-1):
        sum = sum + (shapederi(index1,d[i])*shapederi(index2,d[i])*dx)
    return sum

def eulerint(lower, upper, index1):
    d = np.linspace(lower, upper, 1000)
    dx = d[2] - d[1]
    summ = 0
    for i in range(0,len(d)-1):
        summ = summ + (shape(index1, d[i])*Forcing(d[i])*dx)
    return summ

#Now, lets construct the stress matrix as follows
def matrixentry(i,j):
    return eulerintder(0,1)

def matrixentries(i,j):
    if i==j:
        return 2/h
    elif abs(i-j)==1:
        return -1/h
    else:
        return 0

def colentries(i):
    return eulerint(0,1,i)

matrix, row = [], []
for i in range(0,99):
    for j in range(0,99):
        row.append(matrixentries(i,j))
    matrix.append(row)
    row = []

unknown = []
for i in range(0,99):
    unknown.append(colentries(i))

#Now, lets us find the matrix inverse
inverse = np.linalg.inv(matrix)
vector = np.dot(inverse, unknown)

# Now, we have the co-efficients in th vector and we will use these to prepare linear
## combinations with shape functions.
def LC(arg):
    summm = 0
    for i in range(0,99):
        summm = summm + unknown[i]*shape(i,arg)
    return summm

# Now, we use the above function to find the value of the approximate
# solution at every argument between 0 and 1
to_plot = []
for every in x:
    store = LC(every)/h
    to_plot.append(store)

plt.plot(x,to_plot,label="Approximate solution")
plt.plot(x,np.sin(x),label="Actual Solution")
plt.xlabel("Values of x \u2193")
plt.ylabel("Values of function")
plt.title("Galerkin Approximate FEM in 1D")
plt.legend()
plt.show()
