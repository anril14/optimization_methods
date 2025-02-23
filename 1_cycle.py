import math
golden = (-1 + 5 ** 0.5) / 2

a = 0.1
b = 3
delta = (abs(b)-abs(a))*0.0001
rounding_value=3
eps = 1 * 10**-rounding_value
i = -1
is_golden = False

def f(x):
    return -math.e ** -x * math.log(x,math.e)

if is_golden:
    while (abs(b) - abs(a)) > eps:
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
else:
    while (abs(b) - abs(a)) > eps:
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

print((a+b)/2, f((a+b)/2))
