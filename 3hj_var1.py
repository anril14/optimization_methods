import matplotlib.pyplot as plt
import numpy as np

def f(x1,x2):
    return 4 * x1 **2 + 5 * x2 ** 2 - 3 * x1 * x2 + 9 * x1 - 2 * x2 + 5

x1space = np.linspace(-20,20,40)
x2space = np.linspace(-20,20,40)
X1, X2 = np.meshgrid(x1space, x2space)
z = f(X1, X2)
plt.contour(x1space,x2space,z,20, zorder=1)
plt.axhline(0, color='black', linewidth=.5, zorder=0)
plt.axvline(0, color='black', linewidth=.5, zorder=0)

def hooke_jeeves(i=-1, x1=2.0, x2=3.0, dx1 = 1.0, dx2 = 1.0, delta = 2.0, acc = 2.2, eps=0.0001):
    point = dict({'x1': x1, 'x2': x2})
    fx0 = f(x1, x2)
    i+=1
    if i == 0:
        plt.scatter(x1, x2, color='black', zorder=2)

    def check_x1():
        nonlocal dx1,dx2, eps, x1, x2
        print(f'\niteration: {i}\nNOW CHECKING X1: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
        if f(x1 + dx1,x2) < fx0:
            x1 = x1+dx1
            print('X1 UP:', x1)
            check_x2()
        elif f(x1 - dx1,x2) < fx0:
            x1 = x1-dx1
            print('X1 DOWN:',x1)
            check_x2()
        else:
            check_x2()

    def check_x2():
        nonlocal dx1,dx2, eps, x1, x2, point
        print(f'NOW CHECKING X2: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
        if f(x1 , x2 + dx2) < fx0:
            x2 = x2 + dx2
            print('X2 UP', x2)
        elif f(x1 , x2 - dx2) < fx0:
            x2 = x2 - dx2
            print('X2 DOWN', x2)
        else:
            if point['x1'] == x1 and dx1 >= dx2:
                dx1 = dx1 / delta
            dx2 = dx2 / delta

        if dx1 > eps and dx2 > eps:
            if point['x1'] != x1 and point['x2'] != x2:
                print('*ACCELERATION STEP ACTIVATED')
                acc_step()
            draw('black', 2)
            hooke_jeeves(i, x1, x2, dx1, dx2)
        else:
            draw('red', 3)

    def acc_step():
        nonlocal x1,x2,point
        print(f'VALUES BEFORE STEP: X1 {x1} X2 {x2}')
        if f(x1,x2) > f(  (x1-point['x1']) * acc + point['x1'],  (x1-point['x2'])* acc +point['x2']  ):
            x1 = (x1-point['x1']) * acc + point['x1']
            x2 = (x2-point['x2']) * acc + point['x2']
            print('BOTH WAS CHANGED')
        elif f(x1,x2) > f(  (x1-point['x1']) * acc + point['x1'],  x2  ):
            x1 = (x1-point['x1']) * acc + point['x1']
            print('X1 WAS CHANGED')
        elif f(x1,x2) > f(  x1,  (x1-point['x2']) * acc +point['x2']  ):
            x2 = (x2-point['x2']) * acc + point['x2']
            print('X2 WAS CHANGED')
        print(f'*VALUES AFTER STEP: X1 {x1} X2 {x2}')

    def draw(color: str, order: int):
        nonlocal x1,x2,point
        print(f'DRAW POINT {x1} {x2}')
        plt.scatter(x1, x2, color=color, zorder=order)
        plt.plot([ x1 , point['x1'] ], [ x2 , point['x2'] ], color=color, linewidth='.5')

    if dx1 > eps and dx1 > eps:
        check_x1()

hooke_jeeves()
plt.show()