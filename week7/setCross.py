inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()

one = set(map(int, lines[0].split()))
two = set(map(int, lines[1].split()))

res = one.intersection(two)
forPrinting = []
for elem in res:
    forPrinting.append(elem)

forPrinting.sort()
print(*forPrinting, file=outFile)

inFile.close()
outFile.close()
