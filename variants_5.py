# Variant choose
def default():
    return exit('Incorrect input')


def var_0():
    def f(x1, x2, r) -> float:
        return 4 * x1 ** 2 + 4 * x1 + x2 ** 2 - 8 * x2 + 5 + r * (2 * x1 - x2 - 6) ** 2

    def df1(x1, x2, r) -> float:
        return 8 * x1 + 4 + 2 * r * (2 * x1 - x2 - 6) * 2

    def df2(x1, x2, r) -> float:
        return 2 * x2 - 8 + 2 * r * (2 * x1 - x2 - 6) * -1

    def pen(x1, x2):
        return 2 * x1 - x2 - 6

    return f, df1, df2, pen, 0, 0, 0.01, 10, 0.01


def var_1():
    def f(x1, x2, r) -> float:
        return 4 * x1 ** 2 + 8 * x1 - x2 - 3 + r * (x1 + x2 + 2) ** 2

    def df1(x1, x2, r) -> float:
        return 8 * x1 + 8 + 2 * r * (x1 + x2 + 2)

    def df2(x1, x2, r) -> float:
        return 1 + 2 * r * (x1 + x2 + 2)

    def pen(x1, x2):
        return -x1 - x2 - 2

    return f, df1, df2, pen, -2, 3, 0.01, 10, 0.01

def var_8():
    def f(x1, x2, r) -> float:
        return 4 * x1 ** 2 - x1 * x2 + 5 * x2 ** 2 + 3 + r * (-4 * x1 + x2 + 2) ** 2

    def df1(x1, x2, r) -> float:
        return 8*x1 - x2 + 2 * r * (-4 * x1 + x2 + 2) * -4

    def df2(x1, x2, r) -> float:
        return -x1 + 10*x2 + 2 * r * (-4 * x1 + x2 + 2) * 1

    def pen(x1, x2):
        return -4 * x1 + x2 + 2

    return f, df1, df2, pen, 0, 0, 0.01, 10, 0.01


def get_variant(var):
    variants = {
        '0': var_0,
        '1': var_1,
        '8': var_8
    }
    return variants.get(var, default)()
