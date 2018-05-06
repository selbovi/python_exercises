import copy
import functools
from sys import stdin


class Matrix:
    def __init__(self, listOfLists) -> None:
        self.res = copy.deepcopy(listOfLists)

    def __str__(self) -> str:
        buff = ''
        for lst in self.res:
            buff = buff + functools \
                .reduce((lambda a, b: str(a) + '\t' + str(b)), lst)
            buff += '\n'

        return buff.strip()

    def size(self):
        return len(self.res), len(self.res[0])

    def __add__(self, other):
        ok = []
        for y in range(len(self.res)):
            row = []
            for x in range(len(self.res[y])):
                row.append(self.res[y][x] + other.res[y][x])
            ok.append(row)
        return Matrix(ok)

    def __mul__(self, num):
        ok = []
        for y in range(len(self.res)):
            row = []
            for x in range(len(self.res[y])):
                row.append(self.res[y][x] * num)
            ok.append(row)
        return Matrix(ok)

    def __rmul__(self, num):
        return self.__mul__(num)


exec(stdin.read())
