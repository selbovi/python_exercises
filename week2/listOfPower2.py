a = int(input())

max = 1

while max <= a:
    power = 0
    lastPower = 0
    res = 2
    while power <= lastPower:
        res = res * 2
        i = i + 1
        if (i * i > a):
            break

