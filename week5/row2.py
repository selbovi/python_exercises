a = int(input())
b = int(input())

r = 1

if a < b:
    r = range(a, b + 1)
else:
    r = range(a, b - 1, -1)

for i in r:
    print(i, end=' ')
