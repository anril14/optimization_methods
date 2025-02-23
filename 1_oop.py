import matplotlib.pyplot as plt
import numpy as np

class Function():
    """Function Class"""

    def __init__(self, rounding_value = 3, point = None):
        self.rounding_value = rounding_value
        self.point = point
        self.eps = 10 ** - rounding_value

    def f(self,x):
        return -np.exp(-x) * np.log(x)

    def golden_count(self, i = -1, a=0.1, b=3 , golden =(-1 + 5 ** 0.5) / 2):
        """Golden count method"""

        if i==-1:
            print('Golden count method')
        i += 1
        c1 = a + golden * (a + golden * (b - a) - a)
        c2 = a + golden * (b - a)
        f_c1 = self.f(c1)
        f_c2 = self.f(c2)
        print(f"i={i}, a={round(a, self.rounding_value)}, "
              f"b={round(b, self.rounding_value)}, "
              f"c1={round(c1, self.rounding_value)}, "
              f"c2={round(c2, self.rounding_value)}, "
              f"f1={round(f_c1, self.rounding_value)}, "
              f"f2={round(f_c2, self.rounding_value)}")
        if f_c1 < f_c2:
            b = c2
        else:
            a = c1
        if (abs(b) - abs(a)) > self.eps:
            self.golden_count(i,a,b)
        else:
            print((a + b) / 2, self.f((a + b) / 2),'\n')
            self.point = (a + b) / 2

    def half_count(self, i = -1, a=0.1,b=3):
        """Half count method"""

        if i==-1:
            print('Half count method')
        delta = (abs(b) - abs(a)) * 0.0001
        i += 1
        c = (a + b) / 2
        c1 = c - delta
        c2 = c + delta
        f_c1 = self.f(c1)
        f_c2 = self.f(c2)
        print(f"i={i}, c={round(c, self.rounding_value)}, "
              f"a={round(a, self.rounding_value)}, "
              f"b={round(b, self.rounding_value)}, "
              f"c1={round(c1, self.rounding_value)}, "
              f"c2={round(c2, self.rounding_value)}, "
              f"f1={round(f_c1, self.rounding_value)}, "
              f"f2={round(f_c2, self.rounding_value)}")
        if f_c1 < f_c2:
            b = c2
        else:
            a = c1
        if (abs(b) - abs(a)) > self.eps:
            self.half_count(i,a,b)
        else:
            print((a + b) / 2, self.f((a + b) / 2),'\n')
            self.point = (a + b) / 2

    def draw(self):
        """Draws plot with function and minimal value point"""

        plt.axhline(0, color='black', linewidth=.5, zorder=0)
        plt.axvline(0, color='black', linewidth=.5, zorder=0)
        values = np.linspace(0.1,3,10000)
        plt.plot(values,self.f(values), color = 'orange', zorder=1)
        plt.scatter(self.point, self.f(self.point), color ='darkblue', zorder=2)
        plt.show()

function = Function(3,0)
function.half_count()
function.golden_count()
function.draw()
