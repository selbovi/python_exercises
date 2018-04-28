n = int(input())

rnd = 5
riddleSet = set([rnd])
total = set(map(int, range(1, n + 1)))


def getIntsList(answers):
    digs = []
    for ans in answers.split():
        if ans.isdigit():
            digs.append(int(ans))
    return set(digs)


for answer in iter(input, 'HELP'):
    mySet = getIntsList(answer)
    yes = len(riddleSet & mySet) > 0

    if not yes:
        total.difference_update(mySet)
    else:
        total = total.intersection(mySet)

eg = sorted(total)

print(*eg)
