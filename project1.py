# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

import numpy as np
from scipy.linalg import norm
import matplotlib.pyplot as plt

# Nvec = []
# errorVec = []
# for N in range(10, 1000, 100):
#     Nvec.append(N)

N = 1000
h = round(1/(N+1),5)
j = []
for int in range(0,N+2):
    j.append(int)

xVec = []
for int in j:
    xVec.append(round(int*h,5))

fVec = []
for x in xVec:
    sum = 4
    for L in range(1,6):
        sum += ((2*np.sin(L*np.pi*x))+((2*x-1)*np.cos(L*np.pi*x)*L*np.pi*x))/(L+1)
    fVec.append(round(sum,5))
    
kappaPos = []
kappaNeg = []
for x in xVec:
    valKappaPos = 2
    valKappaNeg = 2
    for L in range(1,6):
        valKappaPos += (np.sin(L*np.pi*(x+h/2)))/(L+1)
        valKappaNeg += (np.sin(L*np.pi*(x-h/2)))/(L+1)
    kappaPos.append(round(valKappaPos,5))
    kappaNeg.append(round(valKappaNeg,5))
# print(kappaNeg)
# print(kappaPos)

fApprox = []
for index in range(0, len(xVec)):
    uInit = -(xVec[index]**2) + xVec[index]
    uPos = ((xVec[index]+h)**2)-xVec[index]-h
    uNeg = ((xVec[index]-h)**2)-xVec[index]+h
    val = uInit*(kappaPos[index]+kappaNeg[index])+(kappaPos[index]*uPos)+(kappaNeg[index]*uNeg)
    fApprox.append(round(val/(h**2),5))


# print(fVec,fApprox)

# LTE = []
# for i in range(0,len(fVec)):
#     LTE.append(fApprox[i]-fVec[i])
# errorVec.append(norm(LTE))

# print(Nvec,errorVec)

# we want to look at the norm of the LTE as N grows
fig,ax = plt.subplots()
ax.plot(j,fVec, label = "True f(x)")
ax.plot(j,fApprox, label = "Approximated f(x)")
ax.set(xlabel='j', ylabel= "f(x)")
leg = plt.legend(loc='upper right')
plt.show()





