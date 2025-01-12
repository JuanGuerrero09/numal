from typing import Callable
import numpy as np
import sympy as smp

narr = [1, 3, 5, 7, 9]

# 1.1 Algorithms


def stat_alg(arr):
    xsum = 0
    x2sum = 0
    n = len(arr)
    for i in range(0, n):
        xsum = xsum + narr[i]
        x2sum = x2sum + pow(narr[i], 2)
    xbar = xsum / n
    s = np.sqrt(((n * x2sum) - pow(xsum, 2)) / (n * (n - 1)))
    return xbar, s


def trapezoidal_integral(a, b, func: Callable, n=10):
    h = (b - a) / n
    sum = 0
    for i in range(1, n):
        sum = sum + func(a + i * h)
    sum = sum * 2
    sum = sum + func(a) + func(b)
    return (h / 2) * sum


def check_integral(a, b, func: Callable):
    x = smp.symbols("x", real=True)
    #    print(smp.integrate(func, x))
    int_syp = smp.integrate(func(x), (x, a, b))
    int_trap = trapezoidal_integral(a, b, func)
    print("Diference between integrals")
    print(f"Symbolic: {int_syp}")
    print(f"Trapezoidal: {int_trap}")
    abs_dif = abs(int_syp.evalf() - int_trap)
    err = abs_dif / int_syp.evalf()
    print(f"Dif {abs_dif}, err {round(err * 100, 2)}%")


def f(x):
    return 1 / x


def apprx_root(a, x1, e, Nmax):
    x0 = x1
    for i in range(0, Nmax):
        print(x1)
        x1 = (x0 + (a / x0)) / 2
        if abs(x0 - x1) < e:
            return x1
        x0 = x1
    else:
        return f"Max num of iterations {Nmax} reached, no solution obtained"


# print(stat_alg(narr))
# print(trapezoidal_integral(1, 2, f, 4))
# print(apprx_root(2, 2, 0.005, 10))
# check_integral(1, 2, f)
#
