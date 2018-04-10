x = int(input())
y = int(input())


def ReduceFraction(n, m):
    if n % 2 == 0 and m % 2 == 0:
        return ReduceFraction(n / 2, m / 2)
    elif n % 3 == 0 and m % 3 == 0:
        return ReduceFraction(n / 3, m / 3)
    elif n % 5 == 0 and m % 5 == 0:
        return ReduceFraction(n / 5, m / 5)
    elif n % 11 == 0 and m % 11 == 0:
        return ReduceFraction(n / 11, m / 11)
    else:
        return n, m


p, q = ReduceFraction(x, y)
print(int(p), int(q))
