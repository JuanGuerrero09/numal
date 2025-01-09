import numpy as np

n = [2, 4, 5, 6, 7]


def mean(arr):
    xsum = 0
    x2sum = 0
    n = len(arr)
    for xi in range(0, n + 1):
        xsum = xsum + xi
        x2sum = x2sum + (xi * xi)
    xbar = xsum / n
    return xbar


print(mean(n))
