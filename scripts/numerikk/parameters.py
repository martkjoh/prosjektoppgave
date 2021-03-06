# This file must be run once to generate the requisite files
import numpy as np
from numpy import pi, sqrt
import sympy as sp
from scipy.integrate import quad, quadrature


# The parameter space of mu and alpha
n = 201
mu_list = np.linspace(0., 2.5, n)
a_list = np.linspace(0, pi, n)

MU, A = np.meshgrid(mu_list, a_list)


# LEO constants
MPI = 131   # The only dimensionfull constant, defining units of the system
fpi = 128 / np.sqrt(2) / MPI
l1 = -0.4
l2 = 4.3
l3 = 2.9
l4 = 4.4


m = sp.symbols("m")
f = sp.symbols("f")

eq1 = m**2 *(1 - m**2 * l3 / (f**2 * 2*(4 * pi)**2)) - 1**2
eq2 = f**2 *(1 + 2 * m**2 * l4 / (f**2 * (4 * pi)**2)) - fpi**2


# Find nlo solution for mbar and f
sol = sp.solve([eq1, eq2], m, f)
sol = [s for s in sol if (np.abs(s[0]) == s[0]) and (np.abs(s[1]) == s[1])]

mbar_nlo = sol[0][0]
f_nlo = sol[0][1]

# Numerical integraiotr for F_fin

# Much slower method, more accurate
integral = lambda f: (
    lambda *args: quad(f, 0, 50, args=args, epsabs=1e-5, epsrel=1e-5)[0]
    )

# integral = lambda f: (
#     lambda *args: quadrature(f, 0, 10, args=args, maxiter=1000, tol=1e-5)[0]
#     )



if __name__ == "__main__":
    # Print parameters

    print(fpi*MPI)
    print(mbar_nlo)
    print(f_nlo)
    print(MPI*mbar_nlo)
    print(MPI*f_nlo)
