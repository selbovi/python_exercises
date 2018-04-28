n = int(input())

mD = dict()

for r in range(n):
    k, v = input().split()
    mD[k] = v
    mD[v] = k

word = input()
print(mD[word])
