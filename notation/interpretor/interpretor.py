from .token import Token
from .lexer import Lexer
from .parser import Parser

class Interpeter:
    def eval(self, text):
        lexer = Lexer(text)
        parser = Parser(lexer)
        return parser.parse()