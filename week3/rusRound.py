from math import *

a = float(input())

frac, whole = modf(a)

if (str(a).endswith('5')):
    print(int(whole + 1))
else:
    print(round(a))
