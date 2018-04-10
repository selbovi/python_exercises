x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return r ** 2 >= ((x - xc) ** 2 + (y - yc) ** 2)


if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
