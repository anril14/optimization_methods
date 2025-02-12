import matplotlib.pyplot as plt
import numpy as np

rounding_value=3
point = 0

def f(x):
    return -np.exp(-x) * np.log(x)

def golden_count(i = -1, a=0.1,b=3, eps = 10**-rounding_value, golden = (-1 + 5 ** 0.5) / 2 ):
    if i==-1:
        print('Golden count method')
    global point
    i += 1
    c1 = a + golden * (a + golden * (b - a) - a)
    c2 = a + golden * (b - a)
    print("i=", i, "c=", round((a + golden * (b - a)), rounding_value), "a=", round(a, rounding_value),
          "b=", round(b, rounding_value), "c1=", round(c1, rounding_value), "c2=",
          round(c2, rounding_value), "f1=", round(f(c1), rounding_value),
          "f2=", round(f(c2), rounding_value))
    if f(c1) < f(c2):
        b = c2
    else:
        a = c1
    if (abs(b) - abs(a)) > eps:
        golden_count(i,a,b)
    else:
        print((a + b) / 2, f((a + b) / 2),'\n')
        point = (a + b) / 2

def half_count(i = -1, a=0.1,b=3, eps = 1 * 10**-rounding_value ):
    if i==-1:
        print('Half count method')
    global point
    delta = (abs(b) - abs(a)) * 0.0001
    i += 1
    c = (a + b) / 2
    c1 = c - delta
    c2 = c + delta
    print("i=", i, "c=", round(c, rounding_value), "a=", round(a, rounding_value),
          "b=", round(b, rounding_value), "c1=", round(c - delta, rounding_value), "c2=",
          round(c + delta, rounding_value), "f1=", round(f(c - delta), rounding_value),
          "f2=", round(f(c + delta), rounding_value))
    if f(c1) < f(c2):
        b = c2
    else:
        a = c1
    if (abs(b) - abs(a)) > eps:
        half_count(i,a,b)
    else:
        print((a + b) / 2, f((a + b) / 2),'\n')
        point=(a+b)/2

half_count()
golden_count()

plt.axhline(0, color='black', linewidth=.5, zorder=0)
plt.axvline(0, color='black', linewidth=.5, zorder=0)
values = np.linspace(0.1,3,10000)
plt.plot(values,f(values), color = 'orange', zorder=1)
plt.scatter(point,f(point), color = 'darkblue', zorder=2)
plt.show()
