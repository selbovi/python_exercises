a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

res = False

f = []
f.append(a)
f.append(b)
f.append(c)
f.sort()
s = []
s.append(a2)
s.append(b2)
s.append(c2)
s.sort()
if (f[0] == s[0] and f[1] == s[1] and f[2] == s[2]):
    print('Boxes are equal')
elif (f[0] >= s[0] and f[1] >= s[1] and f[2] >= s[2]):
    print('The first box is larger than the second one')
elif (f[0] <= s[0] and f[1] <= s[1] and f[2] <= s[2]):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
