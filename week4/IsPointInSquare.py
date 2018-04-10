x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return x <= 1 and y <= 1 and x >= -1 and y >= -1


if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
