n = int(input())

total = set(map(int, range(1, n + 1)))


def getIntsList(answers):
    digs = []
    for ans in answers.split():
        if ans.isdigit():
            digs.append(int(ans))
    return set(digs)


mySet = set()
for answer in iter(input, 'HELP'):
    if answer != 'YES' and answer != 'NO':
        mySet = getIntsList(answer)
    else:
        if answer == 'YES':
            total = total.intersection(mySet)
        elif answer == 'NO':
            total.difference_update(mySet)

eg = sorted(total)

print(*eg)
