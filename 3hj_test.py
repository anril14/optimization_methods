import matplotlib.pyplot as plt
import numpy as np

def f(x1,x2):
    return (x1-7)**2 + (x2/3-4)**2

x1space = np.linspace(0,12,40)
x2space = np.linspace(0,20,40)
X1, X2 = np.meshgrid(x1space, x2space)
z = f(X1, X2)
plt.contour(x1space,x2space,z,20, zorder=1)
plt.axhline(0, color='black', linewidth=.5, zorder=0)
plt.axvline(0, color='black', linewidth=.5, zorder=0)

def hooke_jeeves(i=-1, x1=1.0, x2=1.0, dx1 = 1.0, dx2 = 1.0, delta = 2.0, acc = 2.2, eps=0.0001):
    point = dict({'x1': x1, 'x2': x2})
    fx0 = f(x1, x2)
    i+=1
    if i == 0:
        plt.scatter(x1, x2, color='black', zorder=2)

    def check_x1():
        nonlocal dx1,dx2, eps, x1, x2
        print('\ninside x1:','i',i, 'x1',x1, 'x2',x2, 'dx1',dx1,'dx2',dx2)
        if f(x1 + dx1,x2) < fx0:
            x1 = x1+dx1
            print('x1 up', x1)
            check_x2()
        elif f(x1 - dx1,x2) < fx0:
            x1 = x1-dx1
            print('x1 down',x1)
            check_x2()
        else:
            check_x2()

    def check_x2():
        nonlocal dx1,dx2, eps, x1, x2, point
        print('inside x2:', 'i', i, 'x1', x1, 'x2', x2, 'dx1',dx1,'dx2',dx2)
        if f(x1 , x2 + dx2) < fx0:
            x2 = x2 + dx2
            print('x2 up', x2)
        elif f(x1 , x2 - dx2) < fx0:
            x2 = x2 - dx2
            print('x2 down', x2)
        else:
            if point['x1'] == x1 and dx1 >= dx2:
                dx1 = dx1 / delta
            dx2 = dx2 / delta

        if dx1 > eps and dx2 > eps:
            if point['x1'] != x1 and point['x2'] != x2:
                print('acceleration step activated')
                acc_step()
            draw('black', 2, True)
            hooke_jeeves(i, x1, x2, dx1, dx2)
        else:
            draw('red', 3, False)

    def acc_step():
        nonlocal x1,x2,point
        print('before step:',x1,x2,point)
        if f(x1,x2) > f(  (x1-point['x1']) * acc + point['x1'],  (x1-point['x2'])* acc +point['x2']  ):
            x1 = (x1-point['x1']) * acc + point['x1']
            x2 = (x2-point['x2']) * acc + point['x2']
            print(f'both x1, x2 {x1, x2}')
        elif f(x1,x2) > f(  (x1-point['x1']) * acc + point['x1'],  x2  ):
            x1 = (x1-point['x1']) * acc + point['x1']
            print(f'x1 {x1}')
        elif f(x1,x2) > f(  x1,  (x1-point['x2']) * acc +point['x2']  ):
            x2 = (x2-point['x2']) * acc + point['x2']
            print(f'x1 {x2}')
        print('after step:', x1,x2,point)

    def draw(color: str, order: int, drawline: bool):
        nonlocal x1,x2,point
        print('draw', x1,x2,point)
        plt.scatter(x1, x2, color=color, zorder=order)
        if drawline:
            plt.plot([ x1 , point['x1'] ], [ x2 , point['x2'] ], color=color, linewidth='.5')

    if dx1 > eps and dx1 > eps:
        check_x1()


hooke_jeeves()
plt.show()
