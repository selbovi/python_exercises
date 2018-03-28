a = int(input())
b = int(input())
c = int(input())
d = int(input())

total = b
while d > 0:
    total = (b * 100 + c) + (a / 100) * (b * 100 + c)
    b = int(total // 100)
    c = int(total % 100)
    d -= 1

print(int(total // 100), int(total % 100))
