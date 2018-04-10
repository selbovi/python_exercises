a = float(input())
n = int(input())


def fast(a, n):
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    else:
        return a * fast(a, n - 1)


if (fast(a, n).is_integer()):
    print(int(fast(a, n)))
else:
    print(str(fast(a, n)))
