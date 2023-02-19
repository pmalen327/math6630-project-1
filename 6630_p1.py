# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import norm


# starting the fuck over kms
# mesh points
N=10

h=1/(N+1)

j = []
for i in range(0,N+2):
    j.append(i)

x = []
for i in j:
    x.append(i*h)

f = []
for i in x:
    val1 = -4
    for L in range(1,6):
        val1 += -2*(1/(N+1))*np.sin(L*i*np.pi)
        val2 = (-2*i+1)*(1/(N+1))*np.cos(L*i*np.pi)*L*np.pi
    f.append(val1+val2)



kappa = []
for i in x:
    val = 2
    for L in range(1,6):
        val += 1/(L+1)*np.sin(L*np.pi*i)
    kappa.append(val)


# this is fucked
tildeD = []
for i in range(0,len(j)):
    num = -(x[i]+h/2)*(x[i]+h/2-1) + (x[i]-h/2)*(x[i]-h/2-1)
    tildeD.append(num/(h/2)*kappa[i])


# this is fucked
sol = []
for i in range(0,len(j)):
    temp = -(tildeD[i]+h/2)*(tildeD[i]+h/2-1) + (tildeD[i]-h/2)*(tildeD[i]-h/2-1)
    sol.append(temp/(h/2))

print(sol,f)















