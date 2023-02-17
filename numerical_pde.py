# Math 6630 Project 1
# Preston Malen \\ u0984531 



import numpy as np
import pde
from sympy import *

x1, x2 = symbols('x1 x2')
X = Matrix([x1,x2])
k = symbols('k')
k += 2


# kappa of X
for i in range(1,4):
    for j in range(1,4):
        k += 1/((1+i)*(1+j)) * sin(i*pi*x1) * sin(j*pi*x2)

# Defining the mesh size and bounds
grid = pde.CartesianGrid([[0,1],[0,1]], [2,2])
field = pde.ScalarField(grid)
field.laplace("dirichlet")

# Defining equation
eq = pde.PDE({"u": "gradient(k)*laplace(u)"})


# need to parameterize kappa
# result = eq.solve(field, t_range=10, dt=1e-2)

