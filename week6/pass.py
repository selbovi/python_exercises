k = int(input())

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()

students = []
for line in lines:
    splitted = line.split()
    if (len(splitted) > 3):
        x = int(splitted[len(splitted) - 3])
        y = int(splitted[len(splitted) - 2])
        z = int(splitted[len(splitted) - 1])

        if (x > 39 and y > 39 and z > 39):
            students.append([x + y + z, line])

students.sort(key=lambda t: t[0], reverse=True)


def anyeq(st):
    sublist = students[k - 1:]
    if (sublist[0][0] == sublist[1][0]):
        eq = [0] * 300
        for i in st:
            eq[i[0]] += 1

        if (k < max(eq)):
            return max(eq)

    return 0


def getMinP():
    willPassList = students[0:k]
    min = willPassList[len(willPassList) - 1][0]
    wilPassPlusOne = students[0:k + 1]
    if (min != wilPassPlusOne[len(wilPassPlusOne) - 1][0]):
        return min
    else:
        while (min >= students[len(students) - 1][0]):
            students.pop(len(students) - 1)

        if len(students) == 0:
            return min
        else:
            return students[len(students) - 1][0]


def eqMax():
    slice = students[0:k + 1]
    lastEl = slice[len(slice) - 1][0]
    eq = True
    for s in slice:
        if lastEl != s[0]:
            eq = False
    return eq


if (k < len(students)):
    if (eqMax()):  # равный максимальный балл больше чем K
        print(1, file=outFile)
    else:
        print(getMinP(), file=outFile)
else:
    print(0, file=outFile)

inFile.close()
outFile.close()
