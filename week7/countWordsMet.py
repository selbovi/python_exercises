inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()

tokens = []
for line in lines:
    for token in line.split():
        tokens.append(token)

mapD = dict()
digs = []
for token in tokens:
    res = mapD.get(token, 0)
    digs.append(str(res))
    mapD[token] = res + 1

for r in digs:
    print(r)

inFile.close()
outFile.close()
