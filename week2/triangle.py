a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    if (a < b):
        k = a
        l = b
    else:
        k = b
        l = a
    if l < c:
        h = c
    else:
        h = l
        l = c
    t1 = h * h
    t2 = k*k + l*l
    if t1 == t2:
        print('rectangular ')
    elif t1 < t2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')
