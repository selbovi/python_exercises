intList = list(map(int, input().split()))

for i in range(len(intList)):
    if i % 2 == 0 and len(intList) > i + 1:
        a = intList[i]
        b = intList[i + 1]
        intList[i] = b
        intList[i + 1] = a

print(' '.join(map(str, intList)))
