num = int(input())

last = num
max = 0
count = 0

while num > 0:
    if last == num:
        count += 1
        if count > max:
            max = count
    else:
        count = 1
        last = num
    num = int(input())

print(max)
