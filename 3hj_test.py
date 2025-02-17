import time, datetime
import matplotlib.pyplot as plt
import numpy as np
from functools import wraps

def recTime(func):
    global total_time
    total_time = 0

    def wrapper(*args, **kwargs):
        """Counts time in seconds of other func working"""

        global total_time
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        total_time += done.total_seconds()
    return wrapper

class Solution():
    """Function class"""

    def __init__(self, delta = 2.0, acc = 2.2, eps = 0.001):
        self.delta = delta
        self.acc = acc
        self.eps = eps

    def f(self, x1,x2):
        return (x1-7)**2 + (x2/3-4)**2

    def showplot(self):
        x1space = np.linspace(-20, 20, 40)
        x2space = np.linspace(-20, 20, 40)
        X1, X2 = np.meshgrid(x1space, x2space)
        z = self.f(X1, X2)
        plt.contour(x1space, x2space, z, 20, zorder=1)
        plt.axhline(0, color='black', linewidth=.5, zorder=0)
        plt.axvline(0, color='black', linewidth=.5, zorder=0)
        plt.show()

    @recTime
    def hooke_jeeves(self,i=-1, x1=2.0, x2=3.0, dx1 = 1.0, dx2 = 1.0, delta = 2.0, acc = 2.2, eps=0.001):
        point = dict({'x1': x1, 'x2': x2})
        fx0 = self.f(x1, x2)
        i+=1
        if i == 0:
            plt.scatter(x1, x2, color='blue', zorder=3)

        def check_x1():
            nonlocal dx1,dx2, x1, x2
            print(f'\niteration: {i}\nNOW CHECKING X1: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
            if self.f(x1 + dx1,x2) < fx0:
                x1 = x1+dx1
                print('X1 UP:', x1)
                check_x2()
            elif self.f(x1 - dx1,x2) < fx0:
                x1 = x1-dx1
                print('X1 DOWN:',x1)
                check_x2()
            else:
                check_x2()

        def check_x2():
            nonlocal dx1,dx2, eps, x1, x2, point
            print(f'NOW CHECKING X2: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
            if self.f(x1 , x2 + dx2) < fx0:
                x2 = x2 + dx2
                print('X2 UP', x2)
            elif self.f(x1 , x2 - dx2) < fx0:
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
                self.hooke_jeeves(i, x1, x2, dx1, dx2)
            else:
                draw('red', 3)

        def acc_step():
            nonlocal x1,x2,point
            print(f'VALUES BEFORE STEP: X1 {x1} X2 {x2}')
            if self.f(x1,x2) > self.f(  (x1-point['x1']) * acc + point['x1'],  (x1-point['x2'])* acc +point['x2']  ):
                x1 = (x1-point['x1']) * acc + point['x1']
                x2 = (x2-point['x2']) * acc + point['x2']
                print('BOTH WAS CHANGED')
            elif self.f(x1,x2) > self.f(  (x1-point['x1']) * acc + point['x1'],  x2  ):
                x1 = (x1-point['x1']) * acc + point['x1']
                print('X1 WAS CHANGED')
            elif self.f(x1,x2) > self.f(  x1,  (x1-point['x2']) * acc +point['x2']  ):
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

function = Solution()
function.hooke_jeeves()
function.showplot()
print(total_time)
