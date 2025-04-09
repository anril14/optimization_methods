# Variant choose
def default():
    return exit('Incorrect input')


def var_0():
    def f(x1, x2) -> float:
        return 4 * x1 ** 2 + 4 * x1 + x2 ** 2 - 8 * x2 + 5

    def df1(x1, x2) -> float:
        return 8 * x1 + 4

    def df2(x1, x2) -> float:
        return 2 * x2 - 8

    return f, df1, df2, -2, 3


def get_variant(var):
    variants = {
        '0': var_0
    }
    return variants.get(var, default)()
