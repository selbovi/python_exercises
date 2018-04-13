num = int(input())

one = '+___ '


def concat(template, x):
    str = ''
    for i in range(x):
        str = str + template
    return str


def two(y):
    res = ''
    for i in range(y):
        res = res + '|' + str(i + 1) + ' / '
    return res


three = '|__\ '
four = '|    '


def printFlag(x):
    print(concat(one, x))
    print(two(x))
    print(concat(three, x))
    print(concat(four, x))


printFlag(num)
