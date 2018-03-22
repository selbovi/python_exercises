x = int(input())
y = int(input())

apartsInPod = y - x + 1

if y % apartsInPod == 0 and (x - 1) % apartsInPod == 0:
    print('YES')
else:
    print('NO')
