num = int(input())

prevmax = 0
lastMax = 0
while num > 0:
    if num > lastMax:
        prevmax = lastMax
        lastMax = num
    elif num > prevmax:
        prevmax = num
    num = int(input())

if prevmax > 0:
    print(prevmax)
