# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

# trying a sympy approach
from sympy import *
import numpy as np
from numpy import linalg as la
from math import *


x,h,L = symbols('x h L')

N = 10
h = N + 1
j = []

for num in range(0,N+2):
    j.append(num)

xVec = []
for num in j:
    xVec.append(num/(h))

u = x*(x-1)

# the exact f(x) on the RHS
def f(var):
    val = 4
    for L in range(1,6):
        val += ((sin(L*pi*var)*2) + (2*var-1)*(cos(L*pi*var))*L*pi*var)/h
    return val

fVec = []
for i in xVec:
    fVec.append(f(i))

# kappaArg = sin(L*pi*x)/(L+1)
# kappa = 2 + Sum(kappaArg, (L,1,5)).doit()

term1 = (sin(L*pi*(x+h/2))*(x+h/2-1))/(L+1)
term2 = -(sin(L*pi*(x-h/2))*(x-h/2-1))/(L+1)

sum1 = Sum(term1, (L,1,5)).doit()
sum2 = Sum(term2, (L,1,5)).doit()
laplaceOp = 2 + ((sum1-sum2)/h)




# now just need to substitute values
sol = []
for num in xVec:
    sol.append(laplaceOp.subs(x,num))
sol = np.array(sol, dtype=np.float64)


# LTE = abs(la.norm(sol)-la.norm(fVec))
print(fVec)




