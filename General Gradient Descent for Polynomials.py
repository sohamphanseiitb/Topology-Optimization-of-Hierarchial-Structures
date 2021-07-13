# Now we generalize the method we have learnt for polynomials.
# Lets first construct the differentaition of a polynomial
import numpy as np
import matplotlib.pyplot as pyplot
n = 2
degree = n
coeff = [1,2,1]
# This function differentiates the polynomial and
# supplies the new coefficients
def differentiate(initial_coefficient_array):
    differentiated_coefficient_array = []
    exponent = n
    for each in initial_coefficient_array:
        new_coeff = exponent*each
        differentiated_coefficient_array.append(new_coeff)
        exponent = exponent - 1
    return differentiated_coefficient_array

#Thsi function evaluates the value of the polynomial at any given argument
# by taking the array of the co-coefficients of the polynomial
def evaluate(coeff_array, arg):
    poldegree2 = len(coeff_array)
    sum = 0
    for each in coeff_array:
        exponent = len(coeff_array) - coeff_array.index(each)
        sum = sum + each*(arg**exponent)
    return sum

# Now, lets start with the gradient descent
alpha = 0.01 #Set some alpha as a small number
initial = -1#Set some value as the initial answer
boolval = 1 # Set it equal to zero if you want to find maximum
argvals = []
while True:
    next = initial - alpha*evaluate(differentiate(coeff),initial)
    if boolval==1:
        if evaluate(differentiate(coeff),next)<evaluate(differentiate(coeff),initial):
            initial = next
            print(next)
            argvals.append(next)
        else:
            break
#    else:
#        if evaluate(differentiate(coeff),next)>=evaluate(differentiate(coeff),initial):
#            next = initial
#            argvals.append(next)
#        else:
#            break
print(argvals)
