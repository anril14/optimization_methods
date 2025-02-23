import matplotlib.pyplot as plt
import numpy as np

def f(x1,x2):
    return (x1-7)**2 + (x2/3-4)**2

x1 = np.linspace(0,12,40)
x2 = np.linspace(0,20,40)
X1, X2 = np.meshgrid(x1, x2)
z = f(X1, X2)
plt.contour(x1,x2,z,20, zorder=1)
plt.axhline(0, color='black', linewidth=.5, zorder=0)
plt.axvline(0, color='black', linewidth=.5, zorder=0)

def hooke_jeeves(i=-1, x1=1.0, x2=1.0, dx1=1.0, dx2=1.0, a=2, eps=0.1):
    i+=1
    print()
    fx0 = f(x1,x2)
    if i==0:
        plt.scatter(x1, x2, color='black', zorder=2)

    def checkx1():
        nonlocal dx1, eps, x1, x2
        print('insidex1','i',i, 'x1',x1, 'x2',x2, 'dx1',dx1,'\n')
        if f(x1 + dx1,x2) < fx0:
            x1 = x1+dx1
            plt.scatter(x1, x2, color='black', zorder=2)
            print('x1up', x1)
            checkx2()
        elif f(x1 - dx1,x2) < fx0:
            x1 = x1-dx1
            plt.scatter(x1, x2, color='black', zorder=2)
            print('x1down',x1)
            checkx2()
        else:
            if dx1/2 < eps:
                checkx2()
                return
            dx1 = dx1/2
            checkx1()
    def checkx2():
        nonlocal dx2, dx1, eps, x1, x2
        print('insidex2', 'i', i, 'x1', x1, 'x2', x2, 'dx1', dx1,'dx2', dx2,'\n')
        if f(x1 , x2 + dx2) < fx0:
            x2 = x2 + dx2
            plt.scatter(x1, x2, color='black', zorder=2)
            print('x2up', x2)
        elif f(x1 , x2 - dx2) < fx0:
            x2 = x2 - dx2
            plt.scatter(x1, x2, color='black', zorder=2)
            print('x2down', x2)
        else:
            if dx2 / 2 < eps:
                return
            dx2 = dx2 / 2
        if dx1 > eps or dx2 > eps:
            hooke_jeeves(i, x1, x2, dx1, dx2)
    if dx1 > eps or dx2 > eps:
        checkx1()

hooke_jeeves()
plt.show()