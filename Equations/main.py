from math import sin
from bisect import Bisect
from secant import Secant
from bruteforce import Bruteforce


def f(x):
    return x**2 + 4*sin(x)


left = int(input('Enter left border: '))
right = int(input('Enter right border: '))
n = int(input('Enter number of points: '))

bf = Bruteforce(left, right, n, func)
bf.FirstStep()
bf.plots()

s1 = Secant.find(f, a=-2, b=-1)
s2 = Secant.find(f, a=-1, b=1)
b1 = Bisect.find(f, a=-2, b=-1)
b2 = Bisect.find(f, a=-1, b=1)

print("Secant: {} {}".format(s1, s2))
print("Bisect: {} {}".format(b1, b2))