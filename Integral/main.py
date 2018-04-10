import numpy as np
from integral import Integral


def fn(x):
    return np.sqrt(x + 1) * np.tan(x + 3)

# a = int(input('Enter left border: '))
# b = int(input('Enter right border: '))
# n = int(input('Enter number of points: '))

I = Integral(fn, 0.15, 0.63)

rectMid = I.rectangles()
rectLeft = I.rectangles('l')
rectRight = I.rectangles('r')
trapezoid = I.trapezoid()
simpson = I.Simpson()

value = 0.157469

print('\nMiddle rectangles: {}; error: {}'.format(rectMid, value - rectMid))
print('Left rectangles: {}; error: {}'.format(rectLeft, value - rectLeft))
print('Middle rectangles: {}; error: {}'.format(rectRight, value - rectRight))
print('Keystones: {}; error: {}'.format(trapezoid, value - trapezoid))
print('Simpson: {}; error: {}'.format(simpson, value - simpson))
