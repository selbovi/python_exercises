a = int(input())
n = int(input())


def sum(a, n):
    if n != 0:
        a += 1
        return sum(a, n - 1)
    return a


print(sum(a, n))
