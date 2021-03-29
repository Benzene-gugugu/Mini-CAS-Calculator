from Lexer import Lexer
from Parser import Parser


# Process of using the lexer and parser to execute the code
def run(source: str, out):
    lex = Lexer(source)
    # out(lex.scanTokens())
    parse = Parser(lex, out)
    parse.statement()
    return parse.identval


def run_line(strin, out):
    line: str = strin
    try:
        if line == '':
            raise UserWarning("There is no code to execute")
        return run(line, out)
    except ArithmeticError as e:
        out(e)
    except SyntaxError as e:
        out(e)
    except UserWarning as w:
        out(w)
    except Exception as e:
        out(e)


'''
def run_cli():
    while True:
        line: str = input()
        try:
            if line == '':
                break
            run(line, print)
        except ArithmeticError as e:
            print(e)
        except SyntaxError as e:
            print(e)
        except UserWarning as w:
            print(w)
        except Exception as e:
            print(e)
'''
