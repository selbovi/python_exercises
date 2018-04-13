num = int(input())


def ladder(x):
    for i in range(x):
        for n in range(i + 1):
            print(n + 1, end='')
        print()


ladder(num)
