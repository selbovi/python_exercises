myList = list(map(int, input().split()))

mySet = set([])

for i in myList:
    size = len(mySet)
    mySet.add(i)
    newSize = len(mySet)
    if size == newSize:
        print('YES')
    else:
        print('NO')
