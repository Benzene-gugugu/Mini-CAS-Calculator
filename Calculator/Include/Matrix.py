from BasicAlgebra import Number
from typing import NoReturn, List


class Row:
    def __init__(self, row: List[Number]):
        self.__row = row
        self.__width = len(row)

    def setRow(self, row: List[Number]):
        self.__row = row
        self.__width = len(row)

    def getRow(self) -> List[Number]:
        return self.__row

    def getWidth(self) -> int:
        return len(self.__row)

    def __add__(self, other):
        if self.getWidth() != other.getWidth():
            raise ArithmeticError("Incorrect dimensions for the matrix")
        a = []
        for i in range(self.getWidth()):
            a.append(self.getRow()[i] + other.getRow()[i])
        return Row(a)

    def __sub__(self, other):
        if self.getWidth() != other.getWidth():
            raise ArithmeticError("Incorrect dimensions for the matrix")
        a = []
        for i in range(self.getWidth()):
            a.append(self.getRow()[i] - other.getRow()[i])
        return Row(a)

    def __str__(self):
        s = '['
        for n in self.__row:
            s += str(n) + ','
        s = s[0:len(s) - 1]
        s += ']'
        return s


class Matrix:
    def __init__(self, mat: List[Row]):
        self.__mat = mat
        self.__width = mat[0].getWidth()
        self.__height = len(mat)
        for r in mat:
            if len(r.getRow()) != self.__width:
                raise ArithmeticError("Incorrect dimensions for the matrix")

    def setMat(self, mat: List[Row]):
        self.__mat = mat
        self.__width = mat[0].getWidth()
        self.__height = len(mat)
        for r in mat:
            if len(r.getRow()) != self.__width:
                raise ArithmeticError("Incorrect dimensions for the matrix")

    def getMat(self) -> List[Row]:
        return self.__mat

    def getWidth(self) -> int:
        return self.__width

    def getHeight(self) -> int:
        return self.__height

    def __add__(self, other):
        a = []
        for i in range(self.getHeight()):
            a.append(self.getMat()[i] + other.getMat()[i])
        return Matrix(a)

    def __sub__(self, other):
        a = []
        for i in range(self.getHeight()):
            a.append(self.getMat()[i] * other.getMat()[i])
        return Matrix(a)

    def __mul__(self, other):
        if self.getWidth() != other.getHeight():
            raise ArithmeticError("Dimensions are not allowed for multiplication")
        a = []
        for i in range(self.getHeight()):
            r = []
            for j in range(other.getWidth()):
                n = Number('0')
                for k in range(self.getWidth()):
                    n = n + self.getMat()[i].getRow()[k] * self.getMat()[k].getRow()[j]
                r.append(n)
            a.append(Row(r))
        return Matrix(a)

    def __str__(self):
        s = '['
        for r in self.__mat:
            s += str(r) + ',\n'
        s = s[0:len(s) - 2]
        s += ']'
        return s


def determinant(m: Matrix) -> Number:
    tmat: List[Row] = m.getMat()
    mat: List[List[Number]] = [tmat[i].getRow() for i in range(len(tmat))]
    if m.getWidth() != m.getHeight():
        raise ArithmeticError("Dimensions are not allowed for determinant to be carried out")
    if m.getWidth() == 2:
        return mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
    elif m.getWidth() == 3:
        return mat[0][0] * mat[1][1] * mat[2][2] + mat[0][1] * mat[1][2] * mat[2][0] + mat[0][2] * mat[1][0] * mat[2][1] \
               - mat[0][0] * mat[1][2] * mat[2][1] - mat[0][1] * mat[1][0] * mat[2][2] - mat[0][2] * mat[1][1] * mat[2][0]
    else:
        n: int = m.getWidth()
        singular: bool = False
        i: int = 0
        while i < n and not singular:
            if mat[i][i] == Number('0'):
                j: int = 1
                while j < n and mat[j][i] == 0:
                    j += 1
                if mat[j][i] != Number('0'):
                    for k in range(0, n):
                        temp: Number = mat[i][k]
                        mat[i][k] = mat[j][k]
                        mat[j][k] = -temp
                else:
                    singular = True
        if singular:
            return Number('0')
        else:
            pivot: Number = Number('1')
            for k in range(0, n - 1):
                for i in range(k + 1, n):
                    for j in range(k + 1, n):
                        mat[i][j] = mat[k][k] * mat[i][j] - mat[i][k] * mat[k][j]
                        mat[i][j] = mat[i][j] / pivot
                pivot = mat[k][k]
            return mat[n - 1][n - 1]


def inverse(m: Matrix) -> Matrix:
    if determinant(m) == Number('0'):
        raise ArithmeticError("Matrix is singular. Inverse does not exist")
    if m.getWidth() != m.getHeight():
        raise ArithmeticError("Dimensions are not allowed for inverse to be calculated")
    tmat: List[Row] = m.getMat()
    mat: List[List[Number]] = [tmat[i].getRow() for i in range(len(tmat))]
    for p in range(len(mat)):
        pivot: Number = mat[p][p]
        if pivot == Number('0'):
            raise ArithmeticError("Matrix is singular. Inverse does not exist")
        for i in range(len(mat)):
            mat[i][p] = -mat[i][p] / pivot
        for i in range(len(mat)):
            if i != p:
                for j in range(len(mat)):
                    if j != p:
                        mat[i][j] = mat[i][j] + mat[p][j] * mat[i][p]
        for j in range(len(mat)):
            mat[p][j] = mat[p][j] / pivot
        mat[p][p] = Number(1) / pivot
    tmat: List[Row] = [Row(mat[i]) for i in range(len(mat))]
    return Matrix(tmat)
