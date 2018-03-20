import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Lagrange:

    def __init__(self, left, right, n, func):
        self.left = left
        self.right = right
        self.n = n

        self.points = np.linspace(left, right, n + 1)
        self.values = func(self.points)

        self.linspace = np.linspace(left, right, 100)
        self.function = func(self.linspace)

        self.polinom = 0
        self.error = []
        self.MSE = 0

    def calculate(self):
        for i in range(self.n + 1):
            dividend = 1
            divider = 1
            for j in range(self.n + 1):
                if i != j:
                    dividend = dividend * (self.linspace - self.points[j])
                    divider = divider * (self.points[i] - self.points[j])

            self.polinom = self.polinom + self.values[i] * dividend / divider

        self.error = self.function - self.polinom
        self.MSE = np.sqrt(((self.function - self.polinom) ** 2).mean())

    def plots(self):
        plt.plot(self.points, self.values, 'ok')
        plt.plot(self.linspace, self.function, '-b', label=u'f(x)')
        plt.plot(self.linspace, self.polinom, '-r', label=u'L(x)')
        plt.legend()
        plt.grid()
        plt.show()

        plt.plot(self.linspace, self.error, '-b')
        plt.title('Absolute error')

        mse = mpatches.Patch(color='red', label='MSE: {}'.format(self.MSE))
        error = mpatches.Patch(label='Absolute error')
        plt.legend(handles=[error, mse])
        plt.grid()
        plt.show()
