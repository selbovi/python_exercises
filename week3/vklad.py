a = int(input())
b = int(input())
c = int(input())

total = (b * 100 + c) + (a / 100) * (b * 100 + c)

print(int(total // 100), int(total % 100))
