last = int(input())

pr = last > 0

sum = 0
total = 0

while last > 0:
    sum = sum + last
    total = total + 1
    last = int(input())

if pr:
    print(str(sum / total))
