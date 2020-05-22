from sympy import *

"""
这是一个多项式积分，按理说应该是有解的，但是sympy却非常慢
"""
x = symbols('x')
y = integrate(sin(x) ** 2 / (1 + sin(x) ** 4), [x, -pi / 2, pi / 2])
print(y)
