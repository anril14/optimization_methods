# Find the derivative
from sympy import *

x1, x2 = symbols('x1 x2')
expr = x1 ** 2 + 3 * x2 ** 2 + 3 * x1 * x2 - x1 - 2 * x2 - 1
print("Expression : {}".format(expr))

# Use sympy.Derivative() method
expr_diff1 = Derivative(expr, x1)
expr_diff2 = Derivative(expr, x2)

print("Derivative of expression with respect to x1 : {}".format(expr_diff1))
print("Value of the derivative : {}".format(expr_diff1.doit()))

print("Derivative of expression with respect to x2 : {}".format(expr_diff2))
print("Value of the derivative : {}".format(expr_diff2.doit()))
