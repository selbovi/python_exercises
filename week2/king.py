c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

b = abs(c1 - c2) <= 1 and (abs(r1 - r2) <= 1)
if b:
    print('YES')
else:
    print('NO')
