intList = list(map(int, input().split()))

min = min(intList)
max = max(intList)

minI = intList.index(min)
maxI = intList.index(max)

intList[minI] = max
intList[maxI] = min

print(' '.join(map(str, intList)))
