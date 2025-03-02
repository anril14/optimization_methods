import math
import time
import matplotlib.pyplot as plt
import numpy as np

# Variant choose
var = input('Choose your variant, available:\n0(test), 1, 3\n')
match var:
    case '0':
        def f(x1, x2):
            return 3*x1**2 - 4*x1 + x2**2 - x1*x2
        def df1(x1, x2):
            return 6 * x1 - x2 - 4
        def df2(x1, x2):
            return -x1 + 2 * x2
        x1, x2 = 2, 3
    case '1':
        def f(x1, x2):
            return 4*x1**2 + 5*x2**2 - 3*x1*x2 + 9*x1 - 2*x2 + 5
        def df1(x1, x2):
            return 8 * x1 - 3 * x2 + 9
        def df2(x1, x2):
            return -3 * x1 + 10 * x2 - 2
        x1, x2 = 2, 3
    case '3':
        def f(x1, x2):
            return x1**2 + 3*x2**2 + 3*x1*x2 - x1 - 2*x2 - 1
        def df1(x1, x2):
            return 2*x1 + 3*x2 - 1
        def df2(x1, x2):
            return 3*x1 + 6*x2 - 2
        x1, x2 = 3, 3
    case _:
        print('Incorrect input')
        exit()

# Plot settings
x1_space = np.linspace(-20,20,40)
x2_space = np.linspace(-20,20,40)
x1_grid, x2_grid = np.meshgrid(x1_space, x2_space)
x3_space = f(x1_grid, x2_grid)

plt.ion()
fig, ax = plt.subplots(figsize = (10,7))

# "tight" layout - more usable space but some bugs with text
# fig.set_layout_engine("tight")
ax.contour(x1_space,x2_space,x3_space,20,zorder = 1)
ax.grid(True)
plt.axhline(0, color='black', linewidth=1, zorder=2)
plt.axvline(0, color='black', linewidth=1, zorder=2)

def gradient(i = -1, x1 = 0, x2 = 0, alpha = 0.5, is_next_i = True, eps = 1):
    old_point = dict({'x1': x1, 'x2': x2})
    x1 = x1 - alpha * df1(old_point['x1'], old_point['x2'])
    x2 = x2 - alpha * df2(old_point['x1'], old_point['x2'])

    def check():
        nonlocal alpha, x1, x2, is_next_i

        if f(x1, x2) >= f(old_point['x1'], old_point['x2']):
            alpha /= 2
            print(f'NEW ALPHA: {alpha}')
            is_next_i = False

    def draw(x1,x2: float, color, label: str, order: int, is_text: bool):
        print(f'DRAW POINT {x1} {x2}')

        # New zoom
        ax.set_xlim(old_point['x1']-1*alpha*2,old_point['x1']+1*alpha*2)
        ax.set_ylim(old_point['x2']-1*alpha*2,old_point['x2']+1*alpha*2)

        plt.plot([x1, old_point['x1']], [x2, old_point['x2']],
                 color=color, linewidth='.5')
        plt.scatter(x1, x2, color=color, zorder=order, label=label)
        if is_text:
            plt.text(x1, x2, str(i+1), zorder = order+1)

        # For canvas changing
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.draw()
        time.sleep(0.05)

    print(f'\niteration: {i+1}\n')
    print(f'OLD X1 {old_point['x1']} X2 {old_point['x2']}')
    print(f'NEW X1 {x1} X2 {x2}')

    if (math.sqrt(x1**2+old_point['x1']**2) > eps or math.sqrt(x2**2+old_point['x2']**2) > eps) and alpha > 0.1:
        if i == -1:
            print(f'DRAW POINT {old_point['x1']} {old_point['x2']}')
            print(f'DRAW POINT {x1} {x2}')
            plt.scatter(old_point['x1'], old_point['x2'], color='blue',
                        zorder=3, label='Start point')
            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(2.0)
            plt.draw()

        # Checking for delta changes only
        if is_next_i:
            i += 1

        is_next_i = True
        check()

        if is_next_i:
            draw(x1, x2, 'gray', '', 2, True)
        else:
            draw(x1, x2, 'gray', '', 2, False)

        gradient(i, x1, x2, alpha, is_next_i)
    else:
        draw(old_point['x1'],old_point['x2'],'red', 'End Point', 3, False)

gradient(x1=x1, x2=x2)
plt.ioff()
plt.legend()
plt.show()
