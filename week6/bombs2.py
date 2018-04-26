def getSortedAndIndexed(total, intList):
    res = []
    for i in range(total):
        res.append((i, intList[i]))

    res.sort(key=lambda tup: tup[1])

    return res


villagesNum = int(input())
inc = list(map(int, input().split()))
mapVillages = getSortedAndIndexed(villagesNum, inc)
sheltersNum = int(input())
roadToShelter = list(map(int, input().split()))
mapShelters = getSortedAndIndexed(sheltersNum, roadToShelter)


# villagesNum = 10
# inc = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
# mapVillages = getSortedAndIndexed(villagesNum, inc)
# sheltersNum = 10
# roadToShelter = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]
# mapShelters = getSortedAndIndexed(sheltersNum, roadToShelter)


# villagesNum = 4
# inc = [1, 2, 6, 10]
# mapVillages = getSortedAndIndexed(villagesNum, inc)
# sheltersNum = 2
# roadToShelter = [7, 3]
# mapShelters = getSortedAndIndexed(sheltersNum, roadToShelter)

# villagesNum = 1
# inc = [1]
# mapVillages = getSortedAndIndexed(villagesNum, inc)
# sheltersNum = 1
# roadToShelter = [1]
# mapShelters = getSortedAndIndexed(sheltersNum, roadToShelter)

# print(mapVillages)
# print(mapShelters)

def getNearestShelter(villagePos, shelters, startSearchIndex):
    delta = -1
    mayBeReturnedShelter = shelters[startSearchIndex]
    mayBeReturnedShelterInd = startSearchIndex
    for shelterIndex in range(startSearchIndex, len(shelters)):
        currentShelter = shelters[shelterIndex]
        currentShelterPos = currentShelter[1]
        if (villagePos == currentShelterPos):
            return currentShelter, shelterIndex
        else:
            newDelta = abs(currentShelterPos - villagePos)
            if (delta < 0):
                delta = newDelta
            else:
                if (newDelta < delta):
                    delta = newDelta
                    mayBeReturnedShelter = currentShelter
                    mayBeReturnedShelterInd = shelterIndex
                else:
                    return shelters[shelterIndex - 1], shelterIndex - 1

    return mayBeReturnedShelter, mayBeReturnedShelterInd


matched = []
shelterStartSearchIndex = 0
firstShelter = mapShelters[0]
if sheltersNum == 1:
    for vil in mapVillages:
        matched.append([vil[0], firstShelter[0]])
else:
    for vil in mapVillages:
        posOfVillage = vil[1]
        posOfFirstShelter = firstShelter[1]
        lastShelter = mapShelters[len(mapShelters) - 1]
        posOfLastShelter = lastShelter[1]
        if (posOfVillage <= posOfFirstShelter):
            matched.append([vil[0], firstShelter[0]])
        elif (posOfVillage >= posOfLastShelter):
            matched.append([vil[0], lastShelter[0]])
        else:
            nearestShelter, newSearchIndex = getNearestShelter(
                posOfVillage,
                mapShelters,
                shelterStartSearchIndex
            )
            shelterStartSearchIndex = newSearchIndex
            matched.append([vil[0], nearestShelter[0]])

matched.sort(key=lambda res: res[0])

for m in matched:
    print(m[1] + 1, end=' ')
