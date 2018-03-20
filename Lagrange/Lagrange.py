import numpy as np
import matplotlib.pyplot as plt

class Lagrange:

    def __init__(self, left, right, n, func):
        self.left = left
        self.right = right
        self.n = n

        self.args = np.linspace(left, right, n + 1)
        self.values = func(self.args)

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
                    dividend = dividend * (self.linspace - self.args[j])
                    divider = divider * (self.args[i] - self.args[j])

            self.polinom = self.polinom + self.values[i] * dividend / divider

        self.error = self.function - self.polinom

        # calculate mean squared error
        self.MSE = np.sqrt(((self.function - self.polinom) ** 2).mean())

    def plots(self):
        plt.plot(self.args, self.values, 'ok')
        plt.plot(self.linspace, self.function, '-b', label=u'f(x)')
        plt.plot(self.linspace, self.polinom, '-r', label=u'L(x)')
        plt.legend()
        plt.grid()
        plt.show()

        plt.plot(self.linspace, self.error, '-b')
        plt.title('Absolute error')
        plt.grid()
        plt.show()

        print('MSE: {}'.format(self.MSE))
