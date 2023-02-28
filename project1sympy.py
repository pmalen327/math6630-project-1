# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

import numpy as np
from numpy import linalg as la
from scipy.linalg import norm



N = 10
h = round(1/(N+1),5)
j = []
for int in range(0,N+2):
    j.append(int)

xVec = []
for int in j:
    xVec.append(round(int*h,5))


fVec = []
for x in xVec:
    val1 = 8
    val2 = 0
    val3 = 0
    for L in range(1,6):
        val2 += 2*(np.sin(L*np.pi*x))/(L+1)
        val3 += ((2*x-4)*(np.cos(np.pi*L*x))*L*np.pi*x)/(L+1)
    fVec.append(val1+val2+val3)



kappaPos = [2.3 for i in range(0,len(xVec))]
kappaNeg = [2 for i in range(0,len(xVec))]

# for x in xVec:
#     valKappaPos = 2
#     valKappaNeg = 2
#     for L in range(1,6):
#         valKappaPos += (np.sin(L*np.pi*(x+h/2)))/(L+1)
#         valKappaNeg += (np.sin(L*np.pi*(x+h/2)))/(L+1)
#     kappaPos.append(valKappaPos)
#     kappaNeg.append(valKappaNeg)

# THIS IS THE PROBLEM
# fukkkkkkkkkkkkkkkkk
fApprox = []
for index in range(0, len(xVec)):
    val = 0
    uInit = (index*(index-1))
    uNeg = (index-h)*(index-h-1)
    uPos = (index+h)*(index+h-1)
    val += -(uInit*(kappaPos[index]+kappaNeg[index])) + (kappaPos[index]*uPos) + (kappaNeg[index]*uNeg)
    fApprox.append(round(val/(h**2),5))


# print(fApprox,fVec)
print(xVec,fVec,fApprox)