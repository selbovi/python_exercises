a = int(input())

i = 1

while i <= a:
    print(i * i, end=' ')
    i = i + 1
    if (i * i > a):
        break
