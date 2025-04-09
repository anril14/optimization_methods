import math
import time
import matplotlib.pyplot as plt
import numpy as np
from variants_4 import get_variant

# Variant choose
var = input('Choose your variant, available:\n0(test), 1, 3, 5, 7\n')
f, df1, df2, x1, x2 = get_variant(var)


def half_count(x1, x2, x1_start, x2_start, *, i=-1, a=0.1, b=3, rounding_value=3) -> float:
    eps = 10 ** - rounding_value
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

        if f_c1 < f_c2:
            b = c2
        else:
            a = c1
    else:
        # print((a + b) / 2)
        return (a + b) / 2


def gradient(i=-1, x1=0.0, x2=0.0, alpha=1.0, is_next_i=True, eps=0.01) -> None:
    old_point = dict({'x1': x1, 'x2': x2})
    x1 = x1 - alpha * df1(old_point['x1'], old_point['x2'])
    x2 = x2 - alpha * df2(old_point['x1'], old_point['x2'])

    def check() -> None:
        nonlocal alpha, x1, x2, is_next_i

        if f(x1, x2) >= f(old_point['x1'], old_point['x2']):
            x1 = old_point['x1']
            x2 = old_point['x2']
            is_next_i = False
        alpha = half_count(x1=x1, x2=x2,
                           x1_start=df1(x1, x2),
                           x2_start=df2(x1, x2))
        print(f'NEW ALPHA: {alpha}')

    print(f'\niteration: {i + 2}\n')
    print(f'OLD X1: {old_point['x1']} X2 {old_point['x2']}')
    print(f'NEW X1: {x1} X2 {x2}')

    print('EPS:', math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2))
    if (math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2) > eps
            and alpha > 0.05):

        is_next_i = True
        check()

        # Checking to draw for delta changes only
        if is_next_i:
            i += 1

        print(f'POINT {x1} {x2}')
        return gradient(i, x1, x2, alpha, is_next_i)

    else:
        i += 1
        print(f'POINT {x1} {x2}')


gradient(x1=x1, x2=x2)
