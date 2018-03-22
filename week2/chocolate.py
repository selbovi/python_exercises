n = int(input())
m = int(input())
k = int(input())

if (n):
    print('YES')
elif (isEvenC1 and isEvenC2 and not isEvenR1 and not isEvenR2) or (not  isEvenC1 and not isEvenC2 and isEvenR1 and isEvenR2):
    print('YES')
else:
    print('NO')
