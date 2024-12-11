from .token import Token, TokenType
class Lexer:
    def __init__(self, parser):
        self.parser = parser
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, s: str):
        self._text = s
        self._pos = 0
        self._current_char = self._text[self._pos]
    def __skip(self):
        while (self._current_char is not None and self._current_char.isspace()):
            self.__forward()
    def __integer(self):
        result = ""
        has_decimal_point = False
        while self._current_char is not None:
            if self._current_char.isdigit():
                result += self._current_char
            elif self._current_char == '.' and not has_decimal_point:
                result += self._current_char
                has_decimal_point = True
            else:
                break
            self.__forward()
        return result
    def __forward(self):
        self._pos += 1
        if self._pos > len(self._text) -1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def __identifier(self) -> str:
        result = ''
        while self._current_char is not None and (self._current_char.isalnum() or self._current_char == '_'):
            result += self._current_char
            self.__forward()
        return result
    def next(self) -> Token:
        while self._current_char:
            if self._current_char.isspace():
                self.__skip()
                continue
            if self._current_char.isalpha() or self._current_char == '_':
                var_name = self.__identifier()
                for var in self.parser.interpreter.variables:
                    if var_name == var.value:
                        if self.parser.assignment_is_here:
                            return Token(TokenType.INTEGER_NUMBER, self.parser.interpreter.variables[var])
                        else:
                            return var

                return Token(TokenType.VARIABLE, var_name)
            if self._current_char.isdigit():
                return Token(TokenType.INTEGER_NUMBER, self.__integer())
            if self._current_char == ':':  # Checking for assignment operator ':='
                var = self._current_char
                self.__forward()
                if self._current_char == "=":
                    var = var + self._current_char
                    self.__forward()
                    self.parser.assignment_is_here=True
                    return Token(TokenType.ASSIGNMENT, var)
            if self._current_char in ["+", "-", "*", "/"]:
                op = self._current_char
                self.__forward()
                return Token(TokenType.OPERATOR, op)
            if self._current_char == "(":
                val = self._current_char
                self.__forward()
                return Token(TokenType.LPAREN, val)
            if self._current_char == ")":
                val = self._current_char
                self.__forward()
                return Token(TokenType.RPAREN, val)
            if self._current_char == ";":
                val = self._current_char
                self.__forward()
                self.parser.assignment_is_here=False

            else:
                raise SyntaxError("bad token")

