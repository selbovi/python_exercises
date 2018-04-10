x = int(input())


def IsPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def MinDivisor(n):
    divider = 2
    while n % divider != 0:
        divider += 1
    return divider


if IsPrime(x):
    print(x)
else:
    print(MinDivisor(x))
