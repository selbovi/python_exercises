intList = list(map(int, input().split()))

res = []

for i in range(len(intList)):
    if i > 0:
        if intList[i] > intList[i - 1]:
            res.append(intList[i])

print(' '.join(map(str, res)))
