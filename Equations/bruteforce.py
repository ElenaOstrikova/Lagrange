import numpy as np
import matplotlib.pyplot as plt


class Bruteforce:

    def __init__(self, left, right, n, func):
        self.left = right
        self.right = right
        self.n = n

        self.points = np.linspace(left, right, n + 1)
        self.values = func(self.points)

        self.linspace = np.linspace(left, right, 100)
        self.function = func(self.linspace)

        self.ans = 0
        self.ex = 0

    def FirstStep(self):
        print("---Bruteforce---")
        print("Roots:")
        for i in range(self.n):
            if (self.values[i]*self.values[i+1] < 0):
                self.ans = self.points[i] - ((self.points[i + 1] - self.points[i]) * self.values[i]) / (self.values[i + 1] - self.values[i])
                print(self.ans)
        print("Max:")
        for i in range(self.n):
            if ((i>0) and (self.values[i-1] < self.values[i]) and (self.values[i] > self.values[i+1])):
                self.ex = self.points[i]
                print(self.ex)
        print("Min:")
        for i in range(self.n):
            if ((i>0) and (self.values[i-1] > self.values[i]) and (self.values[i] < self.values[i+1])):
                self.ex = self.points[i]
                print(self.ex)
    def plots(self):
        plt.plot(self.linspace, self.function, '-r', label=u'f(x)')
        plt.legend()
        plt.grid()
        plt.show()
