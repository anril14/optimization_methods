import math
# import time
# import matplotlib.pyplot as plt
# import numpy as np
from variants_5 import get_variant

# Variant choose
var = input('Choose your variant, available:\n0(test), 1\n')
f, df1, df2, pen, x1, x2, r, c, gl_eps = get_variant(var)

# Final values
x1f, x2f, new_r = x1, x2, r


def half_count(x1, x2, r, x1_start, x2_start, *, i=-1, a=0.1, b=3, rounding_value=3) -> float:
    eps = 10 ** - rounding_value
    while (abs(b) - abs(a)) > eps:
        # if i == -1:
        #     print('Half count method')
        delta = (abs(b) - abs(a)) * 0.0001
        i += 1
        c = (a + b) / 2
        c1 = c - delta
        c2 = c + delta
        f_c1 = f(x1=x1 - c1 * x1_start, x2=x2 - c1 * x2_start, r=r)
        f_c2 = f(x1=x1 - c2 * x1_start, x2=x2 - c2 * x2_start, r=r)

        if f_c1 < f_c2:
            b = c2
        else:
            a = c1
    else:
        # print((a + b) / 2)
        return (a + b) / 2


def gradient(i=-1, x1=0.0, x2=0.0, r=new_r, alpha=1.0, is_next_i=True, eps=0.01):
    print(f'x check X1: {x1} X2 {x2}')
    alpha = half_count(x1=x1, x2=x2, r=r,
                       x1_start=df1(x1, x2, r),
                       x2_start=df2(x1, x2, r))
    print(f'NEW ALPHA: {alpha}')
    print(f'r: {r}')
    old_point = dict({'x1': x1, 'x2': x2})
    x1 = x1 - alpha * df1(x1, x2, r)
    x2 = x2 - alpha * df2(x1, x2, r)

    def check() -> None:
        nonlocal is_next_i
        if f(x1, x2, r) >= f(old_point['x1'], old_point['x2'], r):
            is_next_i = False

    print(f'\niteration: {i + 2}\n')
    print(f'OLD X1: {old_point['x1']} X2 {old_point['x2']}')
    print(f'NEW X1: {x1} X2 {x2}')
    print(f'NEW F: {f(x1, x2, r)}')

    print('EPS:', math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2))

    if (math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2)) > eps:

        is_next_i = True
        check()

        # Checking to draw for delta changes only
        if is_next_i:
            i += 1

        # print(f'POINT {x1} {x2}')
        return gradient(i, x1, x2, r, alpha, is_next_i)

    else:
        i += 1
        global x1f, x2f, new_r
        x1f, x2f = x1, x2
        new_r *= c


while abs(pen(x1f, x2f)) > gl_eps:
    print(f'pen: {pen(x1f, x2f)}')
    print(f'\nSTART POINT: {x1f}, {x2f}, r:{new_r}')
    gradient(x1=x1f, x2=x2f, r=new_r)
    print(f'FINAL POINT: {x1f}, {x2f}')

print('dec0_0m')
