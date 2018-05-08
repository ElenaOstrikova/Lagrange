class Bisect:

    @staticmethod
    def find(f, a, b, e=10e-6):
        def check(l, r):
            if f(l) * f(r) > 0:
                raise Exception('Sign of function\'s values are equal')

            m = (l + r) / 2

            if abs(f(m)) < e:
                return m
            else:
                if f(l) * f(m) > 0:
                    return check(m, r)
                else:
                    return check(l, m)

        return check(a, b)