from enum import Enum, unique
from BasicAlgebra import Number
from typing import List, Tuple, Mapping, Dict, Any, NoReturn


@unique # ensure that all the tokens are unique
class TokenType(Enum):
    """
    Corresponding values and type of tokens:
    value=0: special characters
    0<value<100: Literals
    100<value<110: Operations
    110<value<120: Algebraic Keywords
    120<value<130: Matrix Keywords
    130<value<140: Vector Keywords
    140<value<150: 1-Var Statistics Keywords
    150<value<160: Discrete Distribution Keywords
    160<value<170: Continuous Distribution Keywords
    200<value<210: Brackets
    210<value<220: Operations
    """
    # Brackets
    LEFT_PAREN = 201
    RIGHT_PAREN = 202
    LEFT_BRACE = 203
    RIGHT_BRACE = 204
    LEFT_BRACKET = 205
    RIGHT_BRACKET = 206
    # Operations
    COMMA = 211
    DOT = 212
    MINUS = 213
    PLUS = 214
    SLASH = 215
    STAR = 216
    POWER = 217
    ASSIGN = 218
    # Literals
    IDENTIFIER = 1
    NUMBER = 2
    # Language Keywords
    PRINT = 101
    VAR = 102
    # Algebra Keywords
    E = 111  # 0
    PI = 112  # 0
    SIN = 113  # 1
    COS = 114  # 1
    TAN = 115  # 1
    ASIN = 116  # 1
    ACOS = 117  # 1
    ATAN = 118  # 1
    LOG = 119  # 2
    # Matrix Keywords
    INVERSE = 121  # 1
    DETERMINANT = 122   # 1
    # Vector Keywords
    DOTPRODUCT = 131  # 2
    CROSSPRODUCT = 132  # 2
    # One Variable Statistics Keywords
    MEDIAN = 141  # 1
    LOWERQ = 142  # 1
    UPPERQ = 143  # 1
    MODE = 144  # 1
    MEAN = 145  # 1
    PVAR = 146  # 1
    SVAR = 147  # 1
    # Discrete Probability Keywords
    NPR = 151  # 2
    NCR = 152  # 2
    BINP = 153  # 3
    BINC = 154  # 4
    GEOP = 155  # 2
    GEOC = 156  # 3
    POP = 157  # 2
    POC = 158  # 3
    # Inferential Statistics Keywords
    NC = 161  # 3
    TC = 162  # 2
    CHIC = 163  # 2
    INC = 164  # 3
    ITC = 165  # 2
    ICHIC = 166  # 2
    # Special
    NEWLINE = 0


# Defining the token type
class Token:
    def __init__(self, tokentype: TokenType, lexeme: str, literal: Any):
        self.tokentype = tokentype
        self.lexeme = lexeme
        self.literal = literal

    def __str__(self) -> str:
        return str(self.tokentype) + " " + self.lexeme + " " + str(self.literal)


# Lexing takes place through this class
class Lexer:
    # Converting certain keywords to specific tokens
    keywords: Dict[str, TokenType] = {
        'var': TokenType.VAR,
        'print': TokenType.PRINT,
        'sin': TokenType.SIN,
        'cos': TokenType.COS,
        'tan': TokenType.TAN,
        'arcsin': TokenType.ASIN,
        'arccos': TokenType.ACOS,
        'arctan': TokenType.ATAN,
        'log': TokenType.LOG,
        'e': TokenType.E,
        'pi': TokenType.PI,
        'inverse': TokenType.INVERSE,
        'det': TokenType.DETERMINANT,
        'dot': TokenType.DOTPRODUCT,
        'cross': TokenType.CROSSPRODUCT,
        'median': TokenType.MEDIAN,
        'lowerq': TokenType.LOWERQ,
        'upperq': TokenType.UPPERQ,
        'mode': TokenType.MODE,
        'mean': TokenType.MEAN,
        'pvar': TokenType.PVAR,
        'svar': TokenType.SVAR,
        'nPr': TokenType.NPR,
        'nCr': TokenType.NCR,
        'BinP': TokenType.BINP,
        'BinC': TokenType.BINC,
        'GeoP': TokenType.GEOP,
        'GeoC': TokenType.GEOC,
        'PoP': TokenType.POP,
        'PoC': TokenType.POC,
        'NC': TokenType.NC,
        'TC': TokenType.TC,
        'ChiC': TokenType.CHIC,
        'INC': TokenType.INC,
        'ITC': TokenType.ITC,
        "IChiC": TokenType.ICHIC
    }

    def __init__(self, source: str):
        self.__source: str = source
        self.__tokens: List[Token] = []
        self.__start = 0
        self.__current = 0

    # Whether the end of the statement is reached
    def __isAtEnd(self) -> bool:
        return self.__current >= len(self.__source)

    # Move one character forward
    def __advance(self) -> str:
        self.__current += 1
        return self.__source[self.__current - 1]

    # Conveniently add a token
    def __addToken(self, tokentype: TokenType, literal: Any = None) -> NoReturn:
        text: str = self.__source[self.__start:self.__current]
        self.__tokens.append(Token(tokentype, text, literal))

    # Check for marching character
    def __match(self, expected: str) -> bool:
        if self.__isAtEnd():
            return False
        if self.__source[self.__current] != expected:
            return False
        self.__current += 1
        return True

    # Check te character
    def __peek(self) -> str:
        if self.__isAtEnd():
            return '\n'
        return self.__source[self.__current]

    # Check the next character
    def __peekNext(self) -> str:
        if self.__current + 1 >= len(self.__source):
            return '\n'
        return self.__source[self.__current + 1]

    # Check for numbers
    def __number(self) -> NoReturn:
        while self.__peek().isdigit():
            self.__advance()
        if self.__peek() == '.' and self.__peekNext().isdigit:
            self.__advance()
            while self.__peek().isdigit():
                self.__advance()
        self.__addToken(TokenType.NUMBER, Number(self.__source[self.__start:self.__current]))

    # Check for identifiers or keywords
    def __identifier(self) -> NoReturn:
        while self.__peek().isalnum():
            self.__advance()
        text: str = self.__source[self.__start:self.__current]
        tokentype: TokenType = Lexer.keywords.get(text)
        if tokentype is None:
            tokentype = TokenType.IDENTIFIER
        self.__addToken(tokentype)

    # Look for a single token
    def __scanToken(self) -> NoReturn:
        c = self.__advance()
        if c == '(':
            self.__addToken(TokenType.LEFT_PAREN)
        elif c == ')':
            self.__addToken(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.__addToken(TokenType.LEFT_BRACE)
        elif c == '}':
            self.__addToken(TokenType.RIGHT_BRACE)
        elif c == '[':
            self.__addToken(TokenType.LEFT_BRACKET)
        elif c == ']':
            self.__addToken(TokenType.RIGHT_BRACKET)
        elif c == '+':
            self.__addToken(TokenType.PLUS)
        elif c == '-':
            self.__addToken(TokenType.MINUS)
        elif c == '*':
            self.__addToken(TokenType.STAR)
        elif c == '/':
            self.__addToken(TokenType.SLASH)
        elif c == '^':
            self.__addToken(TokenType.POWER)
        elif c == ',':
            self.__addToken(TokenType.COMMA)
        elif c == '.':
            self.__addToken(TokenType.DOT)
        elif c == '=':
            self.__addToken(TokenType.ASSIGN)
        elif c == ' ' or c == '\r' or c == '\t':
            pass
        elif c == '\n':
            pass
        else:
            if c.isdigit():
                self.__number()
            elif c.isalpha():
                self.__identifier()
            else:
                raise SyntaxError("Unexpected character")

    # look for all tokens
    def scanTokens(self) -> List[Token]:
        while not self.__isAtEnd():
            self.__start = self.__current
            self.__scanToken()
        self.__tokens.append(Token(TokenType.NEWLINE, "", None))
        return self.__tokens
