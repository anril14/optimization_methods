import math
import time
import matplotlib.pyplot as plt
import numpy as np
from variants_4 import get_variant

# Variant choose
var = input('Choose your variant, available:\n0(test), 1, 3, 5, 7\n')
f, df1, df2, x1, x2 = get_variant(var)

# Plot settings
x1_space = np.linspace(-20, 20, 40)
x2_space = np.linspace(-20, 20, 40)
x1_grid, x2_grid = np.meshgrid(x1_space, x2_space)
x3_space = f(x1_grid, x2_grid)

# Dynamic drawing
plt.ion()
fig, ax = plt.subplots(figsize=(10, 7))

# "tight" layout - more usable space but some bugs with text
# fig.set_layout_engine("tight")
ax.contour(x1_space, x2_space, x3_space, 20, zorder=1)
ax.grid(True)
plt.axhline(0, color='black', linewidth=1, zorder=2)
plt.axvline(0, color='black', linewidth=1, zorder=2)


def draw(x1, x2, alpha: float, old_point: dict, color, label: str, order, i: int, first: bool) -> None:
    print(f'DRAW POINT {x1} {x2}')

    # New zoom
    if not first:
        ax.set_xlim(x1 - 1 * alpha * 2, x1 + 1 * alpha * 2)
        ax.set_ylim(x2 - 1 * alpha * 2, x2 + 1 * alpha * 2)

    plt.plot([x1, old_point['x1']], [x2, old_point['x2']],
             color='gray', linewidth='.5')
    plt.scatter(x1, x2, color=color, zorder=order, label=label)
    plt.text(x1, x2, str(i + 1), zorder=order + 1)

    # For canvas changing
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.draw()

    if first:
        time.sleep(1.95)
    time.sleep(0.05)


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
            alpha /= 2
            print(f'NEW ALPHA: {alpha}')

    print(f'\niteration: {i + 2}\n')
    print(f'OLD X1 {old_point['x1']} X2 {old_point['x2']}')
    print(f'NEW X1 {x1} X2 {x2}')

    print('EPS:', math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2))
    if (math.sqrt((x1 - old_point['x1']) ** 2 + (x2 - old_point['x2']) ** 2) > eps
            and alpha > 0.05):

        if i == -1 and is_next_i:
            draw(i=i, x1=old_point['x1'], x2=old_point['x2'], old_point=old_point, alpha=alpha, color='blue',
                 label='Start Point', order=3, first=True)

        is_next_i = True
        check()

        # Checking to draw for delta changes only
        if is_next_i:
            i += 1
            draw(i=i, x1=x1, x2=x2, old_point=old_point, alpha=alpha, color='gray',
                 label='', order=2, first=False)

        return gradient(i, x1, x2, alpha, is_next_i)
    else:
        i += 1
        draw(i=i, x1=x1, x2=x2, old_point=old_point, alpha=alpha, color='red',
             label='End Point', order=3, first=False)


gradient(x1=x1, x2=x2)
plt.ioff()
plt.legend()
plt.show()
