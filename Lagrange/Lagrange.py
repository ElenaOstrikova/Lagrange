import numpy as np
import matplotlib.pyplot as plt
import Functions as fnc

print("Choose the number of points")
n = int(input())
a = 0
b = 2 * np.pi

x = np.linspace(a, b, n + 1)
y = np.cos(x)
xfunc = np.linspace(a, b, 100)
yfunc = np.cos(xfunc)
ynew = fnc.lagrange(xfunc, x, y, n)

plt.plot(xfunc, yfunc, '-b', x, y, 'ok')
plt.plot(xfunc, ynew, '-r', x, y, 'ok')
plt.grid()
plt.show()
