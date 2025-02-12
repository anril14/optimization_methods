import matplotlib.pyplot as plt
import numpy as np

rounded_value = 3

def f(x1,x2):
    return 100 * (x2 - x1**2)**2 + (1-x1)**2

x1 = np.linspace(-10,10,100)
x2 = np.linspace(-10,10,100)
plt.plot(x1,x2,f(x1,x2))
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)
plt.show()

print(f(-1,-2))

def hooke_jeeves(i=-1, x1=-1, x2=-2, dx1=1, dx2=1, a=2, eps=0.1):
    i+=1
    fx0 = f(x1,x2)

    if f(x1+dx1,x2) < fx0:
        pass
