a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = 0
y = 0
if (b > 0):
    x = (f - d * e / b) / (c - d * a / b)
    y = (e - a * x) / b
elif (d > 0):
    x = (e - b * f / d) / (a - b * c / d)
    y = (f - c * x) / d

x = round(x, 6)
y = round(y, 6)

n, divider = x.as_integer_ratio()
if (divider == 1):
    print(int(x), end=' ')
else:
    print('{0:.6}'.format(x), end=' ')

n, divider = y.as_integer_ratio()
if (divider == 1):
    print(int(y), end=' ')
else:
    print('{0:.6}'.format(y), end=' ')
