inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()

arr = []

inFile.close()

for line in lines:
    for token in line.split():
        arr.append(token)

md = dict()
for a in arr:
    res = md.get(a, 0)
    md[a] = res + 1

res = []
for k in md:
    v = md[k]
    res.append((v, k))

res = sorted(res, key=lambda tup: (-tup[0], tup[1]))

for r in res:
    print(r[1])
