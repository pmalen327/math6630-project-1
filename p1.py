# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.linalg import norm
from scipy.sparse.linalg import bicg

Nvec = []
errorVec = []
for N in range(1000, 11000, 1000):
    Nvec.append(N)

    h = round(1/(N+1),5)
    j = []
    for int in range(0,N+2):
        j.append(int)

    xVec = []
    for int in j:
        xVec.append(round(int*h,5))

    uVec = []
    for x in xVec:
        uVec.append(round(x**2-x,5))


    fVec = []
    for x in xVec:
        sum = 4
        for L in range(1,6):
            sum += ((2*np.sin(L*np.pi*x))+((2*x-1)*np.cos(L*np.pi*x)*L*np.pi*x))/(L+1)
        fVec.append(round(sum,5))


    kappaPos = []
    kappaNeg = []
    kappaSum = []
    for x in xVec:
        valKappaPos = 2
        valKappaNeg = 2
        for L in range(1,6):
            valKappaPos += (np.sin(L*np.pi*(x+h/2)))/(L+1)
            valKappaNeg += (np.sin(L*np.pi*(x-h/2)))/(L+1)
        kappaPos.append(round(valKappaPos,5))
        kappaNeg.append(round(valKappaNeg,5))
        kappaSum.append(-round(valKappaNeg+valKappaPos,5))


    A = sparse.dia_matrix((N+2,N+2))
    A.setdiag(kappaPos, k=1)
    A.setdiag(kappaNeg, k=-1)
    A.setdiag(kappaSum)
    A = (1/h**2)*A
    A = sparse.csr_matrix(A)
    u = sparse.linalg.bicg(A,fVec)
    u = u[0]

    LTE = []
    for i in range(0,N+2):
        LTE.append(h*abs(u[i]-uVec[i])**2)
    errorVec.append(norm(LTE))


plt.rcParams['text.usetex'] = True
fig,ax = plt.subplots()
ax.plot(Nvec,errorVec, color = 'red')
ax.set(xlabel='N', ylabel='Local Truncation Error')
ax.set_yscale('log')
plt.xticks(Nvec)
plt.show()