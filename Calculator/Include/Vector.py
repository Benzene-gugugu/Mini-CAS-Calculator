from typing import List
from BasicAlgebra import Number


class Vector:
    def __init__(self, v: List[Number]):
        self.__v: List[Number] = v
        self.__dimensions: int = len(v)
        if self.__dimensions < 2:
            raise UserWarning("Smaller dimensions of vector is not allowed")
        if self.__dimensions > 3:
            raise UserWarning("Bigger dimensions of vector is not allowed")

    def getVec(self) -> List[Number]:
        return self.__v

    def setVec(self, v: List[Number]):
        self.__v = v
        self.__dimensions = len(v)
        if self.__dimensions < 2:
            raise UserWarning("Smaller dimensions of vector is not allowed")
        if self.__dimensions > 3:
            raise UserWarning("Bigger dimensions of vector is not allowed")

    def getDim(self) -> Number:
        return self.__dimensions

    def __add__(self, other):
        if self.getDim() != other.getDim():
            raise ArithmeticError("Incorrect dimensions for vector. Calculation is available")
        l = []
        for i in range(self.getDim()):
            l.append(self.getVec()[i] + other.getVec()[i])
        return Vector(l)

    def __sub__(self, other):
        if self.getDim() != other.getDim():
            raise ArithmeticError("Incorrect dimensions for vector. Calculation is available")
        l = []
        for i in range(self.getDim()):
            l.append(self.getVec()[i] - other.getVec()[i])
        return Vector(l)

    def __mul__(self, other):
        l = []
        for i in range(self.getDim()):
            l.append(self.getVec()[i] * other)
        return Vector(l)

    def __str__(self):
        s = '('
        for n in self.__v:
            s += str(n) + ','
        s = s[0:len(s)-1]
        s += ')'
        return s


def dotProduct(vec1: Vector, vec2: Vector) -> Number:
    if vec1.getDim() != vec2.getDim():
        raise ArithmeticError("Incorrect dimensions for vector. Calculation is available")
    n: Number = Number('0')
    for i in range(vec1.getDim()):
        n = n + vec1.getVec()[i] * vec2.getVec()[i]
    return n


def crossProduct(vec1: Vector, vec2: Vector) -> Vector:
    if vec1.getDim() != 3 or vec2.getDim() != 3:
        raise ArithmeticError("Incorrect dimensions for vector. Calculation is available")
    v1: List[Number] = vec1.getVec()
    v2: List[Number] = vec2.getVec()
    l: List[Number] = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
    return Vector(l)
