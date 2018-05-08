import sys


class Newton:

    def __init__(self, func, dfunc, x, max_iterations, eps):
        self.func = func
        self.dfunc = dfunc
        self.x = x
        self.max_iterations = max_iterations
        self.eps = eps

    def calculate(self):
        count = 0
        value = self.func(self.x)

        while count < self.max_iterations and abs(value) > self.eps:
            try:
                self.x = self.x - self.func(self.x)/self.dfunc(self.x)
            except ZeroDivisionError:
                print("Division by zero")
                sys.exit(1)

            value = self.func(self.x)
            count += 1

        return self.x


