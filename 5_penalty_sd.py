import math
# import time
# import matplotlib.pyplot as plt
# import numpy as np
from variants_5 import get_variant

# Variant choose
var = input('Choose your variant, available:\n0(test), 1, 8\n')
f, df1, df2, pen, x1, x2, r, c, gl_eps = get_variant(var)

# Final values
x1f, x2f, new_r = x1, x2, r

def gradient(i=-1, x1=0.0, x2=0.0, r=new_r, lamb=1.0, is_next_i=True, eps=0.01):
    old_point = dict({'x1': x1, 'x2': x2})
    x1 = x1 - lamb * df1(old_point['x1'], old_point['x2'], r)
    x2 = x2 - lamb * df2(old_point['x1'], old_point['x2'], r)
    print(f'r: {r}')
    def check() -> None:
        nonlocal lamb, x1, x2, is_next_i

        if f(x1, x2, r) >= f(old_point['x1'], old_point['x2'], r):
            x1 = old_point['x1']
            x2 = old_point['x2']
            is_next_i = False
            lamb /= 2
            print(f'NEW ALPHA: {lamb}')

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
        return gradient(i, x1, x2, r, lamb, is_next_i)

    else:
        i += 1
        global x1f, x2f, new_r
        x1f, x2f = x1, x2
        new_r = new_r * c


while abs(pen(x1f, x2f)) > gl_eps:
    print(f'pen: {pen(x1f, x2f)}')
    print(f'\nSTART POINT: {x1f}, {x2f}, r:{new_r}')
    gradient(x1=x1f, x2=x2f, r=new_r)
    print(f'FINAL POINT: {x1f}, {x2f}')