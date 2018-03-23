a = int(input())
b = int(input())
c = int(input())

l = sorted([a, b, c])
l.reverse()
while len(l) > 0:
    print(l.pop(), end=' ')
