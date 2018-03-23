num = int(input())

i = []

while num > 0:
    i.append(num)
    num = int(input())

m = max(i)
i.count(m)
print(i.count(m))
