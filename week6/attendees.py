inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()

res = []
for line in lines:
    str = line.split()
    res.append([str[0], str[1], str[3]])

res.sort(key=lambda r: r[0])

for r in res:
    line = " ".join(r)
    print(line, file=outFile)

inFile.close()
outFile.close()
