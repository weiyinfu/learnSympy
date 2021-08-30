import numpy as np
import sympy as sp
from scipy.special import factorial, comb
from tqdm import tqdm

"""
(m-x)(n-x)(k-x)形式的积分
"""
t = sp.symbols("t")


def solve(n):
    a = [sp.numer(i) - t for i in range(1, n + 1)]
    y = sp.prod(a)
    Y = sp.integrate(y, t)
    return Y.evalf(subs={t: 1}) / factorial(n)


def test():
    ans = np.zeros(30)
    for i in tqdm(range(2, len(ans))):
        ans[i] = solve(i)
        print(ans[i])
    import matplotlib.pyplot as plt

    plt.plot(ans[2:])
    plt.show()


test()
