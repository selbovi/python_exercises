from math import *

a = float(input())

frac, whole = modf(a)
print(round(frac, 5))
