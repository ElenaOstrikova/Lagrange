import numpy as np
from math import cos

from bisect import Bisect
from secant import Secant
from bruteforce import Bruteforce
from newton import Newton


def f(x):
    return x**2 + 4*np.sin(x)


left = int(input('Enter left border: '))
right = int(input('Enter right border: '))
n = int(input('Enter number of points: '))

bf = Bruteforce(left, right, n, f)
bf.FirstStep()
bf.plots()

s1 = Secant.find(f, a=-2, b=-1)
s2 = Secant.find(f, a=-1, b=1)
b1 = Bisect.find(f, a=-2, b=-1)
b2 = Bisect.find(f, a=-1, b=1)

print("\nSecant: {} {}".format(s1, s2))
print("Bisect: {} {}".format(b1, b2))


def dfunc(x):
    return 2*x + 4*cos(x)


newton = Newton(f, dfunc, x=2, max_iterations=50, eps=10e-7)
root = newton.calculate()

print("Newton: {}".format(root))
