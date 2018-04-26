n = int(input())

marks = []

for k in range(n):
    arr = input().split()
    marks.append([arr[0], int(arr[1])])

marks.sort(key=lambda r: r[1], reverse=True)

for mar in marks:
    print(mar[0])
