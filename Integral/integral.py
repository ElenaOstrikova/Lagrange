import numpy as np


class Integral:

    def __init__(self, fn, a, b, n = 1000):
        self.fn = fn
        self.a = b
        self.b = b
        self.n = n
        self.h = (b - a) / n
        self.points = np.linspace(a, b, n)

    def rectangles(self, type = 'm'):
        I = 0

        for i in range(0, self.n - 1):
            if type == 'l':
                value = self.fn(self.points[i])
            elif type == 'r':
                value = self.fn(self.points[i + 1])
            else:
                value = self.fn((self.points[i] + self.points[i+ 1]) / 2)

            I += value * (self.points[i + 1] - self.points[i])

        return I

    def trapezoid(self):
        I = 0

        for i in range(0, self.n - 1):
            I += (self.fn(self.points[i + 1]) + self.fn(self.points[i])) / 2 * (self.points[i+1] - self.points[i])

        return I

    def Simpson(self):
        I = 0

        for i in range(1, self.n - 1, 2):
            I += self.fn(self.points[i - 1]) + 4 * self.fn(self.points[i]) + self.fn(self.points[i+1])

        I *= (self.b - self.a) / self.n / 3

        return I
