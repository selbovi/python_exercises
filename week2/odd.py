a = int(input())
b = int(input())
c = int(input())

c_ = (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)
if (c_) and ((a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0)):
    print('YES')
else:
    print('NO')
