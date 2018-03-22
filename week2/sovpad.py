a = int(input())
b = int(input())
c = int(input())

d = 0

if (a == b):
    d = d + 1
if (a == c):
    d = d + 1
if (b == c):
    d = d + 1
if (d == 1):
    d = 2
print(str(d))
