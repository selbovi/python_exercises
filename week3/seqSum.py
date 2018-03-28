a = int(input())

i = 2
res = 1
if a == 1:
    print(1)
else:
    res += 1 / (2 ** 2)
    i += 1
    while i <= a:
        res += 1 / (i ** 2)
        i += 1
    print('{0:.6}'.format(res))
