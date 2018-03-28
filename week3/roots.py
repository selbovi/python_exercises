import math
import cmath

a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

x1 = (-b + d ** 0.5) / (2 * a)

if (d > 0):
    x2 = (-b - d ** 0.5) / (2 * a)
    if x2 >= x1:
        t = x2
        x2 = x1
        x1 = t
    n, divider = x2.as_integer_ratio()
    if (divider == 1):
        print(int(x2), end=' ')
    else:
        print('{0:.6}'.format(x2), end=' ')

if (d >= 0):
    n, divider = x1.as_integer_ratio()
    if (divider == 1):
        print(int(x1), end=' ')
    else:
        print('{0:.6}'.format(x1), end=' ')
