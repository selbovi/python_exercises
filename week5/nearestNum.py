n = int(input())
intList = list(map(int, input().split()))
x = int(input())

diffs = []

for i in intList:
    diffs.append(abs(x - i))

m = min(diffs)

print(intList[diffs.index(m)])
