n = int(input())

res = []
for i in range(n):
    m = int(input())
    studentLangSet = set([])
    for lang in range(m):
        l = input()
        studentLangSet.add(l)

    res.append(studentLangSet)

newS = res[0]
for s in res:
    newS = newS.intersection(s)

print(len(newS))

for o in newS:
    print(o)

newSS = set([])
for s in res:
    newSS.update(s)

print(len(newSS))

for o in newSS:
    print(o)
