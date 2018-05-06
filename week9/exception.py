import copy
import functools
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


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
        if len(self.res) != len(other.res):
            raise MatrixError(self, other)

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

    def transpose(self):
        self.res = Matrix.transposed(self).res
        return self

    @staticmethod
    def transposed(m):
        ok = []
        for x in range(len(m.res[0])):
            row = []
            for y in range(len(m.res)):
                row.append(m.res[y][x])
            ok.append(row)

        return Matrix(ok)


exec(stdin.read())
