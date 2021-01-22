from typing import List, Tuple, Mapping, Dict, Any, Set
from math import sin, cos, tan, asin, acos, atan, e, pi, log


class Number:
    def __init__(self, n):
        self.__num: float = float(n)

    def getNum(self) -> float:
        return self.__num

    def setNum(self, n: str):
        self.__num = float(n)

    def __str__(self) -> str:
        return str(self.__num)

    def __lt__(self, other):
        return self.getNum() < other.getNum()

    def __eq__(self, other):
        return self.getNum() == other.getNum()

    def __gt__(self, other):
        return other.getNum() < self.getNum()

    def __ne__(self, other):
        return not self.getNum() == other.getNum

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        return Number(self.getNum() + other.getNum())

    def __sub__(self, other):
        return Number(self.getNum() - other.getNum())

    def __neg__(self):
        return Number(-self.getNum())

    def __mul__(self, other):
        return Number(self.getNum() * other.getNum())

    def __truediv__(self, other):
        return Number(self.getNum() / other.getNum())

    def __pow__(self, power, modulo=None):
        return Number(self.getNum() ** power.getNum())


def nsin(n: Number) -> Number:
    return Number(str(sin(n.getNum())))


def ncos(n: Number) -> Number:
    return Number(str(cos(n.getNum())))


def ntan(n: Number) -> Number:
    return Number(str(tan(n.getNum())))


def arcsin(n: Number) -> Number:
    return Number(str(asin(n.getNum())))


def arccos(n: Number) -> Number:
    return Number(str(acos(n.getNum())))


def arctan(n: Number) -> Number:
    return Number(str(atan(n.getNum())))


def nlog(n: Number, b: Number = Number('10')) -> Number:
    return Number(str(log(n.getNum(), b.getNum())))


E = Number(str(e))
PI = Number(str(pi))
