import time
import matplotlib.pyplot as plt
import numpy as np

def f(x1,x2):
    return 4*x1**2 + 5*x2**2 - 3*x1*x2 + 9*x1 - 2*x2 + 5

x1_space = np.linspace(-5,5,40)
x2_space = np.linspace(-5,5,40)
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

def hooke_jeeves(i=-1, x1=2.0, x2=3.0, dx1 = 1.0, dx2 = 1.0,
                 is_next_i = True, delta = 2.0, acc_ratio = 2.2, eps=0.001):
    old_point = dict({'x1': x1, 'x2': x2})
    fx0 = f(x1, x2)

    def check_x1():
        nonlocal x1, x2
        print(f'\niteration: {i}\nNOW CHECKING X1: X1 {x1} X2 {x2}'
              f' dX1 {dx1} dX2 {dx2}')
        if f(x1 + dx1, x2) < fx0:
            x1 = x1 + dx1
            print('X1 UP TO:', x1)
            check_x2()
        elif f(x1 - dx1, x2) < fx0:
            x1 = x1 - dx1
            print('X1 DOWN TO:', x1)
            check_x2()
        else:
            check_x2()

    def check_x2():
        nonlocal dx1, dx2, x1, x2, is_next_i
        print(f'NOW CHECKING X2: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
        if f(x1, x2 + dx2) < fx0:
            x2 = x2 + dx2
            print('X2 UP TO:', x2)
        elif f(x1, x2 - dx2) < fx0:
            x2 = x2 - dx2
            print('X2 DOWN TO:', x2)
        else:
            if old_point['x1'] == x1 and dx1 >= dx2:
                print('DELTA X1 DOWN')
                dx1 /= delta
                is_next_i = False
            dx2 /= delta
            print('DELTA X2 DOWN')

        if old_point['x1'] != x1 and old_point['x2'] != x2:
            print('*ACCELERATION STEP ACTIVATED')
            acc_step()

    def acc_step():
        # var acc_ratio is acceleration step ratio when multiplying
        nonlocal x1, x2
        print(f'VALUES BEFORE STEP: X1 {x1} X2 {x2}')
        if f(x1, x2) > f((x1 - old_point['x1']) * acc_ratio + old_point['x1'],
                         (x1 - old_point['x2']) * acc_ratio + old_point['x2']):
            x1 = (x1 - old_point['x1']) * acc_ratio + old_point['x1']
            x2 = (x2 - old_point['x2']) * acc_ratio + old_point['x2']
            print('BOTH WAS CHANGED')
        elif f(x1, x2) > f((x1 - old_point['x1']) * acc_ratio + old_point['x1'], x2):
            x1 = (x1 - old_point['x1']) * acc_ratio + old_point['x1']
            print('X1 WAS CHANGED')
        elif f(x1, x2) > f(x1, (x1 - old_point['x2']) * acc_ratio + old_point['x2']):
            x2 = (x2 - old_point['x2']) * acc_ratio + old_point['x2']
            print('X2 WAS CHANGED')
        print(f'*VALUES AFTER STEP: X1 {x1} X2 {x2}')

    def draw(color, label: str, order: int, is_text: bool):
        print(f'DRAW POINT {x1} {x2}')

        # New zoom
        ax.set_xlim(old_point['x1']-1*dx1*2,old_point['x1']+1*dx1*2)
        ax.set_ylim(old_point['x2']-1*dx2*2,old_point['x2']+1*dx2*2)

        # For canvas changing
        fig.canvas.draw()
        fig.canvas.flush_events()

        plt.scatter(x1, x2, color=color, zorder=order, label=label)
        if is_text:
            plt.text(x1, x2, str(i+1), zorder = order+1)
        plt.plot([x1, old_point['x1']], [x2, old_point['x2']],
                 color=color, linewidth='.5')

        plt.draw()
        time.sleep(0.1)

    #Delta condition
    if dx1 > eps and dx1 > eps:
        # Checking for delta changes only
        if is_next_i:
            if i == -1:
                plt.scatter(x1, x2, color='blue', zorder=3, label='Start point')
                fig.canvas.draw()
                fig.canvas.flush_events()

                time.sleep(2.0)
                plt.draw()
            i += 1

        is_next_i = True
        check_x1()

        if is_next_i:
            draw('gray','', 2, True)
        hooke_jeeves(i, x1, x2, dx1, dx2, is_next_i)
    else:
        draw('red', 'End Point', 3, False)

hooke_jeeves()
plt.ioff()
plt.legend()
plt.show()