import random

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()

arr = []

inFile.close()
md = dict()
for line in lines:
    line = line.strip()
    res = md.get(line, 0)
    md[line] = res + 1

s = []
ok = False
for line in md:
    res = md.get(line)
    perc = res * 100 / (len(lines))
    if perc > 50:
        print(line, file=outFile)
        ok = True
    md[line] = perc
    s.append((perc, line))

if not ok:
    s.sort(reverse=True)
    print(s[0][1], file=outFile)
    print(s[1][1], file=outFile)

outFile.close()
