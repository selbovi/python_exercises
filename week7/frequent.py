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

max = 0
word = ''
for k in md:
    v = md[k]
    if v >= max:
        max = v
        word = k

res = []
for k in md:
    v = md[k]
    if v == max:
        res.append((k, v))

res.sort(key=lambda k: k[0])
print(res[0][0])
