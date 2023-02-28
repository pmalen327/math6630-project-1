# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

import numpy as np
from numpy import linalg as la
from scipy.linalg import norm


N = 10
h = 1/(N+1)
j = []
for int in range(0,N+2):
    j.append(int)

xVec = []
for int in j:
    xVec.append(int*h)


# THIS IS THE PROBLEM
fVec = []
for x in xVec:
    val1 = 8
    val2 = 0
    val3 = 0
    for L in range(1,6):
        val2 += 2*(np.sin(np.radians(L*np.pi*x)))/(L+1)
        val3 += ((2*x-4)*(np.cos(np.radians(np.pi*L*x)))*L*np.pi*x)/(L+1)
    fVec.append(val1+val2+val3)

# setting kappa as a constant to debug
kappa = 4

# kappaPos = []
# kappaNeg = []
# for x in xVec:
#     valKappaPos = 2
#     valKappaNeg = 2
#     for L in range(0,6):
#         valKappaPos += (np.sin(L*np.pi*(x+h/2)))/(L+1)
#         valKappaNeg += (np.sin(L*np.pi*(x-h/2)))/(L+1)
#     kappaPos.append(valKappaPos)
#     kappaNeg.append(valKappaNeg)


fApprox = []
for int in xVec:
    val = -(int*(int-1))*(kappa+kappa)+(kappa*((int-h)*
    (int+h-1)))+(kappa*((int-h)*(int-h-1)))
    fApprox.append(val/(h**2))


print(fApprox,fVec)