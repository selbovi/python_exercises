a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if (a == a2 and b == b2 and c == c2):
    print('Boxes are equal')
elif (a - a2 > 0 and b - b2 > 0 and c - c2 > 0):
    print('The first box is larger than the second one')
elif (a - a2 < 0 and b - b2 < 0 and c - c2 < 0):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
