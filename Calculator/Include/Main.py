from Lexer import Lexer
from Parser import Parser


# Process of using the lexer and parser to execute the code
def run(source: str):
    lex = Lexer(source)
    parse = Parser(lex)
    parse.statement()


def main() -> int:
    while True:
        line: str = input()
        if line is None:
            break
        # run(line)
        try:
            run(line)
        except ArithmeticError as e:
            print(e)
        except SyntaxError as e:
            print(e)
        except UserWarning as w:
            print(w)
        except Exception as e:
            print(e)
    return 0


if __name__=='__main__':
    main()
