"""Differential Equations Resolution."""
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols, exp
from sympy.abc import x

# Definitions
A, B, C = symbols('A B C')
y = Function('f')

# ESSM
print("Enter coefficient from your Differential Equation (Ay''(x)+By'(x)+Cy(x))")

A = int(input('A ? > '))
B = int(input('B ? > '))
C = int(input('C ? > '))

# Processing ESSM
eq = (Eq(A*Derivative(y(x), x, x) + B*Derivative(y(x), x) + C*y(x), y(x)))
s0 = dsolve(eq)

# Result ESSM
print(s0)
