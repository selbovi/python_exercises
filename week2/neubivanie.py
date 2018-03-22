a = int(input())
b = int(input())
c = int(input())

max = max(a, b, c)
min = min(a, b, c)


if (a == min):
    print(str(a), end=' ')
elif (b == min):
    print(str(b), end=' ')
elif (c == min):
    print(str(c), end=' ')

if (a >= min):
    print(str(a), end=' ')
elif (b >= min):
    print(str(b), end=' ')
elif (c >= min):
    print(str(c), end=' ')

print(str(max), end=' ')
