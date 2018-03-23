a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

can = False
# ab пролазит
if (a <= d):
    if (b <= e):
        can = True
elif b <= d:
    if a <= e:
        can = True

# ac пролазит
if not can:
    if (a <= d):
        if (c <= e):
            can = True
    elif c <= d:
        if a <= e:
            can = True

# bc пролазит
if not can:
    if (b <= d):
        if (c <= e):
            can = True
    elif c <= d:
        if b <= e:
            can = True

if can:
    print('YES')
else:
    print('NO')
