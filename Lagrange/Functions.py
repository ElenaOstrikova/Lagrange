import numpy as np


def lagrange(xfunc, x, y, n):
    res = 0

    for i in range(n + 1):
        a = 1
        b = 1
        for j in range(n + 1):
            if i != j:
                a = a * (xfunc - x[j])
                b = b * (x[i] - x[j])
        res = res + y[i] * a / b

    return res
