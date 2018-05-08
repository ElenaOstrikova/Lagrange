class Secant:

    @staticmethod
    def find(func, a, b, e=10e-6):
        def calculate(x1, x2):
            x3 = x1 - (x2 - x1) * func(x1) / (func(x2) - func(x1))

            if abs(x3 - x2) < e:
                return x3
            else:
                return calculate(x2, x3)

        return calculate(a, b)