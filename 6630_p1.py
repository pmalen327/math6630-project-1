# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023


import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import scipy.sparse.linalg  as la
from scipy.linalg import norm


# number of points in mesh
# will loop over this later, just using 100 for the initialization
N = 10

# this is strictly for plotting, but ofc that shit is bugged too
noN = list(range(1,N+1))


# step size
h = 1/(N+1)


# steps
j = []
for i in range(1,N+1):
    j.append(i)



# x values at each j
# for x in [0,1]
x = [0]
for i in j:
    x.append(i*h)
x.append(1)    



# kappa values at each j
kappa = []
for index in range(0,len(j) + 2):
    val = 2
    for L in range(1,6):
        val += 1/(L+1)*np.sin(L*x[index]*np.pi)
    kappa.append(val)

# f values at each j
f = []
for index in range(0,len(j) + 2):
    val1 = -4
    for L in range(1,6):
        val1 += -2*(1/(L+1)*np.sin(L*x[index]*np.pi))
    val2 = -2*x[index]+1
    for L in range(1,6):
        val2 += (1/(L+1)*np.cos(L*x[index]*np.pi))*L*np.pi

    f.append(val1+val2)








