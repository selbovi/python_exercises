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


exec(stdin.read())
