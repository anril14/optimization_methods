# Variant choose
def var_0():
    def f(x1, x2) -> float:
        return 3 * x1 ** 2 - 4 * x1 + x2 ** 2 - x1 * x2

    def df1(x1, x2) -> float:
        return 6 * x1 - x2 - 4

    def df2(x1, x2) -> float:
        return -x1 + 2 * x2

    return f, df1, df2, -2, 3


def var_1():
    def f(x1, x2) -> float:
        return 4 * x1 ** 2 + 5 * x2 ** 2 - 3 * x1 * x2 + 9 * x1 - 2 * x2 + 5

    def df1(x1, x2) -> float:
        return 8 * x1 - 3 * x2 + 9

    def df2(x1, x2) -> float:
        return -3 * x1 + 10 * x2 - 2

    return f, df1, df2, 2, 3


def var_3():
    def f(x1, x2) -> float:
        return x1 ** 2 + 3 * x2 ** 2 + 3 * x1 * x2 - x1 - 2 * x2 - 1

    def df1(x1, x2) -> float:
        return 2 * x1 + 3 * x2 - 1

    def df2(x1, x2) -> float:
        return 3 * x1 + 6 * x2 - 2

    return f, df1, df2, 3, 3


def var_5():
    def f(x1, x2) -> float:
        return 6 * x1 ** 2 + x2 ** 2 - x1 * x2 + 4 * x1 - 8 * x2 + 1

    def df1(x1, x2) -> float:
        return 12 * x1 - x2 + 4

    def df2(x1, x2) -> float:
        return -x1 + 2 * x2 - 8

    return f, df1, df2, 2, 2


def var_7():
    def f(x1, x2) -> float:
        return 2 * x1 ** 2 - 5 * x1 * x2 + 11 * x1 + 4 * x2 ** 2 + 8 * x2 - 3

    def df1(x1, x2) -> float:
        return 4 * x1 - 5 * x2 + 11

    def df2(x1, x2) -> float:
        return -5 * x1 + 8 * x2 + 8

    return f, df1, df2, 2, 2


def default():
    return exit('Incorrect input')


def get_variant(var):
    variants = {
        '0': var_0,
        '1': var_1,
        '3': var_3,
        '5': var_5,
        '7': var_7
    }
    return variants.get(var, default)()
