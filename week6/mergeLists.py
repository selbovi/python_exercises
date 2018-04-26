a = list(map(int, input().split()))
b = list(map(int, input().split()))

while len(a) > 0 or len(b) > 0:
    if (len(a) > 0 and len(b) > 0):
        if (a[0] < b[0]):
            print(a.pop(0), end=' ')
        elif a[0] == b[0]:
            print(b.pop(0), end=' ')
            print(a.pop(0), end=' ')
        else:
            print(b.pop(0), end=' ')
    elif (len(a) > 0):
        print(*a)
        a = []
    else:
        print(*b)
        b = []
