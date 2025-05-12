import math
import time
import matplotlib.pyplot as plt
import numpy as np
from variants_4 import get_variant

# Variant choose
var = input('Choose your variant, available:\n0(test), 1, 3, 5, 7\n')
f, df1, df2, x1, x2 = get_variant(var)

def gradient(i=-1, x1=0.0, x2=0.0, lamb=1.0, is_next_i=True, eps=0.01) -> None:
    old_point = dict({'x1': x1, 'x2': x2})
    x1 = x1 - lamb * df1(old_point['x1'], old_point['x2'])
    x2 = x2 - lamb * df2(old_point['x1'], old_point['x2'])

    def check() -> None:
        nonlocal lamb, x1, x2, is_next_i

        if f(x1, x2) >= f(old_point['x1'], old_point['x2']):
            x1 = old_point['x1']
            x2 = old_point['x2']
            is_next_i = False
            lamb /= 2
            print(f'NEW ALPHA: {lamb}')

    print(f'\niteration: {i + 2}\n')
    print(f'OLD X1 {old_point['x1']} X2 {old_point['x2']}')
    print(f'NEW X1 {x1} X2 {x2}')

    print('EPS:', math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2))
    if (math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2) > eps
            and lamb > 0.05):

        is_next_i = True
        check()

        # Checking to draw for delta changes only
        if is_next_i:
            i += 1

        return gradient(i, x1, x2, lamb, is_next_i)
    else:
        print(f'Финальные значения: X1 {x1} X2 {x2}')

gradient(x1=x1, x2=x2)
