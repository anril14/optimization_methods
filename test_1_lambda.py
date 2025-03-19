import numpy as np

rounding_value = 3
point = 0
eps = 10 ** - rounding_value

x1 = -2
x2 = 3


def df1(x1, x2):
    return 6 * x1 - x2 - 4


def df2(x1, x2):
    return -x1 + 2 * x2


x1_start = df1(x1=x1, x2=x2)
x2_start = df2(x1=x1, x2=x2)

print(x1_start, x2_start)


def f(x1=2, x2=3):
    return 3 * x1 ** 2 - 4 * x1 + x2 ** 2 - x1 * x2


def half_count(i=-1, a=0.1, b=3):
    """Half count method"""

    print(f'x1: {x1}  x2: {x2}  x1_start: {x1_start}  x2_start: {x2_start}')
    while (abs(b) - abs(a)) > eps:
        if i == -1:
            print('Half count method')
        delta = (abs(b) - abs(a)) * 0.0001
        i += 1
        c = (a + b) / 2
        c1 = c - delta
        c2 = c + delta
        f_c1 = f(x1=x1 - c1 * x1_start, x2=x2 - c1 * x2_start)
        f_c2 = f(x1=x1 - c2 * x1_start, x2=x2 - c2 * x2_start)
        print(f"i={i}, c={round(c, rounding_value)}, "
              f"a={round(a, rounding_value)}, "
              f"b={round(b, rounding_value)}, "
              f"c1={round(c1, rounding_value)}, "
              f"c2={round(c2, rounding_value)}, "
              f"f1={round(f_c1, rounding_value)}, "
              f"f2={round(f_c2, rounding_value)}")
        if f_c1 < f_c2:
            b = c2
        else:
            a = c1
    else:
        return (a + b) / 2


print(half_count())
