# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

import numpy as np
from numpy import linalg as la
from scipy.linalg import norm


N = 1000
h = 1/(N+1)
j = []
for int in range(0,N+2):
    j.append(int)

xVec = []
for int in j:
    xVec.append(int*h)


fVec = []
for x in xVec:
    val = 4
    for L in range(0,6):
        val += (((2*x-1)*np.cos(L*np.pi*x)*L*np.pi)+(2*np.sin(L*np.pi*x)))/(L+1)
    fVec.append(val)

kappaPos = []
kappaNeg = []
for x in xVec:
    valKappaPos = 2
    valKappaNeg = 2
    for L in range(0,6):
        valKappaPos += (np.sin(L*np.pi*(x+h/2)))/(L+1)
        valKappaNeg += (np.sin(L*np.pi*(x-h/2)))/(L+1)
    kappaPos.append(valKappaPos)
    kappaNeg.append(valKappaNeg)


fApprox = []
for int in j:
    val = -(int*(int-1))*(kappaPos[int]+kappaNeg[int])+(kappaPos[int]*((int-h)*
    (int+h-1)))+(kappaNeg[int]*((int-h)*(int-h-1)))
    fApprox.append(val/(h**2))


print(abs(norm(fApprox)-norm(fVec)))
# print(fApprox,fVec)
