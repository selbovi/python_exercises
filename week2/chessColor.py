c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

isEvenC1 = c1 % 2 != 0
isEvenC2 = c2 % 2 != 0
isEvenR1 = r1 % 2 != 0
isEvenR2 = c2 % 2 != 0

r_ = (isEvenC1 and isEvenC2 and isEvenR1 and isEvenR2)
even_r_ = (isEvenC1 and isEvenC2 and not isEvenR1 and not isEvenR2)
if r_ or (not isEvenC1 and not isEvenC2 and not isEvenR1 and not isEvenR2):
    print('YES')
elif even_r_ or (not isEvenC1 and not isEvenC2 and isEvenR1 and isEvenR2):
    print('YES')
else:
    print('NO')
