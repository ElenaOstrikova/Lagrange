import numpy as np
import matplotlib.pyplot as plt
import Functions as fnc

print("Choose the number of points")
n = int(input())
a = 0
b = 2 * np.pi

# calculate function values
x = np.linspace(a, b, n + 1)
y = np.cos(x)
xfunc = np.linspace(a, b, 100)
yfunc = np.cos(xfunc)
ynew = fnc.lagrange(xfunc, x, y, n)

# draw the graph of a function
plt.plot(x, y, 'ok')
plt.plot(xfunc, yfunc, '-b', label=u'f(x)')
plt.plot(xfunc, ynew, '-r', label=u'L(x)')
plt.legend()
plt.grid()
plt.show()

# calculate abcolute error
error = yfunc - ynew
plt.plot(xfunc, error, '-b')
plt.title('Absolute error')
plt.grid()
plt.show()

# calculate mean squared error
MSE = np.sqrt(((yfunc - ynew) ** 2).mean())
print('MSE:')
print(MSE)
