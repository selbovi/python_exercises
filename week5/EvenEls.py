intList = list(map(int, input().split()))

res = []

for i in intList:
    if i % 2 == 0:
        res.append(i)

print(' '.join(map(str, res)))
