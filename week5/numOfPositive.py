intList = list(map(int, input().split()))

res = []

for i in intList:
    if i > 0:
        res.append(i)

print(len(res))
