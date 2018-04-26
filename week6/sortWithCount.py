marks = list(map(int, input().split()))


def CountSort(A):
    A.sort()
    print(*A)


CountSort(marks)
