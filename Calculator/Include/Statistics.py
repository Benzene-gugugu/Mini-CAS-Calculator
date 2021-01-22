from typing import List, Union
from BasicAlgebra import Number, E
from collections import Counter
from scipy.stats import norm, t, chi2


class NumList:
    def __init__(self, numlist: List[Number]):
        self.__list = numlist

    def getList(self) -> List[Number]:
        return self.__list

    def appendList(self, num: Number):
        self.__list.append(num)

    def removeList(self, num: Number):
        if num not in self.__list:
            pass
        self.__list.remove(num)

    def __add__(self, other):
        temp = self.getList()
        if isinstance(other, Number):
            temp.append(other)
        else:
            for num in other.getList():
                temp.append(num)
        return NumList(temp)

    def getSize(self) -> int:
        return len(self.__list)

    def getSum(self) -> float:
        tot = 0
        for n in self.__list:
            tot = tot + n.getNum()
        return tot

    def getSumSquare(self) -> float:
        tot = 0
        for n in self.__list:
            tot = tot + n.getNum() * n.getNum()
        return tot

    def __str__(self):
        s = '{'
        for n in self.__v:
            s += str(n) + ','
        s = s[0:len(s) - 1]
        s += '}'
        return s


def mean(l: NumList) -> Number:
    return Number(l.getSum() / l.getSize())


def median(l: NumList) -> Number:
    temp: List[Number] = l.getList()
    temp.sort()
    if l.getSize() % 2 == 1:
        return temp[(l.getSize() - 1) // 2]
    else:
        return (temp[l.getSize() // 2] + temp[l.getSize() // 2 - 1]) / Number('2')


def lowerQ(l: NumList) -> Number:
    temp: List[Number] = l.getList()
    temp.sort()
    if l.getSize() % 2 == 1:
        ttemp: List[Number] = temp[:(l.getSize() - 1) // 2]
        if len(ttemp) % 2 == 1:
            return ttemp[(len(ttemp) - 1) // 2]
        else:
            return (ttemp[len(ttemp) // 2] + ttemp[len(ttemp) // 2 - 1]) / Number('2')
    else:
        ttemp: List[Number] = temp[:l.getSize() // 2]
        if len(ttemp) % 2 == 1:
            return ttemp[(len(ttemp) - 1) // 2]
        else:
            return (ttemp[len(ttemp) // 2] + ttemp[len(ttemp) // 2 - 1]) / Number('2')


def upperQ(l: NumList) -> Number:
    temp: List[Number] = l.getList()
    temp.sort()
    if l.getSize() % 2 == 1:
        ttemp: List[Number] = temp[(l.getSize() - 1) // 2 + 1:]
        if len(ttemp) % 2 == 1:
            return ttemp[(len(ttemp) - 1) // 2]
        else:
            return (ttemp[len(ttemp) // 2] + ttemp[len(ttemp) // 2 - 1]) / Number('2')
    else:
        ttemp: List[Number] = temp[l.getSize() // 2:]
        if len(ttemp) % 2 == 1:
            return ttemp[(len(ttemp) - 1) // 2]
        else:
            return (ttemp[len(ttemp) // 2] + ttemp[len(ttemp) // 2 - 1]) / Number('2')


def mode(l: NumList) -> Number:
    d = dict()
    for n in l.getList():
        if n.getNum() not in d:
            d[n.getNum()] = 1
        else:
            d[n.getNum()] += 1
    maxn = -1
    maxe = None
    for e in d:
        if d.get(e) > maxn:
            maxn = d.get(e)
            maxe = e
    return Number(maxe)


def popVar(l: NumList) -> Number:
    return Number(l.getSumSquare() / l.getSize() - (l.getSum() / l.getSize()) ** 2)


def samVar(l: NumList) -> Number:
    return Number((l.getSumSquare() - ((l.getSum() ** 2) / (l.getSize()))) / (l.getSize() - 1))


def nPr(n: Number, r: Number) -> Number:
    prod = Number("1")
    for i in range(int(n.getNum()), int(n.getNum() - r.getNum()), -1):
        prod = prod * Number(i)
    return prod


def nCr(n: Number, r: Number) -> Number:
    return nPr(n, r) / nPr(r, r)


def BinP(n: Number, p: Number, x: Number) -> Number:
    return nCr(n, x) * (p ** x) * ((Number(1) - p) ** (n - x))


def BinC(n: Number, p: Number, lb: Number, ub: Number) -> Number:
    tp = Number('0')
    for x in range(int(lb.getNum()), int(ub.getNum() + 1)):
        tp = tp + BinP(n, p, Number(x))
    return tp


def GeoP(p: Number, x: Number) -> Number:
    return (Number(1) - p) ** (x - Number(1)) * p


def GeoC(p: Number, lb: Number, ub: Number) -> Number:
    tp = Number('0')
    for x in range(int(lb.getNum()), int(ub.getNum() + 1)):
        tp = tp + GeoP(p, Number(x))
    return tp


def PoP(mean: Number, x: Number) -> Number:
    return (E ** (-mean)) * (mean ** x) / nPr(x, x)


def PoC(mean: Number, lb: Number, ub: Number) -> Number:
    tp = Number('0')
    for x in range(int(lb.getNum()), int(ub.getNum() + 1)):
        tp = tp + PoP(mean, Number(x))
    return tp


def NC(mean: Number, var: Number, x: Number) -> Number:
    z = (x.getNum() - mean.getNum()) / (var.getNum() ** (1 / 2))
    return Number(norm.cdf(z))


def INC(mean: Number, var: Number, p: Number) -> Number:
    z = norm.ppf(p.getNum())
    return Number(z * (var.getNum() ** (1 / 2)) + mean.getNum())


def TC(df: Number, x: Number) -> Number:
    return Number(t.cdf(x.getNum(), df.getNum()))


def ITC(df: Number, p: Number) -> Number:
    return Number(t.ppf(p.getNum(), df.getNum()))


def ChiC(df: Number, x: Number) -> Number:
    return Number(chi2.cdf(x.getNum(), df.getNum()))


def IChiC(df: Number, p: Number) -> Number:
    return Number(chi2.ppf(p.getNum(), df.getNum()))
