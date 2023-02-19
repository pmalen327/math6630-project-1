# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import norm


# mesh points
N=10

h=1/(N+1)

j = []
for i in range(0,N+2):
    j.append(i)

x = []
for i in j:
    x.append(i*h)

def f(x):
    val = 4
    for L in range(1,6):
        val += ((2*x-1)*(np.cos(L*np.pi*x)*L*np.pi)-2*(np.sin(L*np.pi*x)))/(L+1)
    return val

fVec = []
for i in range(0, len(j)):
    fVec.append(f(x[i]))

def u(x):
    return((x**2)-x)


def diff(func,var):
    numerator = (func(*var+h/2))-(func(*var-h/2))
    denom = h/2
    return(numerator/denom)


def kappa(x):
    val = 2
    for L in range(0,6):
        val += (np.sin(np.pi*L*x))/(1+L)
    return val


def laplace(var):
    arg = kappa(*var)*diff(u,*var)
    return(diff(arg,*var))

sol = []
for i in range(0, len(j)):
    sol.append(laplace(x[i]))

print(f,sol)


















