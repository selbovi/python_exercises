inc = list(map(int, input().split()))
lim = inc[0]
users = inc[1]

total = []

for i in range(users):
    total.append(int(input()))

total.sort()

i = 0

while lim > 0 and i < users:
    lim = lim - total.pop(0)
    if (lim > 0):
        i += 1

print(i)
