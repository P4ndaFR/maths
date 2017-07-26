"""Differential Equations Resolution."""
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols, exp
from sympy.abc import x

# Definitions
A, B, C = symbols('A B C')
y = Function('f')

# Initialisation
A = int(input('A ?'))
B = int(input('B ?'))
C = int(input('C ?'))

# Processing Equation
s0 = dsolve(A*Derivative(y(x), x, x) + B*Derivative(y(x), x) + C*y(x), y(x))

# Result
print(s0)
