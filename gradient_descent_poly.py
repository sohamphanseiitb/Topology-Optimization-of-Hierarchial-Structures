# Author: Soham S. Phanse
# Roll number: 19D170030
# Department of Aerospace Engineering, IIT Bombay
# Project Name: Topology Optimization of Hierarchial Structures
# Project Supervisor: Prof. Amuthan Ramabathiran

# This program takes an input of polynomial co-efficients of any degree.
# It provides the minimum value of the polynomial and is based on the -
# Gradient Descent for Polynomials

import numpy as np
import matplotlib.pyplot as plt

#Stores the co-efficents of the polynomial in an array in the descending degree order
poly = np.array([1,5,0]) #refers to x*x + 1

#Also, we need to mention the interval where we need the solution.
# Like, if we want the solution to be x>0.
upper_limit, lower_limit = 1,-1
step_counter, iteration_number, flag_counter = 0, 1000, 0
#Calculates the value of the polynomial at x
def polyf(x, polynomial):
    sum = 0
    for i in range(len(polynomial)):
        sum = sum + polynomial[i]*(x**(len(polynomial)-i-1))
    return sum

# Differentiates the polynomial and gives output as a array
# of co-efficents of the differentiated polynomial
def diff(polynomial):
    difpoly = []
    for i in range(len(polynomial)-1):
        difpoly.append(poly[i]*(len(polynomial)-i-1))
    return difpoly

#Now, we write the general gradient descent polynomial algorithm.
# x(k+1)= x(k) - (alpha*f'(x(k)))
alpha = 0.1
x_ini = -1 # Lets take an initial guess as a candidate solution

#This function gives the next iterative value of the argument minimizer
def nextval(x):
    return x - alpha*polyf(x, diff(poly))

while True:
    x_next = nextval(x_ini)
    if abs(x_next-x_ini)<0.001:
        print("The iterative solutions are converging.\n The Solution is:", x_next, "\n The value of polynomial at the minimizing argument is:", polyf(x_next, poly))
        break
    step_counter = step_counter + 1
    if step_counter>iteration_number:
        print("The iteration number has crossed", iteration_number)
    if flag_counter==0:
        if x_next<lower_limit or x_next>upper_limit:
            print("The iterative value has violated the domain restrictions. \n The computed solution will be out of the domain.")
            flag_counter = 1
    if polyf(x_next, poly)<polyf(x_ini, poly):
        x_ini = x_next
    else:
        #This step takes care of convergence of the solutions.
        if abs(int(x_ini)-x_ini)<0.001:
            print("The minimizing argument is: ", int(x_ini))
            print("The minimum value of the polynomial at",x_ini,"is: ", polyf(int(x_ini), poly))
        else:
            print("The minimum value of the polynomial at",x_ini,"is: ", polyf(x_ini, poly))
            print("The minimizing argument is: " , x_ini)
        break
