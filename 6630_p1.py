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
N = 100

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

# finding x_j +/- h/2 for the LTE
posDiff = []
negDiff = []
for num in x:
    posDiff.append(num + (h/2))
    negDiff.append(num - (h/2))


# kappa values at each j
kappa = []
for index in range(0,len(j) + 2):
    val = 2
    for L in range(1,6):
        val += 1/(L+1)*np.sin(L*x[index]*np.pi)
    kappa.append(val)


# setting up linear system Au=F

# set the function f(x) here
# chose this randomly for now, still need to find the "exact" solution, tbh I am
# still confused as hell on how to do that
def f(x):
    return(x**3)

# we will store the f(x) values in F
F = []

for num in j:
    F.append(f(x[num]))


diag = []
rows = []
cols = []

# diagonal elements
for num in j:
    val = -(kappa[num+1]+kappa[num-1])
    diag.append(val)


# off diagonal elements
for num in range(0,len(j)-2):
    val = kappa[num+1]
    rows.append(val)

for num in range(0,len(j)-2):
    val = kappa[num-1]
    cols.append(val)

A = sp.diags([diag,rows,cols], [0,2,-2])
A = sp.csr_matrix(A)
A = A*(4/h**2)


# converging faster for smaller N? dafuq is going on, I definitely did something
# wrong, the scheme SEEMS gtg but the code might be iffy

# solving Au = F for u
sol = la.spsolve(A,F)
# print(sol)


# calculating the LTE
Au = A*sol

# this isn't the actual way to do LTE, just a placeholder
# LTE = norm(F-Au)
# print(LTE)


# this not working rn wtf

# fig, ax = plt.subplots()
# plt.plot(noN,F, color='red')
# plt.plot(noN,Au, color='blue')
# plt.ylim(0,1)
# # plt.autoscale(enable=True, axis='both', tight=None)
# # plt.yscale("logit")
# ax.set(xlabel='time', ylabel='val',
#        title='True vs. Approximate Solution')
# plt.show()





