# Math 6630 Project 1
# Preston Malen \\ u0984531 
# February 2023

# trying a sympy approach

from sympy import *
import numpy as np

x,h,L = symbols('x h L')

u = x*(x-1)

posDiff = x+h/2
negDiff = x-h/2

uPos = posDiff*(posDiff-1)
uNeg = negDiff*(negDiff-1)

opD = uPos-uNeg/(h/2)


kappaArg = 1/(L+1)*sin(L*np.pi*x)
kappa = 2 + Sum(kappaArg, (L,1,5)).doit()

laplaceArg = kappa*opD
lpPos = laplaceArg + h/2
lpNeg = laplaceArg - h/2
opLaplace = lpPos-lpNeg/(h/2)

# now just need to substitute values
print(opLaplace.subs({x:1, h: 2}))







