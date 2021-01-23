from Lexer import *
from typing import List, Dict, Mapping, NoReturn, Any
from BasicAlgebra import *
from Matrix import *
from Vector import *
from Statistics import *


class Parser:
    # Check for all values of the variables
    identval = dict()

    def __init__(self, lexer: Lexer):
        self.tokens: List[Tokens] = lexer.scanTokens()
        self.tokenid: int = 0
        self.curtoken: Token = self.tokens[self.tokenid]
        self.peektoken: Token = self.tokens[self.tokenid + 1]

    # Move to next token
    def nextToken(self):
        self.tokenid += 1
        self.curtoken = self.tokens[self.tokenid]
        if self.tokenid + 1 < len(self.tokens):
            self.peektoken = self.tokens[self.tokenid + 1]
        else:
            self.peektoken = Token(TokenType.NEWLINE, "", None)

    # checks for current token
    def checkToken(self, kind: TokenType):
        return kind.name == self.curtoken.tokentype.name

    # checks for next token
    def checkPeek(self, kind: TokenType):
        return kind.name == self.peektoken.tokentype.name

    # checks for a current token match
    def match(self, kind):
        if not self.checkToken(kind):
            raise SyntaxError("Expected " + str(kind) + ', got ' + str(self.curtoken.tokentype))
        self.nextToken()

    # parses a single statement
    def statement(self):
        while not self.checkToken(TokenType.NEWLINE):
            if self.checkToken(TokenType.PRINT):
                # print("STATEMENT-PRINT")
                self.nextToken()
                print(self.expression())
            elif self.checkToken(TokenType.VAR):
                # print("STATEMENT-VAR")
                self.nextToken()
                ident = self.curtoken.lexeme
                if ident not in Parser.identval:
                    Parser.identval[ident] = None
                self.match(TokenType.IDENTIFIER)
                if self.checkToken(TokenType.ASSIGN):
                    # print("STATEMENT-VAR-NOUNC")
                    self.nextToken()
                    if self.checkToken(TokenType.LEFT_PAREN):
                        # print("STATEMTENT-VAR-VECTOR")
                        l = []
                        self.nextToken()
                        l.append(self.expression())
                        while self.checkToken(TokenType.COMMA):
                            self.nextToken()
                            l.append(self.expression())
                        self.match(TokenType.RIGHT_PAREN)
                        Parser.identval[ident] = Vector(l)
                    elif self.checkToken(TokenType.LEFT_BRACKET) and self.checkPeek(TokenType.LEFT_BRACKET):
                        # print("STATEMENT-VAR-MATRIX/ROW")
                        Parser.identval[ident] = self.matrix()
                    elif self.checkToken(TokenType.LEFT_BRACE):
                        # print("STATEMENT-VAR-LIST")
                        l = []
                        self.nextToken()
                        l.append(self.expression())
                        while self.checkToken(TokenType.COMMA):
                            self.nextToken()
                            l.append(self.expression())
                        self.match(TokenType.RIGHT_BRACE)
                        Parser.identval[ident] = NumList(l)
                    else:
                        # print("STATEMENT-VAR-NUM")
                        Parser.identval[ident] = self.expression()
            else:
                raise SyntaxError("Expected var or print")

    # Parses an expression
    def expression(self):
        # print("EXPRESSION")
        val = self.term()
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            if self.checkToken(TokenType.PLUS):
                self.nextToken()
                val = val + self.term()
            else:
                self.nextToken()
                val = val - self.term()
        return val

    # Parses a term
    def term(self):
        # print("TERM")
        val = self.factor()
        while self.checkToken(TokenType.STAR) or self.checkToken(TokenType.SLASH):
            if self.checkToken(TokenType.STAR):
                self.nextToken()
                val = val * self.factor()
            else:
                self.nextToken()
                val = val / self.factor()
        return val

    # Parses a factor
    def factor(self):
        # print("FACTOR")
        val = self.unary()
        while self.checkToken(TokenType.POWER):
            self.nextToken()
            val = val ** self.unary()
        return val

    # Parses an unary element
    def unary(self):
        # print("UNARY")
        if self.checkToken(TokenType.PLUS):
            self.nextToken()
            return self.primary()
        elif self.checkToken(TokenType.MINUS):
            self.nextToken()
            return -self.primary()
        return self.primary()

    # Parses the primary element
    def primary(self):
        # print("PRIMARY (" + self.curtoken.lexeme + ")")
        if self.checkToken(TokenType.LEFT_PAREN):
            self.nextToken()
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return val
        elif self.checkToken(TokenType.NUMBER):
            val = self.curtoken.literal
            self.nextToken()
            return val
        elif self.checkToken(TokenType.IDENTIFIER):
            if self.curtoken.lexeme not in Parser.identval:
                raise SyntaxError("Undeclared Variable " + self.curtoken.lexeme)
            val = Parser.identval[self.curtoken.lexeme]
            self.nextToken()
            return val
        elif self.checkToken(TokenType.E):
            self.nextToken()
            return E
        elif self.checkToken(TokenType.PI):
            self.nextToken()
            return PI
        elif self.checkToken(TokenType.SIN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return nsin(val)
        elif self.checkToken(TokenType.COS):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return ncos(val)
        elif self.checkToken(TokenType.TAN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return ntan(val)
        elif self.checkToken(TokenType.ASIN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return arcsin(val)
        elif self.checkToken(TokenType.ACOS):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return arccos(val)
        elif self.checkToken(TokenType.ATAN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return arctan(val)
        elif self.checkToken(TokenType.LOG):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return nlog(val1, val2)
        elif self.checkToken(TokenType.INVERSE):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return inverse(val)
        elif self.checkToken(TokenType.DETERMINANT):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return determinant(val)
        elif self.checkToken(TokenType.DOTPRODUCT):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return dotProduct(val1, val2)
        elif self.checkToken(TokenType.CROSSPRODUCT):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return crossProduct(val1, val2)
        elif self.checkToken(TokenType.MEDIAN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return median(val)
        elif self.checkToken(TokenType.LOWERQ):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return lowerQ(val)
        elif self.checkToken(TokenType.UPPERQ):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return upperQ(val)
        elif self.checkToken(TokenType.MODE):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return mode(val)
        elif self.checkToken(TokenType.MEAN):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return mean(val)
        elif self.checkToken(TokenType.PVAR):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return popVar(val)
        elif self.checkToken(TokenType.SVAR):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return samVar(val)
        elif self.checkToken(TokenType.NPR):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return nPr(val1, val2)
        elif self.checkToken(TokenType.NCR):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return nCr(val1, val2)
        elif self.checkToken(TokenType.BINP):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return BinP(val1, val2, val3)
        elif self.checkToken(TokenType.BINC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.COMMA)
            val4 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return BinC(val1, val2, val3, val4)
        elif self.checkToken(TokenType.GEOP):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return GeoP(val1, val2)
        elif self.checkToken(TokenType.GEOC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return GeoC(val1, val2, val3)
        elif self.checkToken(TokenType.POP):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return PoP(val1, val2)
        elif self.checkToken(TokenType.POC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return PoC(val1, val2, val3)
        elif self.checkToken(TokenType.NC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return NC(val1, val2, val3)
        elif self.checkToken(TokenType.TC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return TC(val1, val2)
        elif self.checkToken(TokenType.CHIC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return ChiC(val1, val2)
        elif self.checkToken(TokenType.INC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.COMMA)
            val3 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return INC(val1, val2, val3)
        elif self.checkToken(TokenType.ITC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return ITC(val1, val2)
        elif self.checkToken(TokenType.ICHIC):
            self.nextToken()
            self.match(TokenType.LEFT_PAREN)
            val1 = self.expression()
            self.match(TokenType.COMMA)
            val2 = self.expression()
            self.match(TokenType.RIGHT_PAREN)
            return IChiC(val1, val2)
        else:
            raise SyntaxError("Unexpected token at " + self.curtoken.lexeme)

    # checking for matrices
    def matrix(self):
        # print("MATRIX")
        l = []
        self.match(TokenType.LEFT_BRACKET)
        l.append(self.row())
        while self.checkToken(TokenType.COMMA):
            self.nextToken()
            l.append(self.row())
        self.match(TokenType.RIGHT_BRACKET)
        return Matrix(l)

    # checking for rows in a matrix
    def row(self):
        # print("ROW")
        l = []
        self.match(TokenType.LEFT_BRACKET)
        l.append(self.expression())
        while self.checkToken(TokenType.COMMA):
            self.nextToken()
            l.append(self.row())
        self.match(TokenType.RIGHT_BRACKET)
        return Row(l)
